"""Sync Substack posts into _posts/ as Jekyll posts.

Run by .github/workflows/substack-sync.yml every Wednesday, and can also be
run locally from the repo root to backfill posts:

    pip install python-dateutil requests markdownify beautifulsoup4
    python scripts/substack_sync.py

Feed sources, tried in order:
  1. rss2json proxy — works from GitHub Actions, whose IPs Substack blocks.
  2. Substack's own API — works from a normal connection (e.g. a laptop),
     but returns 403 from GitHub Actions.

Env vars: DRY_RUN=true to only log, MANIFEST_PATH to change where the
new-post manifest is written (used by the workflow's PR step).
"""
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from dateutil import parser as date_parser
from pathlib import Path
from urllib.parse import urlparse, quote

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# rss2json proxies the feed from their servers, bypassing Cloudflare
# bot protection that blocks all direct requests from GitHub Actions IPs.
SUBSTACK_RSS = "https://jamesmaconochie.substack.com/feed"
RSS2JSON_URL = f"https://api.rss2json.com/v1/api.json?rss_url={quote(SUBSTACK_RSS, safe='')}"
POSTS_DIR = "_posts"
IMAGES_DIR = "assets/images"
DELAY_DAYS = 7
MANIFEST_PATH = os.environ.get("MANIFEST_PATH", "/tmp/new_posts_manifest.json")
SUBSTACK_API = "https://jamesmaconochie.substack.com/api/v1"

# ── Helpers ──────────────────────────────────────────────────────────

ROMAN_MAP = [
    ("XVIII", "18"), ("XVII", "17"), ("XVI", "16"), ("XV", "15"),
    ("XIV", "14"), ("XIII", "13"), ("XII", "12"), ("XI", "11"),
    ("X", "10"), ("IX", "9"), ("VIII", "8"), ("VII", "7"),
    ("VI", "6"), ("V", "5"), ("IV", "4"), ("III", "3"),
    ("II", "2"), ("I", "1"),
]


def normalize_title(title):
    """Normalize a title for fuzzy duplicate matching.

    Lowercases, strips subtitles after colons, converts Roman numeral
    part numbers to Arabic, and removes punctuation.
    """
    t = title.lower()
    # Strip subtitle after colon
    t = t.split(":")[0]
    # Roman → Arabic for part numbers (e.g. "part ii" → "part 2")
    for roman, arabic in ROMAN_MAP:
        t = re.sub(
            rf"\bpart\s+{roman.lower()}\b",
            f"part {arabic}",
            t,
        )
    # Remove punctuation (keep letters, digits, whitespace)
    t = re.sub(r"[^\w\s]", "", t)
    # Collapse whitespace
    t = re.sub(r"\s+", " ", t).strip()
    return t


def slugify(title):
    """Convert title to URL-friendly slug."""
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[-\s]+", "-", slug)
    return slug.strip("-")


# ── Substack Tags via Archive API ──────────────────────────────────

SUBSTACK_ARCHIVE_URL = "https://jamesmaconochie.substack.com/api/v1/archive"


def fetch_substack_tags(limit=20):
    """Fetch post tags from Substack's archive API.

    Unlike the RSS feed, this API is not behind Cloudflare and can be
    called directly. Returns a dict mapping canonical_url → list of
    tag slugs (e.g. ['ai', 'attention-economy', 'wisdom']).
    """
    tags_by_url = {}
    try:
        resp = requests.get(
            SUBSTACK_ARCHIVE_URL,
            params={"limit": limit},
            timeout=30,
        )
        resp.raise_for_status()
        posts = resp.json()
        for post in posts:
            url = post.get("canonical_url", "")
            post_tags = post.get("postTags", [])
            if url and post_tags:
                slugs = [t["slug"] for t in post_tags if t.get("slug")]
                tags_by_url[url] = slugs
        print(f"Fetched tags for {len(tags_by_url)} posts from Substack API")
    except Exception as e:
        print(f"WARNING: Could not fetch Substack tags: {e}")
        print("  Falling back to 'substack-sync' category")
    return tags_by_url


# ── Feed Sources ───────────────────────────────────────────────────
# Each returns a list of items in rss2json's shape: title, link,
# description (subtitle), content (HTML), pubDate, thumbnail, enclosure.

def fetch_items_rss2json(tags_out=None):
    print(f"  Source: {SUBSTACK_RSS}")
    resp = requests.get(RSS2JSON_URL, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    if data.get("status") != "ok":
        raise RuntimeError(f"rss2json status '{data.get('status')}': "
                           f"{data.get('message', 'unknown')}")
    return data.get("items", [])


def fetch_items_substack_api(tags_out=None, limit=12):
    """Build items from Substack's archive API plus one call per post.

    The archive listing has no post body, and its cover_image is the
    1200x630 social card, so each post is fetched for its full HTML, and the
    first image in the body (the 1500x500 hero) is used as the thumbnail,
    matching what rss2json returned.
    """
    resp = requests.get(f"{SUBSTACK_API}/archive",
                        params={"limit": limit}, timeout=30)
    resp.raise_for_status()
    items = []
    for post in resp.json():
        url = post.get("canonical_url", "")
        if post.get("type") == "podcast":
            # Mark voiceovers so main() skips them, as with the RSS feed
            items.append({"title": post.get("title", ""), "link": url,
                          "enclosure": {"type": "audio/mpeg"}})
            continue

        detail = requests.get(f"{SUBSTACK_API}/posts/{post['slug']}", timeout=30)
        detail.raise_for_status()
        detail = detail.json()
        body = detail.get("body_html") or ""

        hero = ""
        first_img = BeautifulSoup(body, "html.parser").find("img")
        if first_img and first_img.get("src"):
            hero = first_img["src"]
        hero = hero or detail.get("cover_image") or ""

        if tags_out is not None and detail.get("postTags"):
            tags_out[url] = [t["slug"] for t in detail["postTags"] if t.get("slug")]

        items.append({
            "title": detail.get("title", ""),
            "link": url,
            "description": detail.get("subtitle", ""),
            "content": body,
            "pubDate": detail.get("post_date", ""),
            "thumbnail": hero,
            "enclosure": {},
        })
    return items


# ── Duplicate Detection ─────────────────────────────────────────────

def get_existing_posts():
    """Parse front matter of all _posts/*.md and build lookup indices.

    Returns (substack_urls: set, normalized_titles: set).
    """
    substack_urls = set()
    normalized_titles = set()

    posts_path = Path(POSTS_DIR)
    if not posts_path.exists():
        return substack_urls, normalized_titles

    for filepath in posts_path.glob("*.md"):
        try:
            text = filepath.read_text(encoding="utf-8")
        except Exception:
            continue

        # Quick front-matter parse (between first two ---)
        if not text.startswith("---"):
            continue
        end = text.find("---", 3)
        if end == -1:
            continue
        front = text[3:end]

        for line in front.splitlines():
            line = line.strip()
            if line.startswith("title:"):
                raw_title = line[len("title:"):].strip().strip('"').strip("'")
                normalized_titles.add(normalize_title(raw_title))
            elif line.startswith("substack_url:"):
                url = line[len("substack_url:"):].strip().strip('"').strip("'")
                if url:
                    substack_urls.add(url)

    return substack_urls, normalized_titles


def is_duplicate(entry_title, entry_link, substack_urls, normalized_titles):
    """Check if an RSS entry already exists in _posts.

    Returns (is_dup: bool, reason: str).
    """
    # 1. Exact substack_url match
    if entry_link and entry_link in substack_urls:
        return True, f"substack_url match: {entry_link}"

    # 2. Normalized title match
    norm = normalize_title(entry_title)
    if norm in normalized_titles:
        return True, f"title match: '{norm}'"

    return False, ""


# ── HTML → Markdown Conversion ─────────────────────────────────────

def clean_html(raw_html):
    """Pre-process Substack HTML before markdown conversion.

    - Strips subscription widgets, paywall, share dialogs
    - Removes the first hero <figure> (handled separately)
    - Simplifies <picture> srcset to plain <img>
    """
    soup = BeautifulSoup(raw_html, "html.parser")

    # Remove Substack widgets
    for selector in [
        "div.subscription-widget-wrap",
        "div.paywall",
        "div.share-dialog",
        "div.subscribe-widget",
        "div.footer",
        "div.post-footer",
    ]:
        tag_name, _, class_name = selector.partition(".")
        for el in soup.find_all(tag_name, class_=class_name):
            el.decompose()

    # Remove first figure (hero image handled via enclosure)
    first_figure = soup.find("figure")
    if first_figure:
        first_figure.decompose()

    # Simplify <picture> → <img>
    for picture in soup.find_all("picture"):
        img = picture.find("img")
        if img:
            picture.replace_with(img)

    return str(soup)


def html_to_markdown(raw_html):
    """Convert Substack HTML content to clean Markdown."""
    cleaned = clean_html(raw_html)

    # Convert to markdown with ATX headings
    result = md(
        cleaned,
        heading_style="ATX",
        strip=["script", "style"],
    )

    # Post-process: collapse excessive blank lines
    result = re.sub(r"\n{4,}", "\n\n\n", result)
    # Remove trailing backslashes (markdownify line-break artifacts)
    result = re.sub(r"\\\s*$", "", result, flags=re.MULTILINE)
    # Strip Substack CTA lines
    result = re.sub(r"(?m)^Thanks for reading.*?Subscribe for free.*$\n?", "", result)
    # Trim trailing whitespace per line
    result = "\n".join(line.rstrip() for line in result.splitlines())
    return result.strip()


# ── Hero Image Download ────────────────────────────────────────────

def download_hero_image(item, slug):
    """Download hero image from rss2json item.

    Prefers the thumbnail (contains the 1500x500 hero via Substack CDN),
    extracting the original S3 URL when possible. Falls back to enclosure
    (which is typically the smaller 1200x630 social/OG image).
    """
    from urllib.parse import unquote as url_unquote
    image_url = None

    # Prefer thumbnail — contains the actual 1500x500 hero image
    thumb = item.get("thumbnail", "")
    if thumb and "substack-post-media.s3.amazonaws.com" in thumb:
        # Extract original S3 URL from CDN wrapper
        idx = thumb.find("https%3A%2F%2Fsubstack-post-media")
        if idx > 0:
            image_url = url_unquote(thumb[idx:])
        else:
            image_url = thumb
    elif thumb:
        image_url = thumb

    # Fallback: enclosure (typically 1200x630 social image)
    if not image_url:
        enclosure = item.get("enclosure", {})
        if isinstance(enclosure, dict) and enclosure.get("link"):
            image_url = enclosure["link"]

    if not image_url:
        print(f"  No hero image found for '{slug}'")
        return None

    # Determine extension from URL
    parsed = urlparse(image_url)
    path_ext = Path(parsed.path).suffix.lower()
    ext = path_ext if path_ext in (".png", ".jpg", ".jpeg", ".webp", ".gif") else ".png"

    image_filename = f"{slug}_hero_substack{ext}"
    image_path = os.path.join(IMAGES_DIR, image_filename)

    try:
        resp = requests.get(image_url, timeout=30)
        resp.raise_for_status()
        os.makedirs(IMAGES_DIR, exist_ok=True)
        with open(image_path, "wb") as f:
            f.write(resp.content)
        size_kb = len(resp.content) / 1024
        print(f"  Downloaded hero image: {image_path} ({size_kb:.0f} KB)")
        return image_path
    except Exception as e:
        print(f"  Failed to download hero image: {e}")
        return None


# ── Post File Generation ───────────────────────────────────────────

def create_post(item, pub_date, categories=None):
    """Create a Jekyll post file from an rss2json item.

    categories: list of tag slugs from Substack API, or None to
    fall back to ['substack-sync'].

    Returns dict with post metadata for the manifest.
    """
    title = item.get("title", "Untitled")
    slug = slugify(title)
    link = item.get("link", "")
    subtitle = item.get("description", "")
    # Clean subtitle: strip HTML if present
    if subtitle:
        subtitle = BeautifulSoup(subtitle, "html.parser").get_text().strip()
        # Truncate if excessively long
        if len(subtitle) > 250:
            subtitle = subtitle[:247] + "..."

    date_str = pub_date.strftime("%Y-%m-%d")
    filename = f"{date_str}-{slug}.md"
    filepath = os.path.join(POSTS_DIR, filename)

    # Get content (rss2json provides content as a plain string)
    raw_html = item.get("content", "")

    # Convert HTML → Markdown
    markdown_content = html_to_markdown(raw_html)

    # Extract first paragraph for description (if subtitle is short)
    description = subtitle
    if len(subtitle) < 80:
        # Subtitle is just a tagline; use first real paragraph instead
        for para in markdown_content.split("\n\n"):
            clean = para.strip().lstrip("#").strip()
            if len(clean) > 80 and not clean.startswith("*") and not clean.startswith("!"):
                description = clean
                if len(description) > 300:
                    # Keep whole sentences rather than cutting mid-word
                    ends = [m.end() for m in re.finditer(r"[.!?][\"”’]?(?=\s)", description[:300])]
                    description = description[:ends[-1]] if ends else description[:297] + "..."
                break

    # Download hero image
    image_path = download_hero_image(item, slug)
    image_ref = f"/{image_path}" if image_path else ""

    # Escape title for YAML (wrap in quotes, escape inner quotes)
    yaml_title = title.replace('"', '\\"')
    yaml_desc = description.replace('"', '\\"') if description else ""

    # Resolve categories: use Substack tags if available, else fallback
    cats = categories if categories else ["substack-sync"]

    # Build front matter matching existing post format
    lines = [
        "---",
        f'title: "{yaml_title}"',
        "layout: single",
        "author_profile: true",
        f"date: {date_str}",
        f"permalink: /blog/{slug}/",
        "categories:",
    ]
    for cat in cats:
        lines.append(f"  - {cat}")
    lines += [
        f'description: "{yaml_desc}"',
        f'substack_url: "{link}"',
    ]
    if image_ref:
        lines.append(f"image: {image_ref}")
    lines.append("---")
    lines.append("")

    # Hero image in content
    if image_ref:
        lines.append(f"![{title}]({image_ref})")
        lines.append("")

    # Subtitle heading (matching existing post format)
    if subtitle:
        lines.append(f"### {subtitle}")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Main content
    lines.append(markdown_content)
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*Originally published on [Substack]({link}).*")
    lines.append("")

    post_content = "\n".join(lines)

    os.makedirs(POSTS_DIR, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(post_content)

    print(f"  Created post: {filepath}")

    return {
        "title": title,
        "slug": slug,
        "date": date_str,
        "filename": filename,
        "filepath": filepath,
        "image_path": image_path,
    }


# ── Main ───────────────────────────────────────────────────────────

def main():
    dry_run = os.environ.get("DRY_RUN", "false").lower() == "true"
    if dry_run:
        print("=== DRY RUN MODE ===\n")

    # Tags the Substack API path picks up for free, keyed by post URL
    prefetched_tags = {}

    items = None
    for name, fetch in [("rss2json proxy", fetch_items_rss2json),
                        ("Substack API", fetch_items_substack_api)]:
        print(f"Fetching feed via {name}...")
        try:
            items = fetch(tags_out=prefetched_tags)
        except Exception as e:
            print(f"  FAILED: {e}\n")
            continue
        if items:
            break
        print("  FAILED: returned 0 items\n")

    if not items:
        print("ERROR: Every feed source failed. Aborting.")
        sys.exit(1)

    print(f"Found {len(items)} entries in feed\n")

    substack_urls, normalized_titles = get_existing_posts()
    print(f"Existing posts indexed: {len(normalized_titles)} titles, "
          f"{len(substack_urls)} substack URLs\n")

    # Fetch tags from Substack archive API (not behind Cloudflare)
    tags_by_url = prefetched_tags or fetch_substack_tags(limit=20)

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=DELAY_DAYS)

    new_posts = []
    skipped_recent = []
    skipped_dup = []
    skipped_podcast = []

    for item in items:
        title = item.get("title", "Untitled")
        link = item.get("link", "")

        # Skip podcast/audio items (whitepaper voiceovers). These live
        # in the Substack "Whitepapers - The Working Source Documents"
        # section and are pushed to Apple Podcasts; the written
        # whitepapers under /papers/ are canonical on the site.
        enclosure = item.get("enclosure", {})
        enc_type = enclosure.get("type", "") if isinstance(enclosure, dict) else ""
        if enc_type.startswith("audio/"):
            print(f"SKIP '{title}': podcast/audio item (whitepaper voiceover)")
            skipped_podcast.append(title)
            continue

        # Parse publish date (rss2json format: "YYYY-MM-DD HH:MM:SS")
        pub_date = None
        pub_str = item.get("pubDate", "")
        if pub_str:
            pub_date = date_parser.parse(pub_str)
            if pub_date.tzinfo is None:
                pub_date = pub_date.replace(tzinfo=timezone.utc)

        if not pub_date:
            print(f"SKIP '{title}': no publish date")
            continue

        # Check 7-day delay
        if pub_date > cutoff:
            days_remaining = (pub_date - cutoff).days + 1
            print(f"SKIP '{title}': only {days_remaining} day(s) old "
                  f"(published {pub_date.strftime('%Y-%m-%d')})")
            skipped_recent.append(title)
            continue

        # Check duplicates
        dup, reason = is_duplicate(title, link, substack_urls, normalized_titles)
        if dup:
            print(f"SKIP '{title}': duplicate ({reason})")
            skipped_dup.append(title)
            continue

        # New post
        print(f"NEW  '{title}' (published {pub_date.strftime('%Y-%m-%d')})")

        # Look up tags for this post by its Substack URL
        post_categories = tags_by_url.get(link, None)
        if post_categories:
            print(f"  Tags from Substack: {', '.join(post_categories)}")
        else:
            print(f"  No tags found — will use 'substack-sync'")

        if dry_run:
            print("  [dry run] Would create post and PR")
            new_posts.append({
                "title": title,
                "slug": slugify(title),
                "date": pub_date.strftime("%Y-%m-%d"),
                "filename": f"{pub_date.strftime('%Y-%m-%d')}-{slugify(title)}.md",
                "filepath": None,
                "image_path": None,
            })
        else:
            post_info = create_post(item, pub_date, categories=post_categories)
            new_posts.append(post_info)

    # Summary
    print(f"\n{'='*50}")
    print(f"Summary: {len(new_posts)} new, "
          f"{len(skipped_dup)} duplicates, "
          f"{len(skipped_recent)} too recent, "
          f"{len(skipped_podcast)} podcast/audio")

    if new_posts:
        print("\nNew posts:")
        for p in new_posts:
            print(f"  - {p['title']} ({p['date']})")

    # Write manifest for the PR creation step
    with open(MANIFEST_PATH, "w") as f:
        json.dump(new_posts, f, indent=2)
    print(f"\nManifest written to {MANIFEST_PATH}")


if __name__ == "__main__":
    main()

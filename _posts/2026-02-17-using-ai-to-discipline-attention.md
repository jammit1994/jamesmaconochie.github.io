---
title: "Using AI to Discipline Attention"
layout: single
author_profile: true
date: 2026-02-17
permalink: /blog/using-ai-to-discipline-attention/
categories:
  - substack-sync
description: "Last week, I admitted I’m part of the problem. Despite advocating restraint, I’ve felt the pull to post more, feed the algorithm, and add to the noise. We’re all drowning in a flood we helped create."
substack_url: "https://jamesmaconochie.substack.com/p/using-ai-to-discipline-attention"
image: /assets/images/using-ai-to-discipline-attention_hero_substack.png
---

![Using AI to Discipline Attention](/assets/images/using-ai-to-discipline-attention_hero_substack.png)

### Fighting Fire with Fire, Carefully

---

Last week, I admitted I’m part of the problem. Despite advocating restraint, I’ve felt the pull to post more, feed the algorithm, and add to the noise. We’re all drowning in a flood we helped create.

I ended with a question: Could the same tools flooding us with content also help us navigate it?


This post is my answer.

### The Needle and the Haystack

We live in a world of infinite language.

No human can process it all, nor should they. Most of it is, at best, meaningless to any individual. At worst, it’s noise, pollution, or manipulation clogging the channels where meaning once flowed.

I talk about disciplining attention by being deliberate. But it’s hard. Every day, the same question: In this endless sea of language, where should I focus? How do I find the needles in the haystack?

For months, I scrolled and skimmed, hoping algorithms would surface something worthwhile. Occasionally, they did. Mostly, they didn’t.

Then I realized: I was asking the wrong question.

### What LLMs Are Actually Good At

I’ve argued that LLMs won’t achieve AGI. They don’t reason like humans. They don’t truly understand.

But here’s what they are good at: processing language. Pattern matching. Summarizing. Filtering. Categorizing.

These aren’t the glamorous capabilities that dominate AI headlines. No one writes breathless articles about “AI that sorts your reading list.” But for the problem I faced (too much language, too little attention), these are exactly the tools I needed.

This is the AHI thesis in practice: use AI to extend human capabilities, not replace human judgment. Let the machine do what machines do well (process volume) so the human can do what humans do well (decide what matters).

### Building a Filter, Not a Firehose

Here’s what I did.

I wanted to engage with writers whose work intersects with mine: AI, attention, cognition, architecture. But finding them manually, keeping up with their output, and identifying meaningful conversations: that was a full-time job.

So I built a simple system. Nothing fancy, but deliberate.

First, I curated a list of authors. Not everyone writing about AI, only those whose thinking genuinely aligns with mine, whose audiences might value my perspective. This required human judgment. No algorithm could tell me who I respect.

Second, I built a corpus of my own work. My Substack posts, whitepapers, and core ideas. This corpus gave the system a reference point: What does my thinking sound like? What themes do I care about?

Third, I created a scoring mechanism. When a new post from someone on my list appears, the system evaluates its relevance to my corpus. How much overlap? How timely? The output isn’t a binary “read or skip.” It’s a score from 0 to 100, with a ‘worth-a-look’ threshold currently set at 90 or higher: any article that reaches or exceeds it is identified as a potential engagement opportunity and therefore worthy of review and potentially posting a comment.

The system doesn’t tell me what to think. It doesn’t write my responses (although it can certainly offer potential starting points - more on this later). It just filters the infinite down to the manageable so that I can do the actual intellectual work.

I’m using the very thing that caused the flood to build a personal lifeboat.

And that’s precisely the point.

### How I Built My Filter (A Practical Pattern)

If you’re curious about the mechanics, not as a prescription, but as a pattern, here are the steps I followed:

**Define your “needle.”** I started by clarifying what I was actually looking for: writers exploring the intersection of AI, cognition, and meaning. Not “everything about AI,” but my slice of it. Your needle will be different.

**Gather your own voice.** I fed my system a corpus of my own writing: Substack posts, white papers, notes, and key ideas. This corpus provided a reference point for relevance: “Find things that resonate with this.” Your corpus is your intellectual fingerprint.

**Curate, don’t collect.** I handpicked a starter list of thinkers whose work I genuinely respect. No algorithms. The starter list is a human gate, built once, then scaled. Your list should feel like a dinner party invitation list, not a block party.

**Score for signal, not popularity.** My system ranks new content by thematic overlap, not engagement metrics. It asks: “How much does this align with what you care about?” Your scoring should reflect your priorities, not the platform’s.

**Build an interface you’ll actually use.** Raw output from a script isn’t enough. I built a simple web interface to review, sort, and manage the authors list, the scoring results, and record actual engagements (comments that I post). If you can’t easily see and interact with the insights, you won’t use the system. Make it visible. Make it yours.

**Preserve the human moment.** The output isn’t a command. It’s a filtered feed. I still choose what to read, how to engage, and whether to respond. Your judgment stays in the loop.

**Iterate relentlessly.** My first pass wasn’t right. I’ve refined my author list, adjusted my scoring weights, and improved the user interface as I learned what I actually needed. The system that I have built isn’t a finished product. It’s a living system that evolves as my thinking does. Your filter should grow with you.

The tools are simple: RSS feeds, a language model API, a basic script, and a lightweight web app. The philosophy is what matters: AI as a lens, not a source.

### The Discipline Still Required

Here’s what AI can’t do for me:

It can’t decide what I actually care about. It can’t distinguish deep insight from clickbait in intellectual clothing. It can’t write a thoughtful response that truly reflects my voice, my personal experience, and my ever-evolving point of view. It can’t build real relationships with other thinkers.

All of that remains mine.

What AI can do is reduce the search cost. It helps me spend less time looking and more time thinking. It’s a filter, not a replacement for judgment.

It can suggest potential starting points for me to consider, or more often than not, not consider. My process is:

1. Read the articles that exceed my scoring threshold (90/100)
2. Make my own notes about the thoughts that the article evokes in me, and parallels to the work that I have produced previously
3. View any system-generated starting points, and consider how, if at all, they might echo my personal gut reactions
4. Work to develop a final comment that considers all inputs, while ensuring the article is my work product and that I reference my own point of view and personal experience (just as I am doing right here).
5. My experience has been that more than 85% of the time, my own notes are the only input to the final comment. This is critical for me, as my corpus update process incorporates all of my comments as well as new articles and whitepapers written since the last update. I have also observed occasional hallucinations in the ‘target passage’ identification part of the system generated suggested starting points.

This process is constraint-awareness applied to tools: knowing what to delegate and what to keep. Using AI to extend attention, not abdicate it.

### An Invitation to Experiment

I haven’t solved the attention crisis. I’ve built one small tool for one specific problem. It helps me. It might not help you.

But the principle generalizes.

If you’re drowning in content, ask yourself: What’s my needle? What’s my haystack? What would it look like to use AI as a filter rather than a generator? Where could pattern-matching reclaim time for deeper thinking?

The flood won’t stop. The language will keep coming. But we’re not helpless. The same technologies that are accelerating the crisis might, if used carefully, help us navigate it.

Not by processing more, but by attending better.

*This is the fifth essay in my series on language, attention, and the architecture of shared meaning.* *Previous posts: [[Part I: The Constraints We Lost]](https://jamesmaconochie.substack.com/p/the-architecture-of-language-part?r=5270g6) • [[Part II: Serviceability Failure]](https://jamesmaconochie.substack.com/p/the-architecture-of-language-part-241?r=5270g6) • [[Part III: Wisdom in an Infinite-Language World]](https://jamesmaconochie.substack.com/p/the-architecture-of-language-part-fd6?r=5270g6) • [[Part IV: We Are the Problem]](https://jamesmaconochie.substack.com/p/we-are-a-part-of-the-problem?r=5270g6)*

*Next week in ‘More Instruments, Same Song’ I will summarize the growing number of respected AI experts that question the ‘Bigger is Better’ mantra for models, compare my critiques to these experts’, and share our observations about what might drive the next breakthroughs in the field of AI.*

---

*Originally published on [Substack](https://jamesmaconochie.substack.com/p/using-ai-to-discipline-attention).*

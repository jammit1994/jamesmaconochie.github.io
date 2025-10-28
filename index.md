---
layout: splash
title: "Exploring the Edge of Human and Artificial Intelligence"
permalink: /
header:
  overlay_image: /assets/images/sunrise_over_boston_thin.jpg
  overlay_color: "#000000"   # ensures the filter is applied over black, not theme default
  overlay_filter: 0.15       # lower = brighter image (try 0.15–0.22)
  caption: "Sunrise over the Charles River between Cambridge and Boston"
  actions:
    - label: "Read the Papers"
      url: /papers/
      class: "btn--primary"
    - label: "About James"
      url: /about/
excerpt: "<br><br><br><br>Working papers and frameworks on architecture, attention, and the pursuit of wisdom in machine intelligence."
---

<style>
/* keep your shallower hero */
.page__hero--overlay {
  min-height: 48vh !important;
  height: auto !important;
  background-position: center 35% !important;
  background-size: cover !important;
  padding-top: 0 !important;        /* no extra space above the title */
  padding-bottom: 1.75rem !important;
}

/* 1) Move the SUBTITLE (excerpt) down RELATIVE TO THE TITLE */
.page__hero--overlay h1 + p                 { margin-top: 3rem !important; }
.page__hero--overlay [class*="page__title"] + p { margin-top: 3rem !important; }  /* fallback if title has a class */
.page__hero--overlay .page__lead            { margin-top: 3rem !important; }      /* fallback if excerpt has this class */

/* 2) Move the BUTTON BLOCK down (the element immediately after the excerpt) */
.page__hero--overlay h1 + p + *                 { margin-top: 2rem !important; }
.page__hero--overlay [class*="page__title"] + p + * { margin-top: 2rem !important; }

/* If the theme wraps buttons differently, also nudge common containers */
.page__hero--overlay .page__actions,
.page__hero--overlay .btn-group,
.page__hero--overlay .btn { margin-top: 2rem !important; }

/* mobile: a touch taller for readability */
@media (max-width: 768px) {
  .page__hero--overlay { min-height: 52vh !important; background-position: center 40% !important; }
  .page__hero--overlay h1 + p,
  .page__hero--overlay [class*="page__title"] + p,
  .page__hero--overlay .page__lead { margin-top: 2.25rem !important; }
  .page__hero--overlay h1 + p + *,
  .page__hero--overlay [class*="page__title"] + p + * { margin-top: 1.5rem !important; }
}
</style>

Welcome! I build and write about modular, biologically inspired approaches to AI—how systems learn, adapt, and coordinate, and how human attention and meaning should guide what we build. These working papers are living documents: clear enough for practitioners, grounded enough for researchers, and open to revision as the field evolves.

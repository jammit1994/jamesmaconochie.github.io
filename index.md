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
/* Shallower hero that still expands to fit its content */
.page__hero--overlay {
  min-height: 48vh !important;          /* target height */
  height: auto !important;               /* allow growth for buttons */
  background-position: center 35% !important;
  background-size: cover !important;
  padding-top: 1.75rem !important;
  padding-bottom: 1.75rem !important;
}

/* remove the earlier ::before hack; let theme handle it normally */
.page__hero--overlay::before {
  height: auto !important;
  padding-top: 0 !important;
}

/* keep subtitle lower relative to title */
.page__hero .page__lead {
  margin-top: 2.5rem !important;
}

/* optional: nudge the whole block a touch */
.page__hero--overlay .wrapper {
  padding-top: 0.5rem !important;       /* increase to push lower */
  padding-bottom: 0.5rem !important;
}

/* mobile: a bit taller for readability */
@media (max-width: 768px) {
  .page__hero--overlay {
    min-height: 52vh !important;
    background-position: center 40% !important;
  }
}
</style>

Welcome! I build and write about modular, biologically inspired approaches to AI—how systems learn, adapt, and coordinate, and how human attention and meaning should guide what we build. These working papers are living documents: clear enough for practitioners, grounded enough for researchers, and open to revision as the field evolves.

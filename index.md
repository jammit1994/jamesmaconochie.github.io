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
excerpt: "Working papers and frameworks on architecture, attention, and the pursuit of wisdom in machine intelligence."
---

<style>
/* Keep your shallower hero as before */
.page__hero--overlay {
  min-height: 48vh !important;
  height: auto !important;
  background-position: center 35% !important;
  background-size: cover !important;
  padding-top: 1.75rem !important;
  padding-bottom: 1.75rem !important;
}

/* 🎯 Move the subtitle down relative to the title */
.page__hero--overlay .page__lead {
  margin-top: 9rem !important;      /* increase to push subtitle lower */
  margin-bottom: 2rem !important;   /* adds some space before buttons */
}

/* 🎯 Move the Read the Papers / About James buttons down as a group */
.page__hero--overlay .page__actions {
  margin-top: 1.5rem !important;    /* increase if you want more separation */
}

/* Ensure the buttons stay vertically inside the hero */
.page__hero--overlay .page__actions .btn {
  position: relative !important;
  top: 0 !important;
}

/* Mobile adjustments for readability */
@media (max-width: 768px) {
  .page__hero--overlay {
    min-height: 52vh !important;
    background-position: center 40% !important;
  }
  .page__hero--overlay .page__lead { margin-top: 2rem !important; }
}
</style>

Welcome! I build and write about modular, biologically inspired approaches to AI—how systems learn, adapt, and coordinate, and how human attention and meaning should guide what we build. These working papers are living documents: clear enough for practitioners, grounded enough for researchers, and open to revision as the field evolves.

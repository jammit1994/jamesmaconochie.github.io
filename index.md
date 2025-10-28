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
excerpt: "<br><br><br>Working papers and frameworks on architecture, attention, and the pursuit of wisdom in machine intelligence."
---

<style>
/* Force a shallower hero and control the crop, even if the theme uses a pseudo-element */
.page__hero--overlay {
  height: 44vh !important;         /* explicit height */
  min-height: 0 !important;        /* neutralize theme min-height */
  background-position: center 35% !important;  /* adjust framing */
  background-size: cover !important;
  padding-top: 0 !important;       /* remove theme's vertical padding */
  padding-bottom: 0 !important;
}

/* If the theme sets height via a pseudo-element, neutralize it */
.page__hero--overlay::before {
  height: 100% !important;
  padding-top: 0 !important;       /* some themes use padding-top to set hero height */
}

/* Shift the whole text block lower inside the shallower hero */
.page__hero--overlay .wrapper {
  padding-top: 2rem !important;
  padding-bottom: 1.5rem !important;
}

/* Push the subtitle down relative to the title */
.page__hero .page__lead {
  margin-top: 2.5rem !important;
}

/* Mobile: slightly taller for readability */
@media (max-width: 768px) {
  .page__hero--overlay {
    height: 45vh !important;
    background-position: center 40% !important;
  }
}
</style>

Welcome! I build and write about modular, biologically inspired approaches to AI—how systems learn, adapt, and coordinate, and how human attention and meaning should guide what we build. These working papers are living documents: clear enough for practitioners, grounded enough for researchers, and open to revision as the field evolves.

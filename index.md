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
excerpt: "<br><br><br><br><br><br><br>Working papers and frameworks on architecture, attention, and the pursuit of wisdom in machine intelligence."
---

<style>
/* TEMP: force hero height + positioning with very broad selectors */
.page__hero,
.page__hero--overlay,
.page__hero--image,
section.page__hero,
section.page__hero--overlay {
  min-height: 38vh !important;        /* make it shallower (try 34–45) */
  padding-top: 1.5rem !important;
  padding-bottom: 1.5rem !important;
  background-position: center 35% !important; /* adjust crop: 25% (higher), 55% (lower) */
  background-size: cover !important;
  background-repeat: no-repeat !important;
}

/* shift the whole text block down slightly */
.page__hero .wrapper,
.page__hero--overlay .wrapper {
  padding-top: 2rem !important;        /* increase to push text lower as a group */
}

/* push the subtitle (excerpt) down relative to the title */
.page__hero .page__lead {
  margin-top: 2.5rem !important;       /* increase to move it further down */
}

/* add a visible test outline so we KNOW the rule applied; remove later */
.page__hero--overlay { outline: 3px dashed rgba(0,0,0,.25) !important; }

/* mobile: a bit taller for readability */
@media (max-width: 768px) {
  .page__hero,
  .page__hero--overlay,
  .page__hero--image,
  section.page__hero,
  section.page__hero--overlay {
    min-height: 45vh !important;
    background-position: center 40% !important;
  }
}
</style>

Welcome! I build and write about modular, biologically inspired approaches to AI—how systems learn, adapt, and coordinate, and how human attention and meaning should guide what we build. These working papers are living documents: clear enough for practitioners, grounded enough for researchers, and open to revision as the field evolves.

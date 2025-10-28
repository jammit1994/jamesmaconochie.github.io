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
/* Shallower hero that expands to fit content */
.page__hero--overlay {
  min-height: 48vh !important;
  height: auto !important;
  background-position: center 35% !important;
  background-size: cover !important;
  padding-top: 0 !important;      /* we'll add spacing with a spacer below */
  padding-bottom: 1.75rem !important;
}

/* 🚀 Add a spacer at the top of the hero content to push everything down */
.page__hero--overlay .wrapper::before {
  content: "";
  display: block;
  height: 3rem;                   /* increase to push lower (e.g., 4rem, 5rem) */
}

/* Subtitle (excerpt) still can have some extra space if desired */
.page__hero .page__lead {
  margin-top: 1.5rem !important;  /* fine-tune local gap under the title */
}

/* Button row spacing under subtitle (optional extra nudge) */
.page__hero .page__meta,
.page__hero .page__actions {
  margin-top: 1.5rem !important;
}

/* Mobile: a bit taller for readability */
@media (max-width: 768px) {
  .page__hero--overlay {
    min-height: 52vh !important;
    background-position: center 40% !important;
  }
  .page__hero--overlay .wrapper::before {
    height: 2.25rem;              /* smaller spacer on phones */
  }
}
</style>

Welcome! I build and write about modular, biologically inspired approaches to AI—how systems learn, adapt, and coordinate, and how human attention and meaning should guide what we build. These working papers are living documents: clear enough for practitioners, grounded enough for researchers, and open to revision as the field evolves.

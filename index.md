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
  min-height: 40vh !important;
  height: auto !important;
  background-position: center 35% !important;
  background-size: cover !important;
  padding-top: 1.75rem !important;
  padding-bottom: 0rem !important;
}

/* 🎯 Move the subtitle down relative to the title */
.page__hero--overlay .page__lead {
  margin-top: 16rem !important;      /* increase to push subtitle lower */
  margin-bottom: 0rem !important;   /* adds some space before buttons */
}

/* 🎯 Move the Read the Papers / About James buttons down as a group */
.page__hero--overlay .page__actions {
  margin-top: 0rem !important;    /* increase if you want more separation */
}

/* Ensure the buttons stay vertically inside the hero */
.page__hero--overlay .page__actions .btn {
  position: relative !important;
  top: 0 !important;
}

/* ✅ Tablet & Mobile overrides */
@media (max-width: 992px) {
  .page__hero--overlay {
    min-height: 50vh !important;              /* a bit taller for mobile */
    background-position: center 40% !important;
    padding-top: 0.5rem !important;           /* small breathing space above */
    padding-bottom: 2rem !important;
  }
  .page__hero--overlay .page__lead {
    margin-top: 10rem !important;           /* maintain visible gap under title */
    margin-bottom: 0rem !important;
  }
  .page__hero--overlay .page__actions {
    margin-top: 2.25rem !important;           /* keep buttons separated */
  }
}

/* ✅ Very small screens (e.g., phones <600px) */
@media (max-width: 600px) {
  .page__hero--overlay {
    min-height: 55vh !important;              /* ensure room for all text */
    background-position: center 45% !important;
  }
  .page__hero--overlay .page__lead {
    margin-top: 10rem !important;
  }
}
</style>

Welcome! I build and write about modular, biologically inspired approaches to AI—how systems learn, adapt, and coordinate, and how human attention and meaning should guide what we build. These working papers are living documents: clear enough for practitioners, grounded enough for researchers, and open to revision as the field evolves.

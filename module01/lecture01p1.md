---
title: Lecture 1.1 - Introduction to this Workshop
layout: lecture
tags:
  - overview
  - introduction
description: >-
  Overview of workshop and info about your instructor.
date: 2026-12-02
---

<br><br><br>
# Welcome to this Web Viz Workshop!

notes:
just a few items before we get into the workshop as far as bureaucratic items and a bit about me!

---

## How to access the workshop website/slides

Workshop webpage: [COURSE_WEBPAGE/](COURSE_WEBPAGE/)

notes:
**make sure this is accessible on the web!**

---

## How to translate these slides

[Google Translate for Webpages](https://translate.google.com/?sl=auto&tl=en&op=websites)

notes:

So you all might be more adept at doing this than I, but a few pointers just in case!

**put in the URL for these slides, starting from main webpage**

**show that if you click on slides, some of the formatting is gone and you might need to play with the zoom**

**check in with folks**

---

## The course webpage

[The syllabus](COURSE_WEBPAGE/syllabus) covers more than we'll probably get to!

notes:
**go over this**

**highlight**:
1. where more reading is
2. where videos are -- if folks want to look over these materials again (and more!)

---

## The course webpage

[The syllabus](COURSE_WEBPAGE/syllabus) covers more than we'll probably get to!

Each Module on the [main course webpage](COURSE_WEBPAGE/) contains lecture slides, links to resources and data, notebooks, and "starter files" you can copy into your own website or app.

notes:
**go over this too**

**highlight:**
1. lecture slides
2. resources/data
3. notebooks (view on the site, or open in Colab) and starter files (Modules 3 & 4)

**pause for questions**

---

### My background

---

### My background

<img src="images/intro_naiman1.png" alt="Simulation rendering of the cosmic web from the Illustris project: glowing orange gas clusters connected by a network of blue filaments." width="800"/>

---

### My background

<img src="images/intro_naiman2.png" alt="The same Illustris cosmic web rendering with the word 'SCIENCE!' overlaid." width="800"/>

---

### My background

<img src="images/intro_naiman3.png" alt="The Illustris rendering annotated: blue 'Dark matter filaments (most of the matter in the Universe)' and bright 'Concentrations where gas collects and forms galaxies'; a scale bar reads about 3 x 10^18 meters." width="800"/>

---

### My background

<img src="images/intro_naiman4.png" alt="The Illustris rendering with three zoomed-in insets showing individual simulated galaxies, two spirals and one elliptical, inside the cosmic web." width="800"/>

---

### My background
#### ytini.com

<img src="images/intro_naiman5.png" alt="Diagram of volume rendering: a camera looks through an image plane into a 3D grid of blue simulation data, with an opacity map and color map that control how data values become pixels." height="400"/>

Naiman et al. 2017, Borkiewicz et al. 2018

---

### My background
#### ytini.com

<img src="images/intro_naiman6.png" alt="Comparison of a 'Simple' and a 'Complex' transfer function: a linear opacity map and grayscale color map give a gray rendering, while a multi-peaked opacity map and multi-color map give a detailed orange-and-purple rendering." height="400"/>

Naiman et al. 2017, Borkiewicz et al. 2018

---

### My background
#### ytini.com

<img src="images/intro_naiman7.png" alt="Cinematic rendering of a cosmological simulation with glowing gas bubbles and blue filaments, made by AVL/NCSA at the University of Illinois with data from Brian O'Shea, Michigan State." height="400"/>

Naiman et al. 2017, Borkiewicz et al. 2018

---

### My background
#### ytini.com

<img src="images/intro_naiman8.png" alt="Two scientific visualizations from the CADENS project (cadens.ncsa.illinois.edu): the Sun with looping blue magnetic field lines, and the solar wind streaming past a planet." height="400"/>

Naiman et al. 2017, Borkiewicz et al. 2018

---

### My background
#### Scientific Digitization

<img src="https://www.astronaiman.com/assets/img/digitization_project/figure_axis_reading_sm-1400.webp" height="500" alt="Image showing optical character recognition (OCR) applied to a technical image of the sky with declination (y) and right ascension (x) axis.  The raw OCR is processed into metadata to be added to the original image to give its location in the sky." />

Naiman et al. 2022, TPDL conference

notes:
also do some science digitization, i.e. trying to turn scans of old scientific figures back into data by having computers "read" objects and axis labels using image processing, optical character recognition and machine learning methods

---

## The plan for today

| Module | What we'll do |
|---|---|
| 1 | Set up: accounts, Google Colab, and your github.io website |
| 2 | Data viz basics: what makes a good (or bad) viz |
| 3 | Interactive plots with **Altair** → on your **Jekyll** website |
| 4 | Interactive **Streamlit** apps → on **Streamlit Community Cloud** |
| 5 | Putting it together & where to go from here |
| 6 | *(Optional, on your own)* installing everything on your computer |

notes:
a lot of this comes from the IS445 Data Visualization course (weeks on Altair, Jekyll and Streamlit) -- squished into one workshop!

modules 1-3 are one complete "tool" (a website with interactive plots), module 4 is a second complete tool (an app) -- so if we run short on time, you still leave with a finished website

everything today is in the browser; module 6 is there for later if you want to work on your own computer

---

## Double check: setup going ok?

notes:
hopefully folks got Lecture 1.0 done (or started) -- quick check in: GitHub account? Colab test notebook ran?

next up: putting the website template on your github.io site

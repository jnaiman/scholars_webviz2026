---
title: Lecture 2.1 - Good & Bad Visualization Design
layout: lecture
tags:
  - data viz
  - concepts
  - overview
description: >-
  Design choices when making visualizations.
date: 2025-10-09
---

<br><br/> <br><br/> <br/>

# Designing a Good Viz

notes:

How do we design a good viz?  Will go through some "best practices", but be warned it will also take a bit of practice.

How to make a good viz:
1. Part 1: choosing your viz
  * mini perception channels
  * data -- viz, types of viz
  * include "types of viz image"
  * look at types of viz webpage

2. Part 2: designing your viz
  * some of tufte
  * go through caveats webpage

---

<br/><br/><br/>
# Designing a Good Viz: Part 1
## Perception Channels & Types of Plots

notes:
first, let's understand how humans actually translate different kinds of visuals into knowledge about the data being presented and how that relates to different kinds of plots or charts

---

## Perception Channels

<style>
  br {
   display: block;
   margin: 0px 0;
   margin-top: 0px;
   content: " ";
   line-height:1px;
}

</style>

<table>
<tr>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_closure.gif" alt="Field of open C-shaped rings with one closed circle among them."/><br>Closure</td>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_hue.gif" alt="Field of short blue dashes with one red dash among them."/><br>Color</td>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_size.gif" alt="Field of short blue dashes with one larger dash among them."/><br>Size</td>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_den.gif" alt="Field of short blue dashes with one region where the dashes are packed more densely."/><br>Density</td>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_curve.gif" alt="Field of straight blue dashes with one curved dash among them."/><br>Curvature</td>
</tr>
<tr>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_lum.gif" alt="Field of blue dashes with one lighter, brighter blue dash among them."/><br>Intensity</td>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_orient.gif" alt="Field of horizontal blue dashes with one tilted dash among them."/><br>Orientation</td>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_3d_depth.gif" alt="Field of shaded 3D spheres with one sphere that appears to sit at a different depth from the rest."/><br>Depth Cues</td>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_isect.gif" alt="Field of L-shaped marks with one plus sign (two intersecting lines) among them."/><br>Intersection</td>
<td><img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/tg_term.gif" alt="Field of L-shaped marks with one T-shaped mark, whose line ends differ, among them."/><br>Terminators</td>
</tr>
</table>

Check out [csc2.ncsu.edu/faculty/healey/PP](https://www.csc2.ncsu.edu/faculty/healey/PP) for more examples and research.

notes:

so in my data viz class we take a week or 2 to cover this so we'll only do a brief overview, but at a very basic level -- there are different kinds of "channels" through which humans can perceive representations of data

some of these channels are more/less effective at conveying information -- which of these "pop out" the most to you?

---

## Preattentive Processing

Which image has the red dot?


<div class="left">
  <img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/colour_A.gif" alt="Field of blue dots, all the same color, with no red dot.">
</div>

<div class="right">
 <img src="https://www.csc2.ncsu.edu/faculty/healey/PP/figs/colour_P.gif" alt="Field of blue dots with a single red dot that stands out immediately.">
</div>

Check out [csc2.ncsu.edu/faculty/healey/PP](https://www.csc2.ncsu.edu/faculty/healey/PP) for more examples and research.


notes:
there are several very powerful perception channels like color which is a "preattentive attribute" -- this means that our brain can sense changes in color before we have to actively focus on an image

this is why you probably immediately saw which of these images had a red dot in it

---

## Strength of Perception Channels


<img src="images/perception_channels/stevensLaw.png" alt="Stevens' psychophysical power law plot of perceived sensation versus physical intensity: electric shock (exponent 3.5) and saturation (1.7) curve upward, length (1) is a straight line, and area (0.7), depth (0.67) and brightness (0.5) curve downward. From Tamara Munzner, data from Stevens.">

notes:
different perception channels map more or less "truthfully" to data -- a fun example is shown here

for example we can see that there is about a 1-to-1 correspondence between the physical length of an object and our perceived length of the object

while for something like area our perception is much less sensitive

this is why something like a bar chart is typically a better way to communicate with data than a pie chart

also, don't try to visualize data with electric shocks please! :D


---

## Perception Channels to Data Encodings

<img src="images/perception_channels/vad_slides_p51.png" alt="Munzner's channel rankings. Magnitude channels for ordered attributes, from most to least effective: position on common scale, position on unaligned scale, length, tilt/angle, area, depth, color luminance, color saturation, curvature, volume. Identity channels for categorical attributes: spatial region, color hue, motion, shape.">

notes:
we can map the effectiveness of different perception channels roughly to the kinds of marks we want to make for different kinds of data

for example, for ordered data like quantitative or ordered categorical something like position on a common scale (i.e. a bar chart) is at the top, 

while something like volume (i.e. a 3D chart) is on the bottom

---

## What kinds of plots should we use with what kinds of data?

notes:
so, the natural next question would probably be, what kinds of precise plots should we use with a particular kind of data?  like a set of time varying points or a bunch of categorical variables?

---

## What kinds of plots should we use with what kinds of data?

<img src="images/types_of_charts/charts_types.jpg" width="30%" alt="Hand-drawn infographic 'Nuts and Bolts of Chart Types' from online-behavior.com, with sketches and joke captions for 12 charts including histogram, bar, pie, line, area, bubble, radar, waterfall, tree map, scatterplot and box plot.">

Source: [online-behavior.com](https://online-behavior.com/analytics/chart-types/)

notes:
the short answer, is it depends but you'll definitely find suggestions from various folks out there

for example, this is a pretty silly chart...

---

## What kinds of plots should we use with what kinds of data?


<img src="images/types_of_charts/pie_chart.png" alt="Hand-drawn pie chart with the caption 'Extremely useful when creating a well designed document that is intended to people that will not read the data (e.g. management)'.">

Caption: Extremely useful when creating a well designed document that is intended to people that will not read the data (e.g. management)



notes:
for example, it suggests that pie charts are good for management since that is a chart they are used to seeing...

---

## What kinds of plots should we use with what kinds of data?

<img src="images/types_of_charts/histogram.png" alt="Hand-drawn histogram with the caption 'Chart used by responsible analysts who understand the power of segmentation and the sadness that comes from aggregating data'.">

Caption: Chart used by responsible analysts who understand the power of segmentation and the sadness that comes from aggregating data.

notes:
and suggests something like a histogram/barchart is for use by very serious analysts :D

---

## What kinds of plots should we use with what kinds of data?

Under "Syllabus" or "Module 2" on Course webpage.

<img src="images/viz_resources.png" style='border:1px solid #000000' alt="The Module 2 row of the syllabus table with the links '2. The Data Viz Picker' and '3. Data Viz Caveats' outlined in red.">

notes:
while you can find such snarky advice all over the internet, it might be useful for us to have a somewhat structured way to figure out what kind of plot to consider playing with with what kind of data

some resources for this are linked under Module 2 on the workshop website (and on the syllabus)...

---

<embed src="https://www.data-to-viz.com/#spider" style="width:100%; height:80vh">

notes:
the first one is the "Visualization Picker"

hit "Explore" to see some suggestions for what kinds of visualizations we should use with what kinds of data

**go through the 1 column of numerical data**

**then have students select numeric, categorical, etc and then select other options**

note -- some of them are hard to read, but you can hover over many of them for examples

---

## Translating Data-to-Viz pages

To translate main page use [Google Translate for Webpages](https://translate.google.com/?sl=auto&tl=en&op=websites) for the direct url: [https://www.data-to-viz.com/#spider](https://www.data-to-viz.com/#spider)

---

## Translating Data-to-Viz pages

To translate main page use [Google Translate for Webpages](https://translate.google.com/?sl=auto&tl=en&op=websites) for the direct url: [https://www.data-to-viz.com/#spider](https://www.data-to-viz.com/#spider)

"Hover-overs" won't work, so, keeping the original, untranslated site open pick a specific plot:
<img src="images/clickonpage.png" width="80%" alt="The data-to-viz.com histogram pop-up, with the 'See the dedicated page' link at the bottom outlined in red.">



---

## Translating Data-to-Viz pages

To translate main page use [Google Translate for Webpages](https://translate.google.com/?sl=auto&tl=en&op=websites) for the direct url: [https://www.data-to-viz.com/#spider](https://www.data-to-viz.com/#spider)

"Hover-overs" won't work, so, keeping the original, untranslated site open pick a specific plot:
<img src="images/clickonpage.png" width="80%" alt="The data-to-viz.com histogram pop-up, with the 'See the dedicated page' link at the bottom outlined in red.">

Then click on the last "dedicated page" link at the bottom and pass that URL to google translate, for example [https://www.data-to-viz.com/graph/histogram.html](https://www.data-to-viz.com/graph/histogram.html).

notes:
**actually go through these!**

---

<br/><br/><br/>
# Designing a Good Viz: Part 2
## How do we avoid misleading folks?

notes:

let's say we've figured out what visual representation we want to use -- so, we've chosen the right plot for our data

how do we avoid misleading folks?

---

## Tufte's 6 Principles for Graphical Excellence

1. **Comparisons:**  Show data by comparisons (bar charts and the like) to depict contrasts and differences between dependent variables.

2. **Causality:**  Demonstrate how one or more independent variables impact or influence dependent variables.

3. **Multivariate:** Various data are combined so an audience can easily interpret an otherwise complex narrative.

4. **Integration:**  Incorporate various modes of information (texts, maps, calculations, diagrams, etc.), to show evidence of source data-to-findings. 

5. **Documentation:**  For credibility, include attribution, detailed titles, and measurements (scales).

6. **Context:** Describe or depict the before and after state. Show trend lines to hint at results in the future.

Excerpt from [ISDI](https://internationalservicedesigninstitute.com/tuftes-6-principles-graphical-integrity-adopted-service-design/).

notes:
so someone you should probably know about is Edward Tufte who's pretty famous in design

while we won't have time to go through all of these principles in detail today (Knaflic's book, linked on the syllabus, covers them in more depth)... 

---

## Tufte's 6 Principles for Graphical Excellence

1. <font color='gray'>**Comparisons:**  Show data by comparisons (bar charts and the like) to depict contrasts and differences between dependent variables.</font>

2. <font color='gray'>**Causality:**  Demonstrate how one or more independent variables impact or influence dependent variables.</font>

3. <font color='gray'>**Multivariate:** Various data are combined so an audience can easily interpret an otherwise complex narrative.</font>

4. <font color='gray'>**Integration:**  Incorporate various modes of information (texts, maps, calculations, diagrams, etc.), to show evidence of source data-to-findings.</font> 

5. <font color='gray'>**Documentation:**  For credibility, include attribution, detailed titles, and measurements (scales).</font>

6. <font color='gray'>**Context:** Describe or depict the before and after state. Show trend lines to hint at results in the future.</font>

Excerpt from [ISDI](https://internationalservicedesigninstitute.com/tuftes-6-principles-graphical-integrity-adopted-service-design/).

notes:
let's do a quick overview

---

## Tufte's 6 Principles for Graphical Excellence

1. **Comparisons:**  Show data by comparisons (bar charts and the like) to depict contrasts and differences between dependent variables.

2. <font color='gray'>**Causality:**  Demonstrate how one or more independent variables impact or influence dependent variables.</font>

3. <font color='gray'>**Multivariate:** Various data are combined so an audience can easily interpret an otherwise complex narrative.</font>

4. <font color='gray'>**Integration:**  Incorporate various modes of information (texts, maps, calculations, diagrams, etc.), to show evidence of source data-to-findings.</font> 

5. <font color='gray'>**Documentation:**  For credibility, include attribution, detailed titles, and measurements (scales).</font>

6. <font color='gray'>**Context:** Describe or depict the before and after state. Show trend lines to hint at results in the future.</font>

Excerpt from [ISDI](https://internationalservicedesigninstitute.com/tuftes-6-principles-graphical-integrity-adopted-service-design/).

notes:

---

## Tufte's 6 Principles for Graphical Excellence

1. <font color='gray'>**Comparisons:**  Show data by comparisons (bar charts and the like) to depict contrasts and differences between dependent variables.</font>

2. **Causality:**  Demonstrate how one or more independent variables impact or influence dependent variables.

3. <font color='gray'>**Multivariate:** Various data are combined so an audience can easily interpret an otherwise complex narrative.</font>

4. <font color='gray'>**Integration:**  Incorporate various modes of information (texts, maps, calculations, diagrams, etc.), to show evidence of source data-to-findings.</font> 

5. <font color='gray'>**Documentation:**  For credibility, include attribution, detailed titles, and measurements (scales).</font>

6. <font color='gray'>**Context:** Describe or depict the before and after state. Show trend lines to hint at results in the future.</font>

Excerpt from [ISDI](https://internationalservicedesigninstitute.com/tuftes-6-principles-graphical-integrity-adopted-service-design/).

notes:

---

## Tufte's 6 Principles for Graphical Excellence

1. <font color='gray'>**Comparisons:**  Show data by comparisons (bar charts and the like) to depict contrasts and differences between dependent variables.</font>

2. <font color='gray'>**Causality:**  Demonstrate how one or more independent variables impact or influence dependent variables.</font>

3. **Multivariate:** Various data are combined so an audience can easily interpret an otherwise complex narrative.

4. <font color='gray'>**Integration:**  Incorporate various modes of information (texts, maps, calculations, diagrams, etc.), to show evidence of source data-to-findings.</font> 

5. <font color='gray'>**Documentation:**  For credibility, include attribution, detailed titles, and measurements (scales).</font>

6. <font color='gray'>**Context:** Describe or depict the before and after state. Show trend lines to hint at results in the future.</font>

Excerpt from [ISDI](https://internationalservicedesigninstitute.com/tuftes-6-principles-graphical-integrity-adopted-service-design/).

notes:

---

## Tufte's 6 Principles for Graphical Excellence

1. <font color='gray'>**Comparisons:**  Show data by comparisons (bar charts and the like) to depict contrasts and differences between dependent variables.</font>

2. <font color='gray'>**Causality:**  Demonstrate how one or more independent variables impact or influence dependent variables.</font>

3. <font color='gray'>**Multivariate:** Various data are combined so an audience can easily interpret an otherwise complex narrative.</font>

4. **Integration:**  Incorporate various modes of information (texts, maps, calculations, diagrams, etc.), to show evidence of source data-to-findings. 

5. <font color='gray'>**Documentation:**  For credibility, include attribution, detailed titles, and measurements (scales).</font>

6. <font color='gray'>**Context:** Describe or depict the before and after state. Show trend lines to hint at results in the future.</font>

Excerpt from [ISDI](https://internationalservicedesigninstitute.com/tuftes-6-principles-graphical-integrity-adopted-service-design/).

notes:

---

## Tufte's 6 Principles for Graphical Excellence

1. <font color='gray'>**Comparisons:**  Show data by comparisons (bar charts and the like) to depict contrasts and differences between dependent variables.</font>

2. <font color='gray'>**Causality:**  Demonstrate how one or more independent variables impact or influence dependent variables.</font>

3. <font color='gray'>**Multivariate:** Various data are combined so an audience can easily interpret an otherwise complex narrative.</font>

4. <font color='gray'>**Integration:**  Incorporate various modes of information (texts, maps, calculations, diagrams, etc.), to show evidence of source data-to-findings.</font> 

5. **Documentation:**  For credibility, include attribution, detailed titles, and measurements (scales).

6. <font color='gray'>**Context:** Describe or depict the before and after state. Show trend lines to hint at results in the future.</font>

Excerpt from [ISDI](https://internationalservicedesigninstitute.com/tuftes-6-principles-graphical-integrity-adopted-service-design/).

notes:

---

## Tufte's 6 Principles for Graphical Excellence

1. <font color='gray'>**Comparisons:**  Show data by comparisons (bar charts and the like) to depict contrasts and differences between dependent variables.</font>

2. <font color='gray'>**Causality:**  Demonstrate how one or more independent variables impact or influence dependent variables.</font>

3. <font color='gray'>**Multivariate:** Various data are combined so an audience can easily interpret an otherwise complex narrative.</font>

4. <font color='gray'>**Integration:**  Incorporate various modes of information (texts, maps, calculations, diagrams, etc.), to show evidence of source data-to-findings.</font> 

5. <font color='gray'>**Documentation:**  For credibility, include attribution, detailed titles, and measurements (scales).</font>

6. **Context:** Describe or depict the before and after state. Show trend lines to hint at results in the future.

Excerpt from [ISDI](https://internationalservicedesigninstitute.com/tuftes-6-principles-graphical-integrity-adopted-service-design/).

notes:

---

## Tufte's 6 Principles for Graphical Excellence

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20240513134644/Pic-1.jpeg" width="80%" alt="Infographic of five Tufte principles: 1. Maximize data-ink ratio, 2. Minimize chartjunk, 3. Data over design variation, 4. Use small multiples, 5. Provide context.">

notes:
you'll often see representations like this which are more of a list of things to not do

---

## Tufte's 6 Principles for Graphical Excellence

<img src="images/tufte/g4g_dataInkRatio.jpeg" width="80%" alt="The same Tufte principles infographic with principle 1, 'Maximize Data-Ink Ratio', outlined in red. Original from geeksforgeeks.org.">

notes:
for example, "maximize data-ink ratio"

---

## Tufte's 6 Principles for Graphical Excellence

<img src="https://i.ytimg.com/vi/JIMUzJzqaA8/maxresdefault.jpg" alt="Two versions of the same monthly bar chart (Jan to Sep, 5% to 15%). Left, labeled 'low data-ink ratio', has a teal background and heavy grid lines. Right, labeled 'high data-ink ratio', has only the bars, with white lines cutting through them for the gridlines.">

notes:
this along with the "minimize chart junk" is very much centered around maximizing the "work" that each element of your visualization is doing to convey information to your viewer

for example the blue background here was not adding any useful information, same with the grid lines

---

## Tufte's 6 Principles for Graphical Excellence

<img src="https://i.ytimg.com/vi/JIMUzJzqaA8/maxresdefault.jpg" alt="Two versions of the same monthly bar chart (Jan to Sep, 5% to 15%). Left, labeled 'low data-ink ratio', has a teal background and heavy grid lines. Right, labeled 'high data-ink ratio', has only the bars, with white lines cutting through them for the gridlines.">

[Storytelling with Data: A Data Visualization Guide for Business Professionals](https://i-share-uiu.primo.exlibrisgroup.com/permalink/01CARLI_UIU/q00vor/cdi_askewsholts_vlebooks_9781119002062) by Knaflic is a great resource for more info.

notes:
there will be more examples of this as you go through the reading, 

and there are also some extra examples in Chapter 9 of Knaflic if you want to dig deeper after the workshop.

---

<embed src="https://www.data-to-viz.com/caveats.html" style="width:100%; height:80vh">

notes:
a little more practically, there is also the "Caveats" section of the Data-Viz-Picker website we looked at before that lists of several caveats that you'll want to be aware of for each type of visualization

similar with the viz-picker, once you have a type of plot, let's say a line plot, then you can head over to this page to see some of the caveats associated with these types of plots

**click on spaghetti chart**

**also click on the "misleading" tab**

note -- even the ones not labeled "misleading" could still be misleading!
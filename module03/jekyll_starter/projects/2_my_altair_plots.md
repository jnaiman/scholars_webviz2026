---
title: Interactive Plots with Altair
tools: [Python, Altair, vega-lite]
image: my_assets/pngs/altair_workshop_card.png
description: Four interactive plots made in Python with Altair, from the Bolashak Scholars Web Viz Workshop.
custom_js:
  - vega.min
  - vega-lite.min
  - vega-embed.min
  - justcharts
---

<!--
  HOW THIS FILE WORKS (this comment does not show on your website)

  * The part between the two "---" lines at the top is the "front matter":
      title        -> the page title and the name on your Projects page card
      tools        -> the little tags on the card
      image        -> the picture on the card (a file in my_assets/pngs/)
      description  -> the text on the card
      custom_js    -> loads the code that draws the plots.  KEEP THESE FOUR LINES
                      on every page with an interactive plot!
  * Everything below is Markdown (like Jupyter text cells), plus one
    <vegachart> line for each plot.  schema-url points at a .json file you
    saved with Altair and uploaded to my_assets/json/.
  * The file name starts with "2_" so it is listed after 1_Vega_lite_project.md.
-->

# Interactive plots with Altair

These plots were made in Python with [Altair](https://altair-viz.github.io/), saved as vega-lite `.json` files, and embedded here. Everything you see is interactive -- hover, click and drag!

## Who moves up?

The [mobility dataset](https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv) measures how likely a child from a low-income family in each US region is to move up in income as an adult. Pick a state from the dropdown to highlight its regions; hover for details, scroll to zoom.

<vegachart schema-url="{{ site.baseurl }}/my_assets/json/mobility_scatter.json" style="width: 100%"></vegachart>

Dot size shows population. Notice that higher income doesn't automatically mean higher mobility.

## A linked dashboard

Drag a box on the left plot (regions grouped by state and student/teacher ratio) to update the histogram of mobility on the right.

<vegachart schema-url="{{ site.baseurl }}/my_assets/json/mobility_dashboard.json" style="width: 100%"></vegachart>

## How many regions per state?

This plot reads its data straight from the web, so its `.json` file is tiny.

<vegachart schema-url="{{ site.baseurl }}/my_assets/json/bars_by_state.json" style="width: 100%"></vegachart>

## Corgis!

Corgis born per year in the six countries with the most corgis (data from the [Cardigan Archives](http://cardiped.net/)). Click a country in the legend to highlight it.

<vegachart schema-url="{{ site.baseurl }}/my_assets/json/corgis_over_time.json" style="width: 100%"></vegachart>

## The data and the code

<div class="left">
{% include elements/button.html link="https://github.com/UIUC-iSchool-DataViz/is445_data" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/jnaiman/scholars_webviz2026/blob/main/module03/altair_to_json.ipynb" text="The Analysis" %}
</div>

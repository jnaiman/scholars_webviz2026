---
title: Lecture 3.1 - Interactive Plots with Altair
layout: lecture
tags:
  - altair
  - vega-lite
  - python
  - hands-on
description: >-
  Making interactive plots in Python with Altair, and saving them as vega-lite JSON files.
date: 2026-12-05
---

<br/><br/><br/>
# Interactive Plots with Altair

notes:
in Module 2 we talked about how to design a good viz -- now let's build some that people can interact with on the web

---

## The plan for Modules 3 & 4

1. Make interactive plots in **Python** with **Altair** (this lecture)
2. Put them on your **Jekyll** website as `.json` files (Lecture 3.2)
3. Put them in a **Streamlit** app (Module 4)

The same Altair code works for both!

notes:
the nice thing about altair is that it's one way of making plots that ends up in both of our web "homes"

---

## vega-lite: a plot as a text file

[vega-lite](https://vega.github.io/vega-lite/) describes a plot in **JSON** -- just text:

```json
{
  "data": {"url": "https://.../mobility.csv"},
  "mark": "bar",
  "encoding": {
    "x": {"field": "State", "type": "nominal"},
    "y": {"aggregate": "count", "type": "quantitative"}
  }
}
```

Web browsers know how to draw it (with JavaScript). See the [vega-lite example gallery](https://vega.github.io/vega-lite/examples/).

notes:
"json" = javascript object notation, a common way to store structured data as text

this is the key idea: if a plot is a text file, we can upload it anywhere, like any other file, and a webpage can draw it

---

## Altair: Python → vega-lite

[Altair](https://altair-viz.github.io/) writes that JSON for you, from Python:

```python
import altair as alt

alt.Chart(mobility_url).mark_bar().encode(
    x="State:N",
    y="count():Q"
)
```

notes:
same plot as the last slide!  altair just builds the json

and you can do all your data cleaning in pandas first, which is where Python shines

---

## Anatomy of an Altair plot

```python
alt.Chart(DATA).mark_TYPE().encode(CHANNEL="COLUMN:TYPE", ...)
```

* **`Chart(...)`** -- a pandas DataFrame *or* a URL to a CSV/JSON
* **`mark_...()`** -- `mark_bar`, `mark_point`, `mark_circle`, `mark_line`, `mark_rect`, ...
* **`encode(...)`** -- `x`, `y`, `color`, `size`, `opacity`, `tooltip`, ...

notes:
three pieces every time: data, mark, encoding

---

## Data types

| Code | Type | Example |
|---|---|---|
| `:Q` | quantitative (a number) | `Income:Q` |
| `:N` | nominal (a category, no order) | `State:N` |
| `:O` | ordinal (a category with an order) | `Years:O` |
| `:T` | temporal (a date/time) | `Date:T` |

notes:
these tie straight back to Module 2!  the type changes which scales and colors altair picks

e.g. color with :N gives distinct hues, color with :Q gives a gradient

---

## Encodings ↔ perception channels

From Module 2: **position** is our most accurate channel, then length, angle, area, color...

```python
.encode(
    x="Income:Q",        # position -- most important variable
    y="Mobility:Q",      # position
    size="Population:Q", # area -- less precise, "extra" info
    color="State:N",     # hue -- good for categories
)
```

notes:
so a good habit: put the variable you care most about on x or y

---

## Interactivity, level 1: tooltips & zoom

```python
alt.Chart(df).mark_circle().encode(
    x="Income:Q",
    y="Mobility:Q",
    tooltip=["Name:N", "State:N", "Mobility:Q"]
).interactive()
```

* `tooltip` -- info on hover
* `.interactive()` -- scroll to zoom, drag to pan

notes:
two lines and you've already got something better than a static image

---

## Interactivity, level 2: selections

A **selection** is a "parameter" the viewer changes by clicking, dragging, or using a widget:

```python
pick_state = alt.selection_point(
    fields=["State"],
    bind=alt.binding_select(options=states, name="Highlight a state: ")
)

chart.encode(
    color=alt.condition(pick_state, alt.value("steelblue"), alt.value("lightgray"))
).add_params(pick_state)
```

notes:
selection_point = click (or a widget, via bind); selection_interval = drag a box (a "brush")

alt.condition = "if selected, this color, otherwise gray"

---

## Interactivity, level 3: linked plots

```python
brush = alt.selection_interval(encodings=["x", "y"])

left  = alt.Chart(url).mark_rect().encode(...).add_params(brush)
right = alt.Chart(url).mark_bar().encode(...).transform_filter(brush)

left | right     # side by side
```

Dragging on the left **filters** the right.

notes:
this is a mini-dashboard -- the same thing you'd do in PowerBI/Tableau, but in a few lines of code

`|` = side by side, `&` = stacked

---

## Saving: one line

```python
chart.save("my_plot.json")    # for websites (Lecture 3.2) 
chart.save("my_plot.html")    # a stand-alone web page
```

notes:
the json is what we'll put on our Jekyll site

the html is a complete web page you can open or upload anywhere

---

## Where does the data go?

| | `alt.Chart(df)` (DataFrame) | `alt.Chart(url)` (URL) |
|---|---|---|
| Data saved... | **inside** the JSON | stays at the URL |
| File size | bigger | tiny |
| Works offline / if the URL moves? | yes | no |
| Can use pandas first? | yes | only vega-lite transforms |

**Tip:** only pass the columns you plot: `alt.Chart(df[["Name", "Income", "Mobility"]])`

notes:
for the DataFrame version, altair will refuse more than 5000 rows by default -- that's a hint to aggregate or use a URL

---

## Sizing for the web

* `width="container"` -- fill the page width (single plots)
* `width=300` -- fixed pixels (needed for side-by-side plots)

```python
chart.properties(width="container", height=350)
```

notes:
container plots can look small in the notebook -- they'll fill the page on your site

---

## Hands-on: the Module 3 notebook

[altair_to_json.ipynb](COURSE_WEBPAGE/nbv.html?notebook_name=COURSE_WEBPAGE/module03/altair_to_json.ipynb)

* **Track A:** download it, `conda activate webviz`, `jupyter lab`
* **Track B:** [open it in Colab](COURSE_COLAB/module03/altair_to_json.ipynb)

We'll make 4 plots and save 4 JSON files.

notes:
**work through the notebook together**

1. bar chart from a URL
2. scatter with a dropdown
3. linked dashboard
4. corgis! -- with a pandas melt to reshape the data first

---

## Try it yourself

Change something and re-save:
* a different column, mark, or title
* a color scheme: `scale=alt.Scale(scheme="viridis")`
* steal from the [Altair gallery](https://altair-viz.github.io/gallery/index.html) -- every example ends with a `chart` you can `.save()`

notes:
remember the Module 2 advice -- what's the point of your plot? who is it for?

next: put these on your website!

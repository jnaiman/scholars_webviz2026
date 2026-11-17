---
title: Lecture 5.1 - Putting It Together & Where to Go from Here
layout: lecture
tags:
  - publishing
  - other viz engines
  - sharable viz
description: >-
  Link your Streamlit app and your Jekyll site, then a few future resources.
date: 2026-12-10
---

<br><br><br>
# Putting It Together & Where to Go from Here

---

## What we built

* `https://<you>.github.io` -- a portfolio with interactive Altair plots
* `https://<your-app>.streamlit.app` -- an interactive app

Let's connect them!

---

## 1. A button to your app

On a project page in `projects/`, plain HTML works in Markdown:

```html
<a class="btn btn-outline-primary" href="https://<your-app>.streamlit.app">Try the app</a>
```

The template also has a shortcut for this -- see the "The Data" / "The Analysis" buttons at the bottom of `2_my_altair_plots.md`.

notes:
the template's button include makes exactly this HTML for you; either way works

---

## 2. Embed the app in a page

```html
<iframe src="https://<your-app>.streamlit.app/?embed=true"
        style="width: 100%; height: 800px; border: none;"></iframe>
```

`?embed=true` hides Streamlit's menus so it fits in your page.

notes:
an iframe is a "window" to another website inside your page

if the app is asleep, visitors will see the "wake up" button inside the frame

---

## 3. Your app's repo as a project card

The template can show GitHub repositories as cards on your Projects page. Add your app's repo to `about_me/remote_repos.yml`:

```yaml
- webviz_streamlit
```

Then give the repo a description and topics in its **About** box on GitHub (⚙️).

notes:
the card pulls its description and tags from the repo's About section

---

## 4. Link back from the app

```python
st.markdown("More of my work: [my portfolio](https://<you>.github.io)")
```

---

## More Altair & Streamlit

* [Altair gallery](https://altair-viz.github.io/gallery/index.html) & [interactive charts guide](https://altair-viz.github.io/user_guide/interactions/index.html)
* [Streamlit multi-page apps](https://docs.streamlit.io/develop/concepts/multipage-apps)
* [Streamlit components](https://streamlit.io/components) (maps, extra widgets, ...)
* [Jekyll themes](https://github.com/topics/jekyll-theme) -- the `<vegachart>`/vega-embed trick works with any of them (see [the plain HTML example](COURSE_WEBPAGE/module03/any_site_starter/plot_page.html))

notes:
multi-page apps are the natural next step when an app gets long -- IS445 week 12 has an example

---

## Other web viz tools

* [Plotly](https://plotly.com/python/) / [Dash](https://dash.plotly.com/) -- another Python interactive plotting library & app framework
* [Quarto](https://quarto.org/) -- websites and reports from notebooks
* [Observable](https://observablehq.com/) -- JavaScript notebooks, [D3](https://d3js.org/)
* [Hugging Face Spaces](https://huggingface.co/spaces) -- another place to host Streamlit (and other) apps
* No-code: [PowerBI](https://www.microsoft.com/en-us/power-platform/products/power-bi), [Tableau Public](https://public.tableau.com/), [Looker Studio](https://lookerstudio.google.com/)

notes:
pros/cons as always: programming tools give you more control and are free; no-code tools are faster to start but harder to customize, and some cost $$

---

## Keep in mind when publishing

* Everything on github.io and free Streamlit apps is **public** -- code and data!
* Check the **license**/terms of any data you use, and cite your sources
* Design for your **audience** (Module 2): titles, labels, a sentence on what to notice

notes:
never put passwords, private data or API keys in a public repo

---

## Where to learn more

* Videos on our [MediaSpace Channel](COURSE_MEDIASPACE)
* The [IS445 online materials](COURSE_IS445) -- a whole semester of Altair, Jekyll, Streamlit and more

<br>

### Thank you!

notes:
**show the IS445 page -- weeks 8-13 are where this workshop's material comes from**

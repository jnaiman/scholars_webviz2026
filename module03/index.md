---
layout: week
icon: undraw_static-website_x3tn.svg
visible: true
notitle: true
examples:
  - filename: altair_to_json.ipynb
    type: ipynb
    title: Module 3 notebook (view on this site)
    description: Make four interactive plots and save them as vega-lite JSON files for your website.
  - filename: colab_altair
    type: colab
    title: Module 3 notebook (open in Google Colab)
    description: The same notebook, ready to run in your browser.
    link: module03/altair_to_json.ipynb
  - filename: jekyll_starter
    type: githubtree
    title: Jekyll starter files (project page + ready-made JSONs)
    description: Drop-in files for the online CV template -- upload them into the matching folders of your github.io repository.
    link: module03/jekyll_starter
  - filename: any_site_starter/plot_page.html
    type: link
    title: Plain HTML page with Altair plots (live demo)
    description: For any website or repository without the Jekyll template. <a href="https://github.com/jnaiman/scholars_webviz2026/tree/main/module03/any_site_starter">Source files on GitHub</a>.
  - filename: cv_template
    type: iodide
    title: Online CV (Jekyll) template and README
    description: What every file in the template does.
    link: https://github.com/jnaiman/online_cv_public_fa2026#readme
data:
  - filename: mobility.csv
    type: dataLink
    title: The Mobility dataset
    description: For 741 US regions, how likely a child from a low-income family is to move up in income as an adult ("mobility"), with information on population, income, schools and more. From a <a href="https://www.census.gov/library/working-papers/2018/adrm/CES-WP-18-40R.html">large census study</a>, collected <a href="http://www.stat.cmu.edu/~cshalizi/uADA/15/hw/01/mobility.csv">here</a> (<a href="http://www.stat.cmu.edu/~cshalizi/uADA/15/hw/01/hw-01.pdf">more info</a>).
    link: https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv
  - filename: corgs_per_country_over_time_columns_2020.csv
    type: dataLink
    title: Corgis per country over time
    description: This dataset is from the <a href="http://cardiped.net/">Cardigan Archives</a>, scraped using Beautiful Soup in Python and further processed in Python into this form.
    link: https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/corgs_per_country_over_time_columns_2020.csv
---

# Interactive Altair Plots on Your Jekyll Site

In this module we make interactive plots in Python with [Altair](https://altair-viz.github.io/), save them as [vega-lite](https://vega.github.io/vega-lite/) `.json` files, and show them on a project page of the github.io site we set up in Module 1.

To get the plots onto your site, upload the `.json` files to `my_assets/json/` and the project page to `projects/` with **Add file → Upload files** on github.com. Your own JSONs from the notebook work, and so do the ready-made files in the [Jekyll starter folder](https://github.com/{{site.githuburlbase}}{{site.baseurl}}/tree/{{site.branch}}/module03/jekyll_starter).

Each plot is one line on a project page (and the page needs the `custom_js` lines in its front matter -- see [Lecture 3.2](lecture3p2.html)):

```html
{% raw %}<vegachart schema-url="{{ site.baseurl }}/my_assets/json/mobility_scatter.json" style="width: 100%"></vegachart>{% endraw %}
```

Not using the template? The same `.json` files work on any web page -- see the [plain HTML example](any_site_starter/plot_page.html).

Prefer to preview your site on your own computer before uploading? See [Module 6]({{site.baseurl}}/module06/) (optional).

### Optional Reading and Materials

1. <a href="https://altair-viz.github.io/gallery/index.html">Altair example gallery</a> and docs -- in particular <a href="https://altair-viz.github.io/user_guide/encodings/index.html#encoding-data-types">Encoding Data Types</a>, <a href="https://altair-viz.github.io/user_guide/interactions/index.html">Interactive Charts</a>, <a href="https://altair-viz.github.io/user_guide/interactions/bindings_widgets.html">Widgets & Bindings</a> and <a href="https://altair-viz.github.io/user_guide/saving_charts.html">Saving Altair Charts</a>
2. <a href="https://vega.github.io/vega-lite/examples/">vega-lite example gallery</a> and the <a href="https://vega.github.io/editor/">online vega editor</a>
3. <a href="https://jekyllrb.com/docs/step-by-step/01-setup/">Jekyll step-by-step tutorial</a> and <a href="https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll">GitHub Pages & Jekyll</a>
4. <a href="https://www.markdownguide.org/cheat-sheet/">Markdown cheat sheet</a>
5. IS445 materials this module is based on: <a href="https://uiuc-ischool-dataviz.github.io/is445_bcu_fall2026/week08/">Week 8 (Altair)</a>, <a href="https://uiuc-ischool-dataviz.github.io/is445_bcu_fall2026/week09/">Week 9 (Jekyll)</a> and the <a href="https://uiuc-ischool-dataviz.github.io/is445_bcu_fall2026/week09/jekyll_tour_notes.html">Jekyll template tour notes</a>

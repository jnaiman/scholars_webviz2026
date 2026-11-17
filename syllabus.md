---
layout: syllabus
title: Syllabus
notitle: true
---

{% assign cv = site.data.class.urls | where: "id", "cv_template" | first %}
{% assign st_tmpl = site.data.class.urls | where: "id", "streamlit_template" | first %}
{% assign is445 = site.data.class.urls | where: "id", "is445" | first %}
{% assign repo = "https://github.com/" | append: site.githuburlbase | append: site.baseurl %}
{% assign colab = "https://colab.research.google.com/github/" | append: site.githuburlbase | append: site.baseurl | append: "/blob/" | append: site.branch %}

## Welcome to the Bolashak Scholars Web Viz Workshop!

Data visualization is crucial to conveying information drawn from models,
observations or investigations. This workshop will provide a brief overview of
visualization "best practices" and where things can "go wrong" with data viz, and then
put them into practice on the web: we'll make interactive plots in Python with
<a href="https://altair-viz.github.io/">Altair</a>, publish them on **your own website**
built with <a href="https://jekyllrb.com/">Jekyll</a> and
<a href="https://pages.github.com/">GitHub Pages</a>, and build an interactive
<a href="https://streamlit.io/">Streamlit</a> app hosted on
<a href="https://share.streamlit.io/">Streamlit Community Cloud</a>. All of these are free.

## Prerequisites: Highly suggested pre-installation

**There are two ways to take part, and everything in the workshop works in both:**

* **Track A -- install on my computer:** faster to work with, and what you'll want if you keep building websites and apps afterwards.
* **Track B -- browser only:** nothing to install. You'll use Google Colab for Python and upload/edit files directly on github.com.

Full step-by-step instructions (with troubleshooting) are on the
<a href="{{site.baseurl}}/module01/installation_instructions.html">Installation & Setup Instructions page</a>,
and in the <a href="{{site.baseurl}}/module01/lecture01p0.html">Lecture 1.0 slides</a>. In short:

#### 1. Make your accounts (everyone)
* A free <a href="https://github.com/signup">GitHub account</a> -- your username becomes your website address, `<username>.github.io`.
* A free <a href="https://share.streamlit.io/">Streamlit Community Cloud</a> account -- click "Continue with GitHub".
* Track B: a Google account for <a href="https://colab.research.google.com/">Google Colab</a>.

#### 2. Python (Track A) or Google Colab (Track B)
* Track A: install <a href="https://www.anaconda.com/download/success">Miniconda</a> and create the workshop environment with <a href="{{ repo }}/raw/{{ site.branch }}/module01/env_files/environment.yml">environment.yml</a>.
* Everyone: run the <a href="{{site.baseurl}}/nbv.html?notebook_name={{ '/module01/test_install.ipynb' | relative_url | url_encode }}">test-your-setup notebook</a> -- locally, or <a href="{{ colab }}/module01/test_install.ipynb">in Colab</a>.

#### 3. git and Ruby/Jekyll (Track A only)
This is the step most likely to need troubleshooting -- please start it early!
* <a href="https://git-scm.com/downloads">git</a>
* Ruby 3.3 or 3.4 and Jekyll, following the <a href="https://jekyllrb.com/docs/installation/">official guide for your system</a>.

#### 4. (Optional) Get a head start on Module 1
Put the <a href="{{ cv.url }}">online CV template</a> on your github.io site and deploy the <a href="{{ st_tmpl.url }}">Streamlit starter app</a> -- see <a href="{{site.baseurl}}/module01/lecture01p2.html">Lecture 1.2</a>. We'll also do this together in the workshop.

## Modules

This workshop will be conducted in several main Modules.

Below are some links to further reading. *All Reading/Materials are **optional*** and can be revisited after the workshop!

<style>
table th:first-of-type {
    width: 10%;
}
table th:nth-of-type(2) {
    width: 30%;
}
table th:nth-of-type(3) {
    width: 60%;
}
</style>

| Module   | Topic  |  Readings/Materials
-------|-------------------|---------
| <a href="{{site.baseurl}}/module01">Module 1</a> | Introduction & Setup | 0. <a href="{{site.baseurl}}/module01/installation_instructions.html">Installation & Setup Instructions</a> (do this pre-workshop!) <br> 1. Who is [your instructor](https://www.astronaiman.com/) anyway? <br> 2. <a href="https://docs.github.com/en/pages/quickstart">GitHub Pages quickstart</a> <br> 3. <a href="{{ cv.url }}#readme">The online CV template's README</a> <br> 4. <a href="https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app">Deploying on Streamlit Community Cloud</a> <br> 5. <a href="https://clauswilke.com/dataviz/">Fundamentals of Data Visualization by Claus O. Wilke</a> <br> 6. <a href="https://www.amazon.com/Visualization-Analysis-Design-AK-Peters/dp/1466508914/">Visualization Analysis & Design, Tamara Munzner</a>. Many concepts found on [the book's webpage](https://www.cs.ubc.ca/~tmm/vadbook/) and the [associated lecture slides](https://www.cs.ubc.ca/~tmm/talks.html#vadallslides).
| <a href="{{site.baseurl}}/module02">Module 2</a> | Data Viz Basics | 1. <a href="https://www.csc2.ncsu.edu/faculty/healey/PP/">Perception in Visualization</a> <br> 2. <a href="https://www.data-to-viz.com/#spider">The Data Viz Picker</a> <br> 3. <a href="https://www.data-to-viz.com/caveats.html">Data Viz Caveats</a> <br> 4. <a href="https://i-share-uiu.primo.exlibrisgroup.com/permalink/01CARLI_UIU/q00vor/cdi_askewsholts_vlebooks_9781119002062">Storytelling with Data: A Data Visualization Guide for Business Professionals</a> by Knaflic (available via UIUC library).
| <a href="{{site.baseurl}}/module03">Module 3</a> | Interactive Altair Plots on Your Jekyll Site | 1. <a href="{{site.baseurl}}/nbv.html?notebook_name={{ '/module03/altair_to_json.ipynb' | relative_url | url_encode }}">Module 3 notebook</a> (or <a href="{{ colab }}/module03/altair_to_json.ipynb">open in Colab</a>) <br> 2. <a href="{{ repo }}/tree/{{ site.branch }}/module03/jekyll_starter">Jekyll starter files</a> -- a project page and ready-made plot files to upload to your site <br> 3. <a href="https://altair-viz.github.io/gallery/index.html">Altair example gallery</a> and <a href="https://altair-viz.github.io/user_guide/interactions/index.html">interactive charts guide</a> <br> 4. <a href="https://vega.github.io/vega-lite/examples/">vega-lite examples</a> <br> 5. <a href="https://jekyllrb.com/docs/step-by-step/01-setup/">Jekyll step-by-step tutorial</a>
| <a href="{{site.baseurl}}/module04">Module 4</a> | Streamlit Apps on Streamlit Community Cloud | 1. <a href="{{ repo }}/tree/{{ site.branch }}/module04/streamlit_starter">Streamlit starter app files</a> <br> 2. <a href="https://docs.streamlit.io/get-started/fundamentals/main-concepts">Streamlit main concepts</a> and <a href="https://docs.streamlit.io/get-started/tutorials/create-an-app">"Create an app" tutorial</a> <br> 3. <a href="https://docs.streamlit.io/develop/api-reference/charts/st.altair_chart">Altair charts in Streamlit</a> <br> 4. <a href="https://streamlit.io/gallery">Streamlit app gallery</a>
| <a href="{{site.baseurl}}/module05">Module 5</a> | Putting It Together & Where to Go from Here | 1. See <a href="{{site.baseurl}}/module05/lecture5p1.html">the Module 5 Lecture</a> for more resources <br> 2. <a href="{{ is445.url }}">IS445 online materials</a> (Weeks 8-13 cover Altair, Jekyll and Streamlit in more depth)

## A note on privacy

Your github.io site, the GitHub repositories behind it and your app, and free Streamlit apps are all **public**. Only publish data you are allowed to share, and never put passwords or private information in a repository.

## Translating this website

Translation for materials on this website using Google Translate has not been tested fully (given the author's mono-language nature, sadly), however it is possible that this may be effective since most material is rendered as HTML.  To try this out go to [Google Translate for Webpages](https://translate.google.com/?sl=auto&tl=en&op=websites) and put in the URL for the page you are interested in rendering and select your language to render to.

Some notes:
1. Translation of lecture slides is somewhat supported, however you may need to play with the zoom in/out on your browser to see slides with larger images/text
2. For some of the external links, like the [Data-to-Viz Viz-Picker](https://www.data-to-viz.com/#spider) not all elements will render from the "base" webpage.  For example if you click on the "histogram" bubble icon on this page, nothing will pop up when using Google Translate, so your best bet is to start from the non-translated version and then click on the histogram bubble, and then click on the last link called "See the dedicated page." and then render the full histogram page that pops up (for example: [https://www.data-to-viz.com/graph/histogram.html](https://www.data-to-viz.com/graph/histogram.html).)
3. Code (in the notebooks, starter files and slides) should **not** be translated -- if a translated page shows code, copy it from the untranslated version.

We will go over this in the workshop as well!

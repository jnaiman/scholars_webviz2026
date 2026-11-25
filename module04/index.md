---
layout: week
icon: undraw_dashboard_p93p.svg
visible: true
notitle: true
examples:
  - filename: streamlit_starter
    type: githubtree
    title: Streamlit starter app files
    description: streamlit_app.py, requirements.txt and a Module 3 JSON plot -- upload them to any public GitHub repository and deploy.
    link: module04/streamlit_starter
  - filename: streamlit_app.py
    type: github
    title: Read the starter app's code (streamlit_app.py)
    description: Widgets, Altair plots, selections sent back to Python, tabs and a data table, with comments.
    link: module04/streamlit_starter/streamlit_app.py
  - filename: streamlit_template
    type: iodide
    title: Starter repository to fork
    description: The repository we fork in Lecture 4.1 -- the simplest possible app.
    link: https://github.com/jnaiman/is445_streamlit_demo
  - filename: streamlit_cloud
    type: iodide
    title: Streamlit Community Cloud
    description: Sign in with GitHub, then deploy and manage your apps.
    link: https://share.streamlit.io/
data:
  - filename: mobility.csv
    type: dataLink
    title: The Mobility dataset
    description: The dataset the starter app explores. For 741 US regions, how likely a child from a low-income family is to move up in income as an adult, plus population, income, schools and more (<a href="http://www.stat.cmu.edu/~cshalizi/uADA/15/hw/01/hw-01.pdf">more info</a>).
    link: https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv
---

# Streamlit Apps on Streamlit Community Cloud

In this module we turn a Python script into an interactive web app with [Streamlit](https://streamlit.io/), put Altair plots in it, and host it for free on [Streamlit Community Cloud](https://share.streamlit.io/).

This module is **self-contained**: all you need is your GitHub account from Module 1. We make the Streamlit account and deploy a first app together in [Lecture 4.1](lecture4p1.html).

An app is just **two files** in a **public GitHub repository** (or a folder in one): `streamlit_app.py` and `requirements.txt`. We upload and edit them on github.com (or press `.` on your repository page for the [github.dev](https://github.dev) editor), and Streamlit Cloud rebuilds the app after every commit.

The [starter app](https://github.com/{{site.githuburlbase}}{{site.baseurl}}/tree/{{site.branch}}/module04/streamlit_starter) has examples of everything in [Lecture 4.2](lecture4p2.html); [Lecture 4.3](lecture4p3.html) covers putting it online and fixing problems.

Prefer to run your app on your own computer while you work on it? See [Module 6]({{site.baseurl}}/module06/) (optional).

### Optional Reading and Materials

1. <a href="https://docs.streamlit.io/get-started/fundamentals/main-concepts">Streamlit main concepts</a> and the <a href="https://docs.streamlit.io/get-started/tutorials/create-an-app">"Create an app" tutorial</a>
2. Streamlit API docs for <a href="https://docs.streamlit.io/develop/api-reference/text">text</a>, <a href="https://docs.streamlit.io/develop/api-reference/widgets">widgets</a>, <a href="https://docs.streamlit.io/develop/api-reference/layout">layout</a> and <a href="https://docs.streamlit.io/develop/api-reference/charts/st.altair_chart">Altair charts</a> (including <a href="https://docs.streamlit.io/develop/concepts/design/dataframes">dataframes</a> and <a href="https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data">caching</a>)
3. <a href="https://docs.streamlit.io/deploy/streamlit-community-cloud">Streamlit Community Cloud docs</a>, especially <a href="https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app">Deploy your app</a> and <a href="https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app">Manage your app</a>
4. <a href="https://streamlit.io/gallery">Streamlit app gallery</a> -- find one you like and look at its code
5. IS445 materials this module is based on: <a href="https://uiuc-ischool-dataviz.github.io/is445_bcu_fall2026/week10/">Week 10</a>, <a href="https://uiuc-ischool-dataviz.github.io/is445_bcu_fall2026/week11/">Week 11</a>, <a href="https://uiuc-ischool-dataviz.github.io/is445_bcu_fall2026/week12/">Week 12 (multi-page apps)</a>

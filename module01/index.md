---
layout: week
icon: undraw_professor_d7zn.svg
visible: true
notitle: true
examples:
  - filename: installation_instructions.html
    type: link
    title: Installation & Setup Instructions
    description: Step-by-step setup for both tracks (install locally, or browser only), plus troubleshooting.
  - filename: test_install.ipynb
    type: ipynb
    title: Test-your-setup notebook
    description: Checks your packages, makes your first Altair plot, and saves it as a JSON file.
  - filename: colab_test
    type: colab
    title: Test-your-setup notebook (open in Google Colab)
    description: The same notebook, for the browser-only track.
    link: module01/test_install.ipynb
  - filename: environment.yml
    type: githubraw
    title: Conda environment file (environment.yml)
    description: "Create the workshop environment with: conda env create -f environment.yml"
    link: module01/env_files/environment.yml
  - filename: requirements.txt
    type: githubraw
    title: pip requirements file (requirements.txt)
    description: For people who prefer pip over conda.
    link: module01/env_files/requirements.txt
  - filename: cv_template
    type: iodide
    title: Online CV (Jekyll) template
    description: The template for your github.io site (see its README for details on every file).
    link: https://github.com/jnaiman/online_cv_public_fa2026
  - filename: streamlit_cloud
    type: iodide
    title: Streamlit Community Cloud
    description: Sign in with GitHub to host your Streamlit apps.
    link: https://share.streamlit.io/
---

{% assign cv = site.data.class.urls | where: "id", "cv_template" | first %}
{% assign st_tmpl = site.data.class.urls | where: "id", "streamlit_template" | first %}

# Introduction & Setup

This module covers an introduction to the workshop and your instructor, and gets you set up with:

* **Python** with Altair, pandas and Streamlit (or Google Colab instead),
* a **GitHub** account and a personal website at `<your-username>.github.io` built from the [online CV template]({{ cv.url }}), and
* a **Streamlit Community Cloud** account with a first app deployed from [a starter repository]({{ st_tmpl.url }}).

There are **two tracks**, and everything in the workshop works in both:

* **Track A -- install on my computer:** Miniconda, git, Ruby & Jekyll. Faster to work with once it's set up.
* **Track B -- browser only:** nothing to install. Use Google Colab for Python and upload/edit files directly on github.com.

**Please try to do the steps in [Lecture 1.0](lecture01p0.html) / the [Installation & Setup Instructions](installation_instructions.html) before the workshop.**

### Optional Materials and Resources
1. Who is [your instructor](https://www.astronaiman.com/) anyway?
2. [GitHub Pages quickstart](https://docs.github.com/en/pages/quickstart) and [GitHub's "Hello World" tutorial](https://docs.github.com/en/get-started/start-your-journey/hello-world)
3. [Jekyll installation guides](https://jekyllrb.com/docs/installation/)
4. [Streamlit Community Cloud docs: deploy your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app)
5. <a href="https://clauswilke.com/dataviz/">Fundamentals of Data Visualization by Claus O. Wilke</a>
6. <a href="https://www.amazon.com/Visualization-Analysis-Design-AK-Peters/dp/1466508914/">Visualization Analysis & Design, Tamara Munzner</a>. Many concepts found on [the book's webpage](https://www.cs.ubc.ca/~tmm/vadbook/) and the [associated lecture slides](https://www.cs.ubc.ca/~tmm/talks.html#vadallslides).

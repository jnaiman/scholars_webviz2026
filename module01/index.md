---
layout: week
icon: undraw_professor_d7zn.svg
visible: true
notitle: true
examples:
  - filename: setup_instructions.html
    type: link
    title: Setup Instructions
    description: Step-by-step setup (all in your browser, nothing to install), plus troubleshooting.
  - filename: colab_test
    type: colab
    title: Test-your-setup notebook (open in Google Colab)
    description: Checks your packages, makes your first Altair plot, and saves it as a JSON file.
    link: module01/test_install.ipynb
  - filename: test_install.ipynb
    type: ipynb
    title: Test-your-setup notebook (view on this site)
    description: The same notebook, to read without running it.
  - filename: cv_template
    type: iodide
    title: Online CV (Jekyll) template
    description: The template for your github.io site (see its README for details on every file).
    link: https://github.com/jnaiman/online_cv_public_fa2026
---

{% assign cv = site.data.class.urls | where: "id", "cv_template" | first %}

# Introduction & Setup

This module covers an introduction to the workshop and your instructor, and gets you set up with:

* a **GitHub** account and a personal website at `<your-username>.github.io` built from the [online CV template]({{ cv.url }}), and
* **Google Colab** for writing Python and making Altair plots.

**Everything happens in your web browser -- there is nothing to install.** (If you'd like to work on your own computer after the workshop, [Module 6]({{site.baseurl}}/module06/) walks through installing everything.)

**Please try to do the steps in [Lecture 1.0](lecture01p0.html) / the [Setup Instructions](setup_instructions.html) before the workshop.**

### Optional Materials and Resources
1. Who is [your instructor](https://www.astronaiman.com/) anyway?
2. [GitHub Pages quickstart](https://docs.github.com/en/pages/quickstart) and [GitHub's "Hello World" tutorial](https://docs.github.com/en/get-started/start-your-journey/hello-world)
3. [Google Colab's welcome notebook](https://colab.research.google.com/notebooks/intro.ipynb)
4. <a href="https://clauswilke.com/dataviz/">Fundamentals of Data Visualization by Claus O. Wilke</a>
5. <a href="https://www.amazon.com/Visualization-Analysis-Design-AK-Peters/dp/1466508914/">Visualization Analysis & Design, Tamara Munzner</a>. Many concepts found on [the book's webpage](https://www.cs.ubc.ca/~tmm/vadbook/) and the [associated lecture slides](https://www.cs.ubc.ca/~tmm/talks.html#vadallslides).

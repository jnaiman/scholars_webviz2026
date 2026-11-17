---
title: Lecture 1.0 - Setup Part 1, Installing Our Tools
layout: lecture
tags:
  - installations
  - setup
description: >-
  Pre-workshop: accounts to make and software to install (or the browser-only option).
date: 2026-12-01
---

<br/><br/><br/>
# Setup Part 1: Installing Our Tools

notes:
raise of hands -- who has used Python before? GitHub? Who has a website?

this is the "pre-workshop" setup -- ideally done before we start, but we'll walk around and help

---

## Where we are going

By the end of this workshop you'll have:

1. A **personal website** at `https://<your-username>.github.io` with **interactive plots** on it
2. A **web app** at `https://<your-app>.streamlit.app` that anyone can use

Both are **free** to host.

notes:
two "products" -- a website (Jekyll + Altair, Module 3) and an app (Streamlit, Module 4)

---

## The tools

| Tool | What it does | Module |
|---|---|---|
| **Python** + [Altair](https://altair-viz.github.io/) | Makes interactive plots | 3, 4 |
| [GitHub](https://github.com/) | Stores your files, hosts your website | 1, 3, 4 |
| [Jekyll](https://jekyllrb.com/) | Turns Markdown files into a website | 3 |
| [Streamlit](https://streamlit.io/) | Turns a Python script into a web app | 4 |
| [Streamlit Community Cloud](https://share.streamlit.io/) | Hosts your Streamlit app | 4 |

notes:
don't worry about memorizing this -- we'll meet each of these as we go

---

## Two ways to do this workshop

| | **Track A: install on my computer** | **Track B: browser only** |
|---|---|---|
| Python | JupyterLab (Miniconda) | [Google Colab](https://colab.research.google.com/) |
| Website | Preview locally, then `git push` | Upload files on github.com |
| App | `streamlit run` locally, then `git push` | Edit files on github.com |
| Install | Miniconda, git, Ruby + Jekyll | Nothing! |

You can mix and match!

notes:
track A is faster once it's set up (you see changes instantly on your own computer) and is what you'd want if you keep building things after the workshop

track B works on any computer with a browser -- good for locked-down work laptops, or if installs are being difficult today

**everything we do today works in both tracks**

---

## Full instructions

Everything on these slides (plus troubleshooting) is on the [Installation & Setup Instructions page](COURSE_WEBPAGE/module01/installation_instructions.html).

notes:
**open this page and show the contents list and the Troubleshooting section at the bottom**

---

## Step 1: Accounts (everyone)

1. **GitHub**: [github.com/signup](https://github.com/signup)
   * your username becomes your website: `<username>.github.io`

notes:
pick a username you'd be ok putting on a CV!

---

## Step 1: Accounts (everyone)

1. **GitHub**: [github.com/signup](https://github.com/signup)
   * your username becomes your website: `<username>.github.io`
2. **Streamlit Community Cloud**: [share.streamlit.io](https://share.streamlit.io/) → "Continue with GitHub"

<img src="images/streamlit_setup/continue_with_github.png" width="35%" style="border: 1px solid black;" alt="The Streamlit sign-in page with a 'Continue with GitHub' button.">

notes:
streamlit cloud reads your GitHub repositories to build apps, so we link the two accounts

---

## Step 1: Accounts (everyone)

1. **GitHub**: [github.com/signup](https://github.com/signup)
   * your username becomes your website: `<username>.github.io`
2. **Streamlit Community Cloud**: [share.streamlit.io](https://share.streamlit.io/) → "Continue with GitHub"
3. **Track B only**: a Google account for [Google Colab](https://colab.research.google.com/)

notes:
colab is Google's free online Jupyter notebook -- altair and pandas are already installed there

---

## Step 2 (Track A): Python with Miniconda

1. Install **Miniconda**: [anaconda.com/download/success](https://www.anaconda.com/download/success) (scroll to "Miniconda Installers")
2. Open **Terminal** (Mac) or **Anaconda Prompt** (Windows)

notes:
conda keeps the packages for this workshop in their own "environment" so they don't mess with anything else on your computer

windows folks -- Anaconda Prompt, not Command Prompt!

---

## Step 2 (Track A): Python with Miniconda

1. Install **Miniconda**: [anaconda.com/download/success](https://www.anaconda.com/download/success) (scroll to "Miniconda Installers")
2. Open **Terminal** (Mac) or **Anaconda Prompt** (Windows)
3. Create the `webviz` environment:

```bash
conda create -n webviz -c conda-forge python=3.12 altair=5.5 vega_datasets pandas numpy matplotlib jupyterlab pip ; conda activate webviz ; pip install streamlit
```

(or use the [environment.yml](COURSE_GITHUB/raw/main/module01/env_files/environment.yml) file: `conda env create -f environment.yml`)

notes:
this one takes a few minutes -- start it now while we talk

why altair 5.5? the website template draws plots with vega-lite 5, altair 6 writes vega-lite 6 files

---

## Step 2 (Track A): Python with Miniconda

1. Install **Miniconda**: [anaconda.com/download/success](https://www.anaconda.com/download/success) (scroll to "Miniconda Installers")
2. Open **Terminal** (Mac) or **Anaconda Prompt** (Windows)
3. Create the `webviz` environment (see above)
4. **Every time** you open a new Terminal: `conda activate webviz`

Your prompt should start with `(webviz)`.

notes:
this is the #1 thing people forget!  if something says "module not found" -- check for (webviz)

---

## Step 2 (Track B): Google Colab

Open the [test notebook in Colab](COURSE_COLAB/module01/test_install.ipynb) → **Runtime → Run all**

notes:
if colab warns "this notebook was not authored by Google" -- click "Run anyway"

colab files disappear when you close it -- use File → Save a copy in Drive, and download any files you make

---

## Step 2: Test it (everyone)

The [test notebook](COURSE_WEBPAGE/nbv.html?notebook_name=COURSE_WEBPAGE/module01/test_install.ipynb):
* imports `pandas` and `altair`
* reads a dataset from the web
* makes an interactive plot
* saves it as `my_first_chart.json`

**Track A:** download it, run `jupyter lab`, open it, Run All.

**Track B:** [open it in Colab](COURSE_COLAB/module01/test_install.ipynb), Runtime → Run all.

notes:
if you see a plot at the end you're good to go!

we'll use that json file in Module 3 -- it's how plots get onto websites

---

## Step 3 (Track A): git

* **Mac:** `xcode-select --install`
* **Windows:** [Git for Windows](https://git-scm.com/downloads/win)

Then tell git who you are:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

notes:
git is how we send files from our computer to GitHub

when you push the first time you'll be asked to log in -- Windows opens a browser; Mac asks for a "password", which needs to be a personal access token (see install page)

---

## Step 3 (Track A): Ruby & Jekyll

Follow the official guide for your system **all the way to the end**:

* [Mac](https://jekyllrb.com/docs/installation/macos/)
* [Windows](https://jekyllrb.com/docs/installation/windows/) (use **Ruby+Devkit 3.4.x**, not 4.0)
* [Ubuntu](https://jekyllrb.com/docs/installation/ubuntu/) / [Other Linux](https://jekyllrb.com/docs/installation/other-linux/)

Then: `gem install jekyll bundler`

notes:
this is the step most likely to give trouble, so start early!

Mac: after brew and chruby install they print "next steps" -- you must run those lines and re-open Terminal

check with `ruby -v` (should be 3.3 or 3.4, NOT 2.6 which is the Mac's built-in one)

---

## Step 3 (Track A): Ruby & Jekyll

Follow the official guide for your system **all the way to the end**:

* [Mac](https://jekyllrb.com/docs/installation/macos/)
* [Windows](https://jekyllrb.com/docs/installation/windows/) (use **Ruby+Devkit 3.4.x**, not 4.0)
* [Ubuntu](https://jekyllrb.com/docs/installation/ubuntu/) / [Other Linux](https://jekyllrb.com/docs/installation/other-linux/)

Then: `gem install jekyll bundler`

Stuck? Check the [Troubleshooting section](COURSE_WEBPAGE/module01/installation_instructions.html#troubleshooting), or switch to Track B for the website for today!

notes:
no shame in switching tracks -- you can always install later and pick up where you left off, since your site lives on GitHub either way

---

## Optional: VS Code

[VS Code](https://code.visualstudio.com/download) -- a free editor with files, a Terminal and Markdown preview in one window.

Any text editor works though!

notes:
we'll set up the website and app themselves in Lecture 1.2, after a bit of an intro

**walk around and help with installs**

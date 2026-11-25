---
title: Lecture 6.1 - Installing the Tools Locally
layout: lecture
tags:
  - installations
  - setup
  - optional
description: >-
  Optional: install Miniconda (Python), git, Ruby and Jekyll on your own computer.
date: 2026-12-11
---

<br/><br/><br/>
# Installing the Tools Locally

notes:
this whole module is optional -- everything in the workshop works in the browser

it's for folks who want to keep building websites and apps afterwards

---

## Why install anything?

| | In the browser | On your computer |
|---|---|---|
| Python | Google Colab | JupyterLab (Miniconda) |
| Website | Upload on github.com, wait 1-2 min | `jekyll serve`: see changes instantly, then `git push` |
| App | Edit on github.com, wait for rebuild | `streamlit run`: see changes instantly, then `git push` |

notes:
the big win is the fast edit loop -- save, refresh, see it -- and only putting things online when they work

your site and app live on GitHub either way, so you can switch any time

---

## Full instructions

Everything on these slides (plus troubleshooting) is on the [Installing Everything Locally page](COURSE_WEBPAGE/module06/installation_instructions.html).

notes:
**open this page and show the contents list and the Troubleshooting section at the bottom**

---

## Step 1: Python with Miniconda

1. Install **Miniconda**: [anaconda.com/download/success](https://www.anaconda.com/download/success) (scroll to "Miniconda Installers")
2. Open **Terminal** (Mac) or **Anaconda Prompt** (Windows)

notes:
conda keeps the packages for this workshop in their own "environment" so they don't mess with anything else on your computer

windows folks -- Anaconda Prompt, not Command Prompt!

---

## Step 1: Python with Miniconda

1. Install **Miniconda**: [anaconda.com/download/success](https://www.anaconda.com/download/success) (scroll to "Miniconda Installers")
2. Open **Terminal** (Mac) or **Anaconda Prompt** (Windows)
3. Create the `webviz` environment:

```bash
conda create -n webviz -c conda-forge python=3.12 altair=6 vega_datasets pandas numpy matplotlib jupyterlab pip ; conda activate webviz ; pip install streamlit
```

(or use the [environment.yml](COURSE_GITHUB/raw/main/module06/env_files/environment.yml) file: `conda env create -f environment.yml`)

notes:
this one takes a few minutes

we use altair 6 -- if you already have altair 5 from another class, the test notebook will tell you how to upgrade

---

## Step 1: Python with Miniconda

1. Install **Miniconda**: [anaconda.com/download/success](https://www.anaconda.com/download/success) (scroll to "Miniconda Installers")
2. Open **Terminal** (Mac) or **Anaconda Prompt** (Windows)
3. Create the `webviz` environment (see above)
4. **Every time** you open a new Terminal: `conda activate webviz`

Your prompt should start with `(webviz)`.

notes:
this is the #1 thing people forget!  if something says "module not found" -- check for (webviz)

---

## Step 1: Test it

1. Download the [test notebook](COURSE_RAW/module01/test_install.ipynb) (right click → "Save link as...")
2. `jupyter lab` → open it → **Run → Run All Cells**
3. `streamlit hello` → a demo app opens (`CTRL+C` to stop)

notes:
same test notebook as Module 1 -- if you see a plot at the end, Python is good to go

---

## Step 2: git

* **Mac:** `xcode-select --install`
* **Windows:** [Git for Windows](https://git-scm.com/downloads/win)

Then tell git who you are:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

notes:
git is how we send files from our computer to GitHub -- instead of "Upload files"

when you push the first time you'll be asked to log in -- Windows opens a browser; Mac asks for a "password", which needs to be a personal access token (see install page)

---

## Step 3: Ruby & Jekyll

Follow the official guide for your system **all the way to the end**:

* [Mac](https://jekyllrb.com/docs/installation/macos/)
* [Windows](https://jekyllrb.com/docs/installation/windows/) (use **Ruby+Devkit 3.4.x**, not 4.0)
* [Ubuntu](https://jekyllrb.com/docs/installation/ubuntu/) / [Other Linux](https://jekyllrb.com/docs/installation/other-linux/)

Then: `gem install jekyll bundler`

notes:
this is the step most likely to give trouble, so give yourself time!

Mac: after brew and chruby install they print "next steps" -- you must run those lines and re-open Terminal

check with `ruby -v` (should be 3.3 or 3.4, NOT 2.6 which is the Mac's built-in one)

---

## Step 3: Ruby & Jekyll

```bash
ruby -v      # 3.3.x or 3.4.x
jekyll -v    # a version number
```

Stuck? Check the [Troubleshooting section](COURSE_WEBPAGE/module06/installation_instructions.html#troubleshooting).

notes:
no rush -- keep using the browser for your site while you sort out Ruby; nothing is lost

---

## Optional: VS Code

[VS Code](https://code.visualstudio.com/download) -- a free editor with files, a Terminal and Markdown preview in one window.

Same editor as github.dev, so it'll look familiar!

notes:
any text editor works though

next: using all of this on your website and app (Lecture 6.2)

---
title: Lecture 1.0 - Setup Part 1, Accounts & Google Colab
layout: lecture
tags:
  - setup
  - accounts
  - colab
description: >-
  Pre-workshop: make your free accounts and test Google Colab. Nothing to install!
date: 2026-12-01
---

<br/><br/><br/>
# Setup Part 1: Accounts & Google Colab

notes:
raise of hands -- who has used Python before? GitHub? Who has a website?

this is the "pre-workshop" setup -- ideally done before we start, but we'll walk around and help

---

## Where we are going

By the end of this workshop you'll have:

1. A **personal website** at `https://<your-username>.github.io` with **interactive plots** on it (Modules 1-3)
2. A **web app** at `https://<your-app>.streamlit.app` that anyone can use (Module 4)

Both are **free** to host.

notes:
two "products" -- a website (Jekyll + Altair) and an app (Streamlit)

each one is self-contained: we finish the website completely before starting on the app

---

## Everything happens in your browser

| Tool | What it does | Module |
|---|---|---|
| [GitHub](https://github.com/) | Stores your files, hosts your website | 1, 3, 4 |
| [Google Colab](https://colab.research.google.com/) | Runs Python + [Altair](https://altair-viz.github.io/) to make interactive plots | 1, 3 |
| [Jekyll](https://jekyllrb.com/) | Turns Markdown files into a website (GitHub runs it for you) | 1, 3 |
| [Streamlit Community Cloud](https://share.streamlit.io/) | Runs your Streamlit app | 4 |

**Nothing to install!**

notes:
don't worry about memorizing this -- we'll meet each of these as we go

want to install everything on your own computer later? Module 6 walks through it -- but you don't need it today

---

## Full instructions

Everything on these slides (plus troubleshooting) is on the [Setup Instructions page](COURSE_WEBPAGE/module01/setup_instructions.html).

notes:
**open this page and show the contents list and the Troubleshooting section at the bottom**

---

## Step 1: A GitHub account

[github.com/signup](https://github.com/signup)

Your username becomes your website: **`<username>.github.io`**

notes:
pick a username you'd be ok putting on a CV!

already have one? great, use it

---

## Step 2: A Google account for Colab

Any Google account works for [Google Colab](https://colab.research.google.com/) -- Google's free online Jupyter notebooks.

Altair and pandas are already installed there.

notes:
some university Google accounts have Colab turned off -- a personal gmail account always works

---

## Step 3: Test it

Open the [test notebook in Colab](COURSE_COLAB/module01/test_install.ipynb) → **Runtime → Run all**

It:
* imports `pandas` and `altair`
* reads a dataset from the web
* makes an interactive plot
* saves it as `my_first_chart.json`

notes:
if colab warns "this notebook was not authored by Google" -- click "Run anyway"

if you see a plot at the end you're good to go!

we'll use that json file idea in Module 3 -- it's how plots get onto websites

---

## Colab tips

* Files you make **disappear** when you close Colab → download them (📁 folder icon on the left → right click → Download)
* Want to keep your notebook? **File → Save a copy in Drive**

notes:
we'll make a handful of .json files in Module 3 -- the Module 3 notebook has a cell that zips them all up and downloads them for you

---

## (Optional) Step 4: A Streamlit account

[share.streamlit.io](https://share.streamlit.io/) → "Continue with GitHub"

We'll do this together at the start of **Module 4**, but you can do it now too.

notes:
streamlit cloud reads your GitHub repositories to build apps, so we link the two accounts

we'll set up the website itself in Lecture 1.2, after a bit of an intro

---
title: Lecture 4.3 - Hosting Your App on Streamlit Community Cloud
layout: lecture
tags:
  - streamlit
  - github
  - hosting
  - hands-on
description: >-
  Putting your own app online with Streamlit Community Cloud by uploading and editing files on GitHub, and fixing problems.
date: 2026-12-09
---

<br/><br/><br/>
# Hosting Your App on Streamlit Community Cloud

notes:
we deployed the starter repo in Lecture 4.1 -- now let's put the full starter app (or OUR app) there

---

## Streamlit Community Cloud

[share.streamlit.io](https://share.streamlit.io/) runs your app for free from a **public GitHub repository**.

<img src="images/streamlitiointro.png" width="70%" style="border: 1px solid black;" alt="The landing page of Streamlit Community Cloud.">

notes:
free for public apps -- your code AND your app are public, so don't put private data in them

---

## What it needs

A **public GitHub repo** (or a folder in one) with:

```
streamlit_app.py      <- your app
requirements.txt      <- one package per line
(any data / .json files your app reads)
```

```
streamlit
altair>=6,<7
pandas
```

notes:
requirements.txt is how Streamlit Cloud knows what to install -- forget a package and you get ModuleNotFoundError

---

## Upload in the browser

1. Download the [starter files](COURSE_GITHUB/tree/main/module04/streamlit_starter) (⬇️ "Download raw file" on each)
2. Your Lecture 4.1 repo (or a new **public** one) → **Add file → Upload files** → **Commit changes**
   * uploading `streamlit_app.py` **replaces** the old one
3. The app rebuilds by itself!

notes:
if you deployed the forked starter in Lecture 4.1, just upload into that same repo -- no need to create a new app

---

## Edit in the browser

On GitHub: open `streamlit_app.py` → ✏️ → edit → **Commit changes** → refresh your app

Bigger edits: press **`.`** on your repo's page to open [github.dev](https://github.dev), a VS Code editor in the browser.

notes:
github.dev can't *run* the app, but it's a much nicer editor; your live app is your "preview"

tip: keep the app open in one tab and GitHub in another

---

## New app or new location?

**Create app** → **Deploy a public app from GitHub**

<img src="images/streamlit_setup/deploy_mod.png" width="50%" style="border: 1px solid black;" alt="The 'Deploy an app' form with Repository, Branch, Main file path and App URL fields and a Deploy button.">

App in a folder? Main file path = `folder/streamlit_app.py`

notes:
so the app files can live anywhere -- a dedicated repo, or a folder inside your github.io repo

you can have several apps from one repo, each pointing at a different file

---

## When things go wrong

* App shows an error → **Manage app** (bottom right) → read the logs
* `ModuleNotFoundError` → add the package to `requirements.txt`
* `FileNotFoundError` → is every data/`.json` file uploaded, next to `streamlit_app.py`?
* Stuck on an old version → ⋮ menu → **Reboot app**

notes:
most errors are a missing package or a missing file

---

## Sharing your app

* The URL: `https://<your-app>.streamlit.app`
* **Settings → Sharing**: public (default) or invite specific people
* Explore others' apps: [Streamlit gallery](https://streamlit.io/gallery)

<img src="images/explorestreamlit.png" width="55%" style="border: 1px solid black;" alt="The Streamlit gallery page showing a grid of community apps.">

notes:
want a faster edit loop, running the app on your own computer first? see Module 6 (optional)

next: linking your app and your website together (Module 5)

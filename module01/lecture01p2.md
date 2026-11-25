---
title: Lecture 1.2 - Setup Part 2, Your github.io Website
layout: lecture
tags:
  - setup
  - github
  - jekyll
description: >-
  Put the Jekyll template on your github.io site, all in the browser.
date: 2026-12-03
---

<br/><br/><br/>
# Setup Part 2: Your github.io Website

notes:
now that we have accounts let's set up our "home on the web"

we'll fill it with interactive plots in Module 3

---

## Your github.io website

[GitHub Pages](https://pages.github.com/) hosts a website for free from a GitHub repository named:

### `<your-username>.github.io`

notes:
the name is very specific!  it has to be exactly your username plus .github.io, all lowercase

---

## The template

We'll start from an [online CV template](CV_TEMPLATE) with interactive plots built in.

<img src="images/jekyll_setup/jekyllWorking2025_line.png" width="65%" style="border: 1px solid black;" alt="The template website: an 'IS445 Jekyll Template' title, Projects/Blog/About links, and a round photo of a corgi with the text 'I am definitely not a corgi!'">

notes:
it has an About page (skills + timeline), a Projects page (where our plots will go) and an optional blog

the screenshot says IS445 -- this is the same template that course uses

---

## 1. Create the repository

1. GitHub → **+** → **New repository**
2. Name: **`<your-username>.github.io`**
3. **Public**
4. Tick **"Add a README file"**
5. **Create repository**

notes:
**demo this live**

the README just makes the repository non-empty, so the "Upload files" button shows up

---

## 2. Download the template

[⬇️ Download the template zip](CV_TEMPLATE_ZIP), then unzip it.

You'll copy **everything inside** `online_cv_public_fa2026-main` (not the folder itself) into your repository.

notes:
the most common mistake: uploading the whole folder, so your site lives at github.io/online_cv_public_fa2026-main -- we want the files at the top level

---

## 3. Upload in the browser

**Add file → Upload files**, drag in the contents of the template folder.

GitHub accepts **100 files per upload**, so do **two batches**:
1. the folders starting with `_` → **Commit changes**
2. everything else → **Commit changes**

notes:
**demo this live** -- the "_" folders first is just a convenient way to split it in two

hidden files like .gitignore may not upload -- that's fine

---

## 4. Turn on GitHub Pages

**Settings → Pages** → "Deploy from a branch", `main`, `/ (root)` → **Save**

Then watch the **Actions** tab:

<img src="images/jekyll_setup/actionsBuilding_line.png" width="70%" style="border: 1px solid black;" alt="The GitHub Actions tab with a 'pages build and deployment' workflow run shown with a yellow 'in progress' circle.">

notes:
yellow = building, green = done, red = error (click it to see why)

then go to https://<you>.github.io -- you should see the corgi!

---

## 5. Make it yours

On GitHub, click `_config.yml` → ✏️ and edit "PART 1" at the top:

```yaml
title               : Your Name -- Portfolio
repository          : your-github-username
author:
  name              : Your Name
```

→ **Commit changes** → watch the Actions tab → refresh your site

notes:
this is the edit loop for the whole workshop: edit on GitHub, commit, wait a minute, refresh

more on all the template's files in Module 3 (and in the template's README)

---

## Bigger edits: github.dev

On your repository's page, press the **`.`** key → [github.dev](https://github.dev) opens: a full editor (VS Code) in your browser.

Edit several files, then **Source Control** (left bar) → message → **Commit & Push**.

notes:
nice when you're changing more than one file at a time -- github.dev can't build the site, so your live github.io site is your "preview"

---

## Option: a different repository

Already using `<you>.github.io`? Put the template in **any** public repo (e.g. `webviz_portfolio`):

1. `_config.yml`: `baseurl: "/webviz_portfolio"`
2. Turn on Pages (same as step 4)

Site: `https://<you>.github.io/webviz_portfolio`

notes:
this is also how this workshop's own site works -- baseurl is the repo name

---

## Checklist

- [ ] `https://<you>.github.io` shows the template with your name
- [ ] The Colab test notebook ran and drew a plot

Want to preview your site on your own computer instead? That's [Module 6](COURSE_WEBPAGE/module06/) -- optional, and not needed today.

notes:
if both work, we're ready for Modules 2 & 3!

**pause for questions / help**

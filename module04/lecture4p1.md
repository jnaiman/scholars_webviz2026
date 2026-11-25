---
title: Lecture 4.1 - Your First Streamlit App
layout: lecture
tags:
  - streamlit
  - github
  - setup
  - hands-on
description: >-
  Make a Streamlit Community Cloud account and deploy a first app from GitHub, all in the browser.
date: 2026-12-07
---

<br/><br/><br/>
# Your First Streamlit App

notes:
modules 1-3 gave us a finished website.  now a second, separate tool: an "app" where Python runs when people use it

everything we need for this module is set up right here -- all you need is your GitHub account

---

## Where we are going

A **web app** at `https://<your-app>.streamlit.app` that anyone can use:

* [Streamlit](https://streamlit.io/) turns a Python script into a web app
* [Streamlit Community Cloud](https://share.streamlit.io/) runs it for free

notes:
today: get a first app online (this lecture), learn how to build one (4.2), then put our own app online (4.3)

---

## An app is two files

In a **public GitHub repository**:

* `streamlit_app.py` -- your Python code
* `requirements.txt` -- the packages to install (`streamlit`, `altair`, ...)

notes:
streamlit community cloud reads these from github and runs the app for you

---

## 1. Make a Streamlit account

[share.streamlit.io](https://share.streamlit.io/) → **"Continue with GitHub"**

<img src="images/streamlit_setup/continue_with_github.png" width="35%" style="border: 1px solid black;" alt="The Streamlit sign-in page with a 'Continue with GitHub' button.">

notes:
streamlit cloud reads your GitHub repositories to build apps, so we link the two accounts -- click "Authorize" when GitHub asks

---

## 2. Get the starter files on GitHub

Pick one:
* **Fork** the [starter repo](STREAMLIT_TEMPLATE) (easiest)
* **Upload** the [workshop's starter files](COURSE_GITHUB/tree/main/module04/streamlit_starter) to a new public repo (Add file → Upload files)
* Put them in a **folder** of any public repo you already have

---

## 2. Forking

<img src="images/streamlit_setup/fork_template.png" width="70%" style="border: 1px solid black;" alt="The starter repository's GitHub page with the 'Fork' button at the top right highlighted.">

notes:
fork = your own copy of somebody else's repository

---

## 2. Forking

<img src="images/streamlit_setup/create_fork.png" width="60%" style="border: 1px solid black;" alt="GitHub's 'Create a new fork' page with an owner dropdown and a repository name box, and a green 'Create fork' button.">

Give it a name like `webviz_streamlit` → **Create fork**

notes:
screenshot shows the IS445 name -- name yours whatever you like

---

## 3. Deploy on Streamlit Community Cloud

[share.streamlit.io](https://share.streamlit.io/) → **Create app**

<img src="images/streamlit_setup/create_app.png" width="70%" style="border: 1px solid black;" alt="The Streamlit Community Cloud workspace with the 'Create app' button at the top right.">

---

## 3. Deploy on Streamlit Community Cloud

**"Deploy a public app from GitHub"**

<img src="images/streamlit_setup/deploy_github.png" width="60%" style="border: 1px solid black;" alt="Streamlit's 'What would you like to do?' page with the option 'Deploy a public app from GitHub' highlighted.">

---

## 3. Deploy on Streamlit Community Cloud

<img src="images/streamlit_setup/deploy_mod.png" width="60%" style="border: 1px solid black;" alt="The 'Deploy an app' form: Repository jnaiman/is445_demo, Branch main, Main file path streamlit_app.py, App URL jnaiman-is445-lab8.streamlit.app with 'Domain is available', and a blue Deploy button.">

Repository, branch `main`, main file `streamlit_app.py` (or `folder/streamlit_app.py`), and an App URL → **Deploy**

notes:
first build takes a few minutes

---

## Your app is live!

<img src="images/streamlit_setup/initial_deploy.png" width="70%" style="border: 1px solid black;" alt="The deployed starter app at its .streamlit.app address, showing a title and an interactive Seattle weather chart.">

notes:
share the URL with a neighbor!

---

## 4. Make an edit

On GitHub: open `streamlit_app.py` → ✏️ → change the text in `st.title(...)` → **Commit changes** → refresh your app

Streamlit Cloud rebuilds the app **every time the repository changes**.

notes:
this is the edit loop for the rest of the module: edit on GitHub, commit, refresh the app

---

## Checklist

- [ ] `https://<your-app>.streamlit.app` shows the starter app
- [ ] Your edit to `st.title(...)` shows up

Want to run apps on your own computer instead? That's [Module 6](COURSE_WEBPAGE/module06/) -- optional, and not needed today.

notes:
next: how a streamlit app actually works

**pause for questions / help**

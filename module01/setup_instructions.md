---
title: Setup Instructions
layout: default
notitle: true
description: >-
  Everything to set up before (or during) the workshop. It all happens in your
  web browser, so there is nothing to install.
---

{% assign cv = site.data.class.urls | where: "id", "cv_template" | first %}
{% assign colab = "https://colab.research.google.com/github/" | append: site.githuburlbase | append: site.baseurl | append: "/blob/" | append: site.branch %}

# Setup Instructions

By the end of the workshop you will have:

1. **A personal website** at `https://<your-username>.github.io` built with [Jekyll](https://jekyllrb.com/), with interactive [Altair](https://altair-viz.github.io/) plots on it (Modules 1-3).
2. **A Streamlit app** at `https://<your-app-name>.streamlit.app` hosted for free on [Streamlit Community Cloud](https://streamlit.io/cloud) (Module 4).

**Everything in the workshop happens in your web browser -- there is nothing to install.** We write Python in [Google Colab](https://colab.research.google.com/) and upload/edit files directly on [github.com](https://github.com/). (Want to install everything on your own computer instead, for after the workshop? See [Module 6]({{site.baseurl}}/module06/). It is optional.)

The slides for [Lecture 1.0]({{site.baseurl}}/module01/lecture01p0.html) and [Lecture 1.2]({{site.baseurl}}/module01/lecture01p2.html) walk through the same steps with screenshots.

**Please try to do Steps 1-3 before the workshop.** We'll do Step 4 together in Module 1, but you're welcome to get a head start.

Contents:
1. [Step 1: Make a GitHub account](#step-1-make-a-github-account)
2. [Step 2: Make sure you can use Google Colab](#step-2-make-sure-you-can-use-google-colab)
3. [Step 3: Run the test notebook](#step-3-run-the-test-notebook)
4. [Step 4: Put the Jekyll template on your github.io site](#step-4-put-the-jekyll-template-on-your-githubio-site)
5. [Coming up in Module 4: a Streamlit account](#coming-up-in-module-4-a-streamlit-account)
6. [Troubleshooting](#troubleshooting)

---

## Step 1: Make a GitHub account

Sign up for a free account at [github.com/signup](https://github.com/signup).

* Your username becomes your website address (`<your-username>.github.io`), so pick something you are happy to put on a CV.
* If you already have a GitHub account *and* already use `<your-username>.github.io` for something else, see [Hosting in a different repository](#option-host-the-template-in-a-different-repository) below.

---

## Step 2: Make sure you can use Google Colab

[Google Colab](https://colab.research.google.com/) runs Jupyter notebooks in your browser, for free, with Altair and pandas already installed. Any Google account works. Go to [colab.research.google.com](https://colab.research.google.com/) and sign in.

> Some university Google accounts have Colab turned off. If yours does, a personal Gmail account always works.

---

## Step 3: Run the test notebook

1. Open the test notebook directly in Colab: **[open test_install.ipynb in Colab]({{ colab }}/module01/test_install.ipynb)**.
2. Click **Runtime → Run all**. (If Colab warns "This notebook was not authored by Google", click "Run anyway".)
3. The last cells draw an interactive plot and save it to a file called `my_first_chart.json`. Click the **folder icon** in Colab's left sidebar to see the file; right click → **Download** to save it to your computer.

If you see the plot, you're done with Python setup.

> Colab notebooks are temporary. To keep your work, use **File → Save a copy in Drive**. Files you create (like the JSONs) disappear when the session ends, so download them as you go.

---

## Step 4: Put the Jekyll template on your github.io site

We'll use the **[online CV template]({{ cv.url }})**, a Jekyll site with an About page, a Projects page, and support for interactive vega-lite/Altair plots built in. Its [README]({{ cv.url }}#readme) has more detail on every file.

### 4.1 Create your github.io repository

1. On GitHub, click **+** (top right) → **New repository**.
2. Name it **exactly** `<your-username>.github.io` (e.g. `jnaiman.github.io`). Any other name won't work as your main site -- watch for typos and capital letters.
3. Make it **Public**, tick **"Add a README file"**, and click **Create repository**.

### 4.2 Download the template

[⬇️ Download the template as a zip file]({{ cv.url }}/archive/refs/heads/main.zip) and unzip it. You get a folder called `online_cv_public_fa2026-main`. You'll copy **everything inside** that folder (not the folder itself) into your repository.

### 4.3 Upload the files in the browser

1. On your repository's GitHub page click **Add file → Upload files**.
2. Drag in the files and folders from **inside** `online_cv_public_fa2026-main`. GitHub only accepts **100 files per upload** and the template has a few more than that, so do it in **two batches**: first the folders whose names start with `_`, click **Commit changes**; then everything else, **Commit changes** again.

> If your computer hides files that start with a `.` (like `.gitignore`), that's fine -- the site works without them.

### 4.4 Turn on GitHub Pages and check the build

1. In your repository go to **Settings → Pages**. Under "Build and deployment" set **Source: Deploy from a branch**, **Branch: `main`**, folder **`/ (root)`**, and **Save**.
2. Click the **Actions** tab. A yellow circle means the site is building; it turns green after a minute or two (red means an error -- see [Troubleshooting](#troubleshooting)).
3. Go to `https://<your-username>.github.io`. You should see the template's About page with a corgi. (A 404 page right after a change usually just means "wait another minute".)

### 4.5 Make it yours (a first edit)

On GitHub, click `_config.yml` and then the ✏️ pencil icon. In "PART 1" change:

* `title:` -- e.g. `Your Name -- Portfolio`
* `repository:` -- your GitHub username (e.g. `jnaiman`)
* `author: name:` -- your name

Click **Commit changes**, watch the Actions tab, then refresh your site.

> **Editing several files at once?** On your repository's page press the **`.`** key to open [github.dev](https://github.dev), a full code editor in your browser. Edit as many files as you like, then use **Source Control** (left bar) → type a message → **Commit & Push**.

### Option: host the template in a different repository

Already using your `<your-username>.github.io` for something else, or want to keep this separate? Put the template in **any** public repository (say `webviz_portfolio`), then:

1. In `_config.yml` set `baseurl: "/webviz_portfolio"` (a slash plus your repository's name).
2. Turn on Pages as in 4.4.

Your site will be at `https://<your-username>.github.io/webviz_portfolio`.

---

## Coming up in Module 4: a Streamlit account

In Module 4 we'll sign in to [Streamlit Community Cloud](https://share.streamlit.io/) with "Continue with GitHub" and deploy an app. We'll do it together, so there's nothing to do now -- but you're welcome to make the account early.

---

## Troubleshooting

<details><summary><strong>github.io shows a 404 or an old version</strong></summary>
<ul>
<li>Wait 1-2 minutes and refresh -- check the <b>Actions</b> tab for the yellow/green circle.</li>
<li>Check <b>Settings → Pages</b> is set to "Deploy from a branch", <code>main</code>, <code>/ (root)</code>.</li>
<li>Check the repository name is exactly <code>&lt;your-username&gt;.github.io</code>, all lowercase.</li>
<li>Check the files are at the <b>top level</b> of the repository (you should see <code>_config.yml</code> on the repository's front page), not inside an <code>online_cv_public_fa2026-main</code> folder.</li>
<li>Hard-refresh your browser (<code>Cmd+Shift+R</code> / <code>Ctrl+Shift+R</code>).</li>
</ul>
</details>

<details><summary><strong>The Actions tab shows a red ✗</strong></summary>
<p>Click the failed run, then the failed step, to read the error. The most common cause is a typo in <code>_config.yml</code> or in a project's front matter (the settings between the <code>---</code> lines) -- YAML is picky about spaces after colons and about indentation. Undo your last change and try again.</p>
</details>

<details><summary><strong>Liquid Exception mentioning "repository" or "PAGES_REPO_NWO"</strong></summary>
<p>Open <code>_config.yml</code> and set <code>repository:</code> to your GitHub username (e.g. <code>repository: jnaiman</code>), then commit.</p>
</details>

<details><summary><strong>"Upload files" only takes some of my files</strong></summary>
<p>GitHub accepts at most 100 files per upload. Upload in smaller batches (e.g. one or two folders at a time), clicking <b>Commit changes</b> after each.</p>
</details>

<details><summary><strong>Colab: "ModuleNotFoundError"</strong></summary>
<p>Add a cell at the top with <code>%pip install &lt;package&gt;</code> and run it first. Altair and pandas are already installed in Colab.</p>
</details>

<details><summary><strong>Colab: my Altair version is older than 6</strong></summary>
<p>The test notebook checks this for you. Run <code>%pip install -U "altair>=6"</code> in a new cell, then <b>Runtime → Restart session</b>, and run the notebook again.</p>
</details>

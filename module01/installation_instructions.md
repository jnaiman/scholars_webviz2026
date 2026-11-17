---
title: Installation & Setup Instructions
layout: default
notitle: true
description: >-
  Everything to install and set up before (or during) the workshop, for both
  the "install on my computer" and the "browser only" tracks.
---

{% assign cv = site.data.class.urls | where: "id", "cv_template" | first %}
{% assign st_tmpl = site.data.class.urls | where: "id", "streamlit_template" | first %}
{% assign repo = "https://github.com/" | append: site.githuburlbase | append: site.baseurl %}
{% assign colab = "https://colab.research.google.com/github/" | append: site.githuburlbase | append: site.baseurl | append: "/blob/" | append: site.branch %}

# Installation & Setup Instructions

By the end of the workshop you will have:

1. **A personal website** at `https://<your-username>.github.io` built with [Jekyll](https://jekyllrb.com/), with interactive [Altair](https://altair-viz.github.io/) plots on it (Module 3).
2. **A Streamlit app** at `https://<your-app-name>.streamlit.app` hosted for free on [Streamlit Community Cloud](https://streamlit.io/cloud) (Module 4).

This page lists everything you need for both. The slides for [Lecture 1.0]({{site.baseurl}}/module01/lecture01p0.html) and [Lecture 1.2]({{site.baseurl}}/module01/lecture01p2.html) walk through the same steps with screenshots and links.

**Please try to do Steps 1 and 2 before the workshop.** Step 3 (Ruby/Jekyll) is the one most likely to need troubleshooting, so if you are installing locally, start it early. We will walk around and help during Module 1.

Contents:
1. [Pick a track](#pick-a-track)
2. [Step 1: Make your accounts (everyone)](#step-1-make-your-accounts-everyone)
3. [Step 2: Python (Track A)](#step-2-python-track-a) or [Google Colab (Track B)](#step-2-google-colab-track-b)
4. [Step 3: git and Ruby/Jekyll (Track A only)](#step-3-git-and-rubyjekyll-track-a-only)
5. [Step 4: Put the Jekyll template on your github.io site (everyone)](#step-4-put-the-jekyll-template-on-your-githubio-site-everyone)
6. [Step 5: Deploy your first Streamlit app (everyone)](#step-5-deploy-your-first-streamlit-app-everyone)
7. [Troubleshooting](#troubleshooting)

---

## Pick a track

You can do this whole workshop **without installing anything**. Installing locally is faster once it works, because you can preview changes on your own computer instead of waiting for GitHub to rebuild.

| | **Track A: install on my computer** | **Track B: browser only** |
|---|---|---|
| Write Python / make Altair plots | JupyterLab on your computer | [Google Colab](https://colab.research.google.com/) (free, needs a Google account) |
| Build your Jekyll site | `bundle exec jekyll serve` previews it on your computer, then `git push` | Upload files on github.com, GitHub builds it (1-2 min per change) |
| Build your Streamlit app | `streamlit run` previews it on your computer, then `git push` | Edit files on github.com, Streamlit Cloud rebuilds it |
| What to install | Miniconda, git, Ruby + Jekyll, (optional) VS Code | Nothing |
| Best for | People who will keep building websites/apps after the workshop | Locked-down or shared computers, tablets, or "I just want to try it" |

You can also mix them: for example, use Colab for Python (Track B) but install Ruby/Jekyll locally (Track A).

---

## Step 1: Make your accounts (everyone)

1. **GitHub** -- sign up for a free account at [github.com/signup](https://github.com/signup).
   * Your username becomes your website address (`<your-username>.github.io`), so pick something you are happy to put on a CV.
   * If you already have a GitHub account *and* already use `<your-username>.github.io` for something else, see [Hosting in a different repository](#option-host-the-template-in-a-different-repository) below.
2. **Streamlit Community Cloud** -- go to [share.streamlit.io](https://share.streamlit.io/), click "Continue with GitHub" and authorize Streamlit to read your GitHub repositories. It is free for public apps.
3. **Track B only: Google** -- any Google account works for [Google Colab](https://colab.research.google.com/). (Illinois users can also use their @illinois.edu Google account if it is turned on.)

---

## Step 2: Python (Track A)

### 2A.1 Install Miniconda

Conda installs Python and keeps the packages for this workshop in their own "environment", separate from anything else on your computer.

* Download **Miniconda** from [anaconda.com/download/success](https://www.anaconda.com/download/success) (scroll to "Miniconda Installers") and run the installer. Accept the defaults. (Full Anaconda works too if you already have it.)
* **Mac:** open the **Terminal** app afterwards. **Windows:** open **Anaconda Prompt** from the Start menu (not the regular Command Prompt).
* Check it worked: `conda --version` should print a version number.

> **Windows tip:** if your Windows username has a space in it (e.g. `C:\Users\Jane Doe`), install Miniconda for "All Users" or into a folder without spaces like `C:\miniconda3`, otherwise some packages won't install.

### 2A.2 Create the workshop environment

Download [environment.yml]({{ repo }}/raw/{{ site.branch }}/module01/env_files/environment.yml) (right click → "Save link as...", keep the name `environment.yml`). In the Terminal/Anaconda Prompt, `cd` to the folder you saved it in (usually `cd Downloads`) and run:

```bash
conda env create -f environment.yml
conda activate webviz
```

Or, without the file, all in one line:

```bash
conda create -n webviz -c conda-forge python=3.12 altair=6 vega_datasets pandas numpy matplotlib jupyterlab pip ; conda activate webviz ; pip install streamlit
```

**Every time** you open a new Terminal/Anaconda Prompt for this workshop, run `conda activate webviz` first. Your prompt will start with `(webviz)`.

> Already have Python 3.10+ and prefer pip? `python -m pip install -r requirements.txt` with this [requirements.txt]({{ repo }}/raw/{{ site.branch }}/module01/env_files/requirements.txt) works too.

> **Which Altair?** This workshop uses **Altair 6** (it saves plots as vega-lite version 6 files). If you already have Altair 5 installed, `conda install -c conda-forge altair=6` upgrades it.

### 2A.3 Test it

1. Download the [test notebook]({{ repo }}/raw/{{ site.branch }}/module01/test_install.ipynb) (right click → "Save link as...").
2. Run `jupyter lab` in your Terminal/Anaconda Prompt (with `(webviz)` showing). A browser tab opens.
3. Open `test_install.ipynb` and run every cell (Run → Run All Cells). The last cells draw an interactive plot and save it to a file called `my_first_chart.json`. If you see the plot, you're done with Python.

Also try `streamlit hello` in the Terminal/Anaconda Prompt. A demo app should open in your browser. Stop it with `CTRL+C`.

---

## Step 2: Google Colab (Track B)

1. Open the test notebook directly in Colab: **[open test_install.ipynb in Colab]({{ colab }}/module01/test_install.ipynb)**.
2. Sign in with your Google account and click **Runtime → Run all**. (If Colab warns "This notebook was not authored by Google", click "Run anyway".)
3. The last cells draw a plot and save `my_first_chart.json`. Click the **folder icon** in Colab's left sidebar to see the file; right click → **Download** to save it to your computer.

> Colab notebooks are temporary. To keep your work, use **File → Save a copy in Drive**. Files you create (like the JSONs) disappear when the session ends, so download them as you go.

You can skip Step 3.

---

## Step 3: git and Ruby/Jekyll (Track A only)

### 3.1 Install git

* **Mac:** in Terminal run `xcode-select --install` (installs Apple's command line tools, which include git). Check with `git --version`.
* **Windows:** install [Git for Windows](https://git-scm.com/downloads/win) with the default options. It includes "Git Credential Manager", which handles logging in to GitHub for you.
* **Linux:** `sudo apt install git` (Ubuntu/Debian) or your distribution's package manager.

Then tell git who you are (use the email from your GitHub account):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

**Logging in when you push:** the first time you `git push`, GitHub asks you to log in. Windows (Git Credential Manager) opens a browser window. On Mac/Linux, when it asks for a "password", paste a **personal access token** instead of your GitHub password. To make one: GitHub → your picture (top right) → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token, tick the `repo` box, and copy the token somewhere safe. ([GitHub's instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens))

### 3.2 Install Ruby, Bundler and Jekyll

Jekyll is written in Ruby. **Ruby 3.3 or 3.4 is recommended** (the workshop template is also tested with Ruby 4.0, but most online instructions are still written for 3.x). Follow the official guide for your system, **all the way to the end of the page** -- each one has "next steps" (like adding lines to your shell config) that are easy to miss:

* **Mac:** [jekyllrb.com/docs/installation/macos](https://jekyllrb.com/docs/installation/macos/) -- installs Homebrew, then `chruby` + `ruby-install`, then Ruby, then Jekyll.
  * After installing **Homebrew**, it prints "Next steps" with two commands (`echo ... >> ...` and `eval ...`). Run them, or `brew` won't be found.
  * After installing **chruby**, add the three `source`/`chruby` lines it lists to `~/.zshrc` (or `~/.bash_profile` if you use bash), then **close and reopen Terminal**.
* **Windows:** [jekyllrb.com/docs/installation/windows](https://jekyllrb.com/docs/installation/windows/) -- download **Ruby+Devkit 3.4.x (x64)** from [rubyinstaller.org](https://rubyinstaller.org/downloads/) (not the 4.0 one), keep "Run `ridk install`" ticked at the end, and choose option 3 (MSYS2 and MINGW development toolchain).
* **Ubuntu Linux:** [jekyllrb.com/docs/installation/ubuntu](https://jekyllrb.com/docs/installation/ubuntu/) &nbsp;&nbsp; **Other Linux:** [jekyllrb.com/docs/installation/other-linux](https://jekyllrb.com/docs/installation/other-linux/)

Then, in a **new** Terminal/Command Prompt:

```bash
gem install jekyll bundler
ruby -v      # should say 3.3.x or 3.4.x
jekyll -v    # should print a version number
```

> **Mac:** `ruby -v` says `2.6.x`? That is Apple's built-in "system" Ruby, which is too old and can't install gems. Your new Ruby isn't on your PATH yet -- re-check the chruby lines in `~/.zshrc`, then close and reopen Terminal.

> You do **not** need to do this inside the `webviz` conda environment. Ruby and conda don't interact.

### 3.3 (Optional) Install VS Code

Any text editor works for this workshop, but [VS Code](https://code.visualstudio.com/download) is free and shows your files, a Terminal and Markdown previews side by side.

---

## Step 4: Put the Jekyll template on your github.io site (everyone)

We'll use the **[online CV template]({{ cv.url }})**, a Jekyll site with an About page, a Projects page, and support for interactive vega-lite/Altair plots built in. Its [README]({{ cv.url }}#readme) has more detail on every file.

### 4.1 Create your github.io repository

1. On GitHub, click **+** (top right) → **New repository**.
2. Name it **exactly** `<your-username>.github.io` (e.g. `jnaiman.github.io`). Any other name won't work as your main site -- watch for typos and capital letters.
3. Make it **Public**, tick "Add a README file" (Track B) or leave it empty (Track A), and click **Create repository**.

### 4.2 Download the template

[⬇️ Download the template as a zip file]({{ cv.url }}/archive/refs/heads/main.zip) and unzip it. You get a folder called `online_cv_public_fa2026-main`. You'll copy **everything inside** that folder (not the folder itself) into your repository.

### 4.3 Track A: copy the files locally, preview, and push

```bash
git clone https://github.com/<your-username>/<your-username>.github.io.git
```

Copy everything inside `online_cv_public_fa2026-main` into the new `<your-username>.github.io` folder. Then:

```bash
cd <your-username>.github.io
bundle install                 # first time only -- installs the site's Ruby packages
bundle exec jekyll serve       # builds the site and serves it on your computer
```

Open **http://localhost:4008** in your browser. You should see the template's About page with a corgi. Stop the server with `CTRL+C` when you're done.

Now put it online:

```bash
git add -A
git commit -m "add Jekyll template"
git push
```

### 4.3 Track B: upload the files in the browser

1. On your repository's GitHub page click **Add file → Upload files**.
2. Drag in the files and folders from **inside** `online_cv_public_fa2026-main`. GitHub only accepts **100 files per upload** and the template has a few more than that, so do it in **two batches**: first the folders whose names start with `_`, click **Commit changes**; then everything else, **Commit changes** again.

> If your computer hides files that start with a `.` (like `.gitignore`), that's fine -- the site works without them.

### 4.4 Turn on GitHub Pages and check the build

1. In your repository go to **Settings → Pages**. Under "Build and deployment" set **Source: Deploy from a branch**, **Branch: `main`**, folder **`/ (root)`**, and **Save**.
2. Click the **Actions** tab. A yellow circle means the site is building; it turns green after a minute or two (red means an error -- see [Troubleshooting](#troubleshooting)).
3. Go to `https://<your-username>.github.io`. It should look like the local preview. (A 404 page right after a push usually just means "wait another minute".)

### 4.5 Make it yours (a first edit)

Open `_config.yml` -- locally in your editor, or on GitHub by clicking the file and then the ✏️ pencil icon. In "PART 1" change:

* `title:` -- e.g. `Your Name -- Portfolio`
* `repository:` -- your GitHub username (e.g. `jnaiman`)
* `author: name:` -- your name

Track A: stop and restart `bundle exec jekyll serve` (changes to `_config.yml` need a restart), check the preview, then `git add -A`, `git commit -m "my info"`, `git push`. Track B: click **Commit changes**, then watch the Actions tab.

### Option: host the template in a different repository

Already using your `<your-username>.github.io` for something else, or want to keep this separate? Put the template in **any** public repository (say `webviz_portfolio`), then:

1. In `_config.yml` set `baseurl: "/webviz_portfolio"` (a slash plus your repository's name).
2. Turn on Pages as in 4.4.

Your site will be at `https://<your-username>.github.io/webviz_portfolio`.

---

## Step 5: Deploy your first Streamlit app (everyone)

[Streamlit](https://streamlit.io/) turns a Python script into a web app. [Streamlit Community Cloud](https://share.streamlit.io/) runs it for free from a **public GitHub repository**. An app needs only two files:

* `streamlit_app.py` -- your Python code
* `requirements.txt` -- the packages Streamlit Cloud must install (e.g. `streamlit` and `altair`)

### 5.1 Get the starter files into a GitHub repository

Pick one:

* **Fork the starter repository** (easiest): go to [{{ st_tmpl.url }}]({{ st_tmpl.url }}), click **Fork**, name it something like `webviz_streamlit`, and click **Create fork**.
* **Upload the workshop's starter files** into a new repository: make a new **Public** repository (with "Add a README file" ticked), then **Add file → Upload files** and upload the two files from the workshop's [streamlit_starter folder]({{ repo }}/tree/{{ site.branch }}/module04/streamlit_starter). (On each file's GitHub page, use the "Download raw file" button ⬇️ to save it first.)
* **Use any repository you already have:** the two files can sit in a folder inside any public repository (even your github.io one). You'll just tell Streamlit Cloud which folder in 5.2.

### 5.2 Deploy it

1. Go to [share.streamlit.io](https://share.streamlit.io/) and click **Create app** (top right).
2. Choose **"Deploy a public app from GitHub"**.
3. Fill in: **Repository** (`<your-username>/webviz_streamlit`), **Branch** (`main`), **Main file path** (`streamlit_app.py`, or `some_folder/streamlit_app.py` if it's in a folder), and an **App URL** you like.
4. Click **Deploy**. The first build takes a few minutes. When it's done you'll have a live app at `https://<your-app-url>.streamlit.app`.

### 5.3 Make an edit

* **Track B:** on GitHub open `streamlit_app.py`, click ✏️, change the text in `st.title(...)`, and **Commit changes**. Refresh your app after a minute.
* **Track A:** clone the repository, then run it on your computer first:

  ```bash
  git clone https://github.com/<your-username>/webviz_streamlit.git
  cd webviz_streamlit
  conda activate webviz
  streamlit run streamlit_app.py
  ```

  A browser tab opens at `http://localhost:8501`. Edit `streamlit_app.py`, save, and click **Rerun** (or "Always rerun") in the app. When you like it, `git add -A`, `git commit -m "..."`, `git push`, and Streamlit Cloud updates the live app.

---

## Troubleshooting

<details><summary><strong>conda: "command not found" / "not recognized"</strong></summary>
<p>Mac: close and reopen Terminal after installing. If it still fails, run <code>~/miniconda3/bin/conda init zsh</code> and reopen Terminal. Windows: make sure you opened <b>Anaconda Prompt</b>, not Command Prompt or PowerShell.</p>
</details>

<details><summary><strong>git push asks for a password and then says "Authentication failed"</strong></summary>
<p>GitHub no longer accepts your account password on the command line. Paste a personal access token instead (see <a href="#install-git">3.1</a>). On Windows, Git Credential Manager should open a browser login instead.</p>
</details>

<details><summary><strong>git push is rejected: "Updates were rejected because the remote contains work that you do not have locally"</strong></summary>
<p>You (or GitHub, e.g. when it created a README) changed something on github.com that isn't on your computer yet. Run <code>git pull</code>, then <code>git push</code> again. It is easiest to make all your edits in one place -- either locally or on GitHub -- and not both.</p>
</details>

<details><summary><strong>bundle install fails, or errors right after you change Ruby versions</strong></summary>
<p>Delete the file <code>Gemfile.lock</code> in your site's folder and run <code>bundle install</code> again.</p>
</details>

<details><summary><strong>Mac: "eventmachine" or "binder.o" errors during bundle install</strong></summary>
<p>Your Xcode command line tools are out of date. Reinstall them and Ruby (try without <code>sudo</code> first):</p>
<pre>
sudo rm -rf /Library/Developer/CommandLineTools
sudo xcode-select --install
brew install chruby ruby-install
ruby-install ruby 3.4.1
</pre>
<p>Then close and reopen Terminal and run <code>bundle install</code> again. More details in <a href="https://github.com/eventmachine/eventmachine/issues/990">this eventmachine issue</a>.</p>
</details>

<details><summary><strong>Mac: "ld: symbol(s) not found for architecture arm64"</strong></summary>
<p>Reinstall Ruby with <code>ruby-install ruby 3.4.1 -- --enable-shared</code>, reopen Terminal, delete <code>Gemfile.lock</code> and run <code>bundle install</code>.</p>
</details>

<details><summary><strong>Liquid Exception mentioning "repository" or "PAGES_REPO_NWO"</strong></summary>
<p>Open <code>_config.yml</code> and set <code>repository:</code> to your GitHub username (e.g. <code>repository: jnaiman</code>), then restart <code>bundle exec jekyll serve</code>.</p>
</details>

<details><summary><strong>The local site works but github.io shows a 404 or an old version</strong></summary>
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

<details><summary><strong>Streamlit Cloud: "ModuleNotFoundError: No module named ..."</strong></summary>
<p>Add the missing package name to <code>requirements.txt</code> (one per line), commit, and the app rebuilds. Every package you <code>import</code> (other than ones built into Python) must be listed there.</p>
</details>

<details><summary><strong>Streamlit Cloud: the app doesn't change after I push</strong></summary>
<p>Wait a minute and refresh. If it still shows the old version, open the app, click <b>Manage app</b> (bottom right) to see the logs, and use the ⋮ menu → <b>Reboot app</b>.</p>
</details>

<details><summary><strong>Colab: "ModuleNotFoundError"</strong></summary>
<p>Add a cell at the top with <code>%pip install &lt;package&gt;</code> and run it first. Altair and pandas are already installed in Colab.</p>
</details>

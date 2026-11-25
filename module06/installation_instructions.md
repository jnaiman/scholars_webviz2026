---
title: Installing Everything Locally
layout: default
notitle: true
description: >-
  Optional: install Python, git, Ruby and Jekyll on your own computer, then
  preview your website and Streamlit app locally before you push them online.
---

{% assign cv = site.data.class.urls | where: "id", "cv_template" | first %}
{% assign st_tmpl = site.data.class.urls | where: "id", "streamlit_template" | first %}
{% assign repo = "https://github.com/" | append: site.githuburlbase | append: site.baseurl %}

# Installing Everything Locally

**This is optional.** Everything in Modules 1-5 works in your web browser. Installing the tools on your own computer gives you a faster edit loop: you see each change to your website or app on your own computer in a second or two, and only upload ("push") it when you're happy with it, instead of waiting for GitHub or Streamlit Cloud to rebuild after every edit.

The slides for [Lecture 6.1]({{site.baseurl}}/module06/lecture6p1.html) (installing) and [Lecture 6.2]({{site.baseurl}}/module06/lecture6p2.html) (working locally) walk through the same steps.

Your website and app live on GitHub either way, so you can switch at any time and pick up where you left off.

Contents:
1. [What gets installed](#what-gets-installed)
2. [Step 1: Python with Miniconda](#step-1-python-with-miniconda)
3. [Step 2: git](#step-2-git)
4. [Step 3: Ruby, Bundler and Jekyll](#step-3-ruby-bundler-and-jekyll)
5. [Step 4: (Optional) VS Code](#step-4-optional-vs-code)
6. [Step 5: Work on your github.io site locally](#step-5-work-on-your-githubio-site-locally)
7. [Step 6: Make Altair plots locally](#step-6-make-altair-plots-locally)
8. [Step 7: Work on your Streamlit app locally](#step-7-work-on-your-streamlit-app-locally)
9. [Troubleshooting](#troubleshooting)

---

## What gets installed

| In the browser (Modules 1-5) | On your computer (this module) |
|---|---|
| Google Colab | Python + JupyterLab, via **Miniconda** |
| Upload / edit files on github.com | **git**: `git clone`, `git add`, `git commit`, `git push` |
| GitHub builds your site after each change (1-2 min) | **Ruby + Jekyll**: `bundle exec jekyll serve` previews it instantly |
| Streamlit Cloud rebuilds your app after each change | **Streamlit**: `streamlit run streamlit_app.py` previews it instantly |
| github.dev editor | (optional) **VS Code** |

You can also install just some of these -- for example, only Miniconda for Python, and keep uploading files on github.com.

---

## Step 1: Python with Miniconda

### 1.1 Install Miniconda

Conda installs Python and keeps the packages for this workshop in their own "environment", separate from anything else on your computer.

* Download **Miniconda** from [anaconda.com/download/success](https://www.anaconda.com/download/success) (scroll to "Miniconda Installers") and run the installer. Accept the defaults. (Full Anaconda works too if you already have it.)
* **Mac:** open the **Terminal** app afterwards. **Windows:** open **Anaconda Prompt** from the Start menu (not the regular Command Prompt).
* Check it worked: `conda --version` should print a version number.

> **Windows tip:** if your Windows username has a space in it (e.g. `C:\Users\Jane Doe`), install Miniconda for "All Users" or into a folder without spaces like `C:\miniconda3`, otherwise some packages won't install.

### 1.2 Create the workshop environment

Download [environment.yml]({{ repo }}/raw/{{ site.branch }}/module06/env_files/environment.yml) (right click → "Save link as...", keep the name `environment.yml`). In the Terminal/Anaconda Prompt, `cd` to the folder you saved it in (usually `cd Downloads`) and run:

```bash
conda env create -f environment.yml
conda activate webviz
```

Or, without the file, all in one line:

```bash
conda create -n webviz -c conda-forge python=3.12 altair=6 vega_datasets pandas numpy matplotlib jupyterlab pip ; conda activate webviz ; pip install streamlit
```

**Every time** you open a new Terminal/Anaconda Prompt for this workshop, run `conda activate webviz` first. Your prompt will start with `(webviz)`.

> Already have Python 3.10+ and prefer pip? `python -m pip install -r requirements.txt` with this [requirements.txt]({{ repo }}/raw/{{ site.branch }}/module06/env_files/requirements.txt) works too.

> **Which Altair?** This workshop uses **Altair 6** (it saves plots as vega-lite version 6 files). If you already have Altair 5 installed, `conda install -c conda-forge altair=6` upgrades it.

### 1.3 Test it

1. Download the [test notebook]({{ repo }}/raw/{{ site.branch }}/module01/test_install.ipynb) (right click → "Save link as...").
2. Run `jupyter lab` in your Terminal/Anaconda Prompt (with `(webviz)` showing). A browser tab opens.
3. Open `test_install.ipynb` and run every cell (Run → Run All Cells). The last cells draw an interactive plot and save it to a file called `my_first_chart.json`. If you see the plot, Python is ready.

Also try `streamlit hello` in the Terminal/Anaconda Prompt. A demo app should open in your browser. Stop it with `CTRL+C`.

---

## Step 2: git

git copies your repositories from GitHub to your computer (`clone`) and sends your changes back (`push`).

### 2.1 Install git

* **Mac:** in Terminal run `xcode-select --install` (installs Apple's command line tools, which include git). Check with `git --version`.
* **Windows:** install [Git for Windows](https://git-scm.com/downloads/win) with the default options. It includes "Git Credential Manager", which handles logging in to GitHub for you.
* **Linux:** `sudo apt install git` (Ubuntu/Debian) or your distribution's package manager.

### 2.2 Tell git who you are

Use the email from your GitHub account:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### 2.3 Logging in when you push

The first time you `git push`, GitHub asks you to log in. Windows (Git Credential Manager) opens a browser window. On Mac/Linux, when it asks for a "password", paste a **personal access token** instead of your GitHub password. To make one: GitHub → your picture (top right) → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token, tick the `repo` box, and copy the token somewhere safe. ([GitHub's instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens))

---

## Step 3: Ruby, Bundler and Jekyll

Jekyll is written in Ruby. **This is the step most likely to need troubleshooting**, so give yourself some time.

**Ruby 3.3 or 3.4 is recommended** (the template is also tested with Ruby 4.0, but most online instructions are still written for 3.x). Follow the official guide for your system, **all the way to the end of the page** -- each one has "next steps" (like adding lines to your shell config) that are easy to miss:

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

---

## Step 4: (Optional) VS Code

Any text editor works, but [VS Code](https://code.visualstudio.com/download) is free and shows your files, a Terminal and Markdown previews side by side. (It's the same editor as github.dev, so it will look familiar.)

---

## Step 5: Work on your github.io site locally

### 5.1 Get your site onto your computer

**Already made your site in Module 1?** Clone it:

```bash
git clone https://github.com/<your-username>/<your-username>.github.io.git
cd <your-username>.github.io
```

<details><summary><strong>Starting from scratch instead?</strong></summary>
<ol>
<li>On GitHub, click <b>+</b> → <b>New repository</b>, name it exactly <code>&lt;your-username&gt;.github.io</code>, make it <b>Public</b>, leave it empty, and click <b>Create repository</b>.</li>
<li><code>git clone https://github.com/&lt;your-username&gt;/&lt;your-username&gt;.github.io.git</code></li>
<li><a href="{{ cv.url }}/archive/refs/heads/main.zip">Download the template zip</a>, unzip it, and copy <b>everything inside</b> <code>online_cv_public_fa2026-main</code> (not the folder itself) into the cloned folder.</li>
<li>After 5.3 below, turn on GitHub Pages: <b>Settings → Pages</b> → "Deploy from a branch", <code>main</code>, <code>/ (root)</code> → <b>Save</b>.</li>
</ol>
</details>

### 5.2 Preview it

```bash
bundle install                 # first time only -- installs the site's Ruby packages
bundle exec jekyll serve       # builds the site and serves it on your computer
```

Open **http://localhost:4008** in your browser. You should see your site. Leave `jekyll serve` running while you edit: save a file, refresh the browser, and the change is there. (Changes to `_config.yml` are the exception -- stop the server with `CTRL+C` and start it again.)

### 5.3 Put your changes online

Stop the server with `CTRL+C` (or open a second Terminal), then:

```bash
git add -A
git commit -m "describe what you changed"
git push
```

GitHub rebuilds your site (watch the **Actions** tab), and `https://<your-username>.github.io` updates a minute or two later.

> **Pick one place to edit.** If you change files on github.com *and* on your computer, git will refuse to push until you `git pull` the github.com changes first. Run `git pull` at the start of every session to be safe.

---

## Step 6: Make Altair plots locally

1. Download the [Module 3 notebook]({{ repo }}/raw/{{ site.branch }}/module03/altair_to_json.ipynb) (right click → "Save link as...").
2. `conda activate webviz`, then `jupyter lab`, and open it. Run the cells.
3. The JSON files are saved in a `my_json_files` folder next to the notebook. Copy them into `my_assets/json/` in your github.io folder, add a `<vegachart>` line for each to a page in `projects/` (see [Lecture 3.2]({{site.baseurl}}/module03/lecture3p2.html)), and check them with `bundle exec jekyll serve` at **http://localhost:4008/projects/**.
4. `git add -A`, `git commit -m "add plots"`, `git push`.

---

## Step 7: Work on your Streamlit app locally

### 7.1 Get your app onto your computer

**Already made your app in Module 4?** Clone its repository:

```bash
git clone https://github.com/<your-username>/webviz_streamlit.git
cd webviz_streamlit
```

**Starting from scratch?** Fork the [starter repository]({{ st_tmpl.url }}) on GitHub (or make a new public repository and add the workshop's [starter files]({{ repo }}/tree/{{ site.branch }}/module04/streamlit_starter)), then clone it as above.

### 7.2 Run it

```bash
conda activate webviz
streamlit run streamlit_app.py
```

A browser tab opens at **http://localhost:8501**. Edit `streamlit_app.py`, save, and click **Rerun** (or "Always rerun") in the app's top-right corner.

### 7.3 Put your changes online

```bash
git add -A
git commit -m "describe what you changed"
git push
```

Streamlit Community Cloud rebuilds the live app a minute later. (Haven't deployed it yet? See [Lecture 4.1]({{site.baseurl}}/module04/lecture4p1.html).)

> Installed a new package with `pip install` or `conda install` to use in your app? Also add it to `requirements.txt`, or the online app will fail with `ModuleNotFoundError` even though it works on your computer.

---

## Troubleshooting

<details><summary><strong>conda: "command not found" / "not recognized"</strong></summary>
<p>Mac: close and reopen Terminal after installing. If it still fails, run <code>~/miniconda3/bin/conda init zsh</code> and reopen Terminal. Windows: make sure you opened <b>Anaconda Prompt</b>, not Command Prompt or PowerShell.</p>
</details>

<details><summary><strong>"ModuleNotFoundError" in JupyterLab or when running streamlit</strong></summary>
<p>Check your prompt starts with <code>(webviz)</code>. If not, run <code>conda activate webviz</code>, then start <code>jupyter lab</code> or <code>streamlit run</code> again.</p>
</details>

<details><summary><strong>git push asks for a password and then says "Authentication failed"</strong></summary>
<p>GitHub no longer accepts your account password on the command line. Paste a personal access token instead (see <a href="#logging-in-when-you-push">2.3</a>). On Windows, Git Credential Manager should open a browser login instead.</p>
</details>

<details><summary><strong>git push is rejected: "Updates were rejected because the remote contains work that you do not have locally"</strong></summary>
<p>Something changed on github.com that isn't on your computer yet (e.g. an edit you made in the browser). Run <code>git pull</code>, then <code>git push</code> again.</p>
</details>

<details><summary><strong>bundle install fails, or errors right after you change Ruby versions</strong></summary>
<p>Delete the file <code>Gemfile.lock</code> in your site's folder and run <code>bundle install</code> again.</p>
</details>

<details><summary><strong>"cannot load such file -- csv" (or base64, bigdecimal, logger) when running jekyll</strong></summary>
<p>Newer Ruby versions (3.4+) no longer include some libraries that older Jekyll versions need. Add a line like <code>gem "csv"</code> (one line per missing name) to the <code>Gemfile</code> in your site's folder, run <code>bundle install</code>, and try <code>bundle exec jekyll serve</code> again.</p>
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

<details><summary><strong>The local site works but github.io doesn't update</strong></summary>
<ul>
<li>Did you <code>git push</code>? Check that your change shows up on your repository's page on github.com.</li>
<li>Wait 1-2 minutes and check the <b>Actions</b> tab for the yellow/green circle (red = error; click it to read why).</li>
<li>Hard-refresh your browser (<code>Cmd+Shift+R</code> / <code>Ctrl+Shift+R</code>).</li>
</ul>
</details>

<details><summary><strong>The app works with streamlit run but not on Streamlit Cloud</strong></summary>
<ul>
<li><code>ModuleNotFoundError</code>: add the package to <code>requirements.txt</code>, commit and push.</li>
<li><code>FileNotFoundError</code>: is every data/<code>.json</code> file committed and pushed? Use paths relative to <code>streamlit_app.py</code>, not your computer's folders (e.g. not <code>C:\Users\...</code>).</li>
<li>Open the app, click <b>Manage app</b> (bottom right) to read the logs, and use the ⋮ menu → <b>Reboot app</b> if it's stuck on an old version.</li>
</ul>
</details>

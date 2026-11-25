---
layout: week
icon: undraw_software-engineer_xv60.svg
visible: true
notitle: true
examples:
  - filename: installation_instructions.html
    type: link
    title: Installing Everything Locally
    description: Step-by-step installs (Miniconda, git, Ruby & Jekyll), working on your site and app locally, and troubleshooting.
  - filename: environment.yml
    type: githubraw
    title: Conda environment file (environment.yml)
    description: "Create the workshop environment with: conda env create -f environment.yml"
    link: module06/env_files/environment.yml
  - filename: requirements.txt
    type: githubraw
    title: pip requirements file (requirements.txt)
    description: For people who prefer pip over conda.
    link: module06/env_files/requirements.txt
  - filename: test_install.ipynb
    type: githubraw
    title: Test-your-setup notebook (download)
    description: The Module 1 test notebook -- open it with jupyter lab to check your local install.
    link: module01/test_install.ipynb
  - filename: altair_to_json.ipynb
    type: githubraw
    title: Module 3 notebook (download)
    description: Make the Module 3 plots locally; the JSON files are saved next to the notebook.
    link: module03/altair_to_json.ipynb
---

# Installing Everything Locally (Optional)

**This module is optional, for after the workshop.** Everything in Modules 1-5 works in your web browser. Here we install the same tools on your own computer, so you can preview your website and Streamlit app locally and only push changes online when you're happy with them:

* **Python** with Altair, pandas, JupyterLab and Streamlit (via Miniconda) -- instead of Google Colab,
* **git** -- instead of uploading files on github.com, and
* **Ruby & Jekyll** -- to preview your github.io site with `bundle exec jekyll serve`.

[Lecture 6.1](lecture6p1.html) covers installing; [Lecture 6.2](lecture6p2.html) covers working on the site and app you already made. The [Installing Everything Locally](installation_instructions.html) page has every step plus troubleshooting.

### Optional Materials and Resources
1. [Jekyll installation guides](https://jekyllrb.com/docs/installation/) and the [Jekyll step-by-step tutorial](https://jekyllrb.com/docs/step-by-step/01-setup/)
2. [GitHub's guide to git](https://docs.github.com/en/get-started/getting-started-with-git) and the [git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)
3. [Conda: managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
4. [Streamlit: install and run locally](https://docs.streamlit.io/get-started/installation)
5. [VS Code](https://code.visualstudio.com/docs) docs

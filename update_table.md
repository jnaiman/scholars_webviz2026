# Web Viz workshop: setup checklist

Items that need a decision, a login, or a check in a live account. (This file is excluded from the website build.)

## Needs your input

| # | Where | Description | Suggested fix | Status |
|---|---|---|---|---|
| 1 | `_data/class.yml` → `course.time`, `course.location` | Date/time and room are `TBD`. | Fill in. |  |
| 2 | `_data/class.yml` → `urls` → `mediaspace` | Still points at the **PowerBI** workshop's MediaSpace channel (linked from the syllabus info box and Lecture 5.1). | Make a Web Viz channel and paste its URL, or remove the entry. |  |
| 3 | `_data/class.yml` → `urls` → `streamlit_template` | Participants fork `jnaiman/is445_streamlit_demo` in Module 1. Its app text says "IS445" and shows that repo's URLs. | Optional: make a workshop repo (e.g. `scholars_webviz_streamlit`) and change this one URL. Uploading `module04/streamlit_starter` there would also work. |  |
| 4 | Workshop length | Modules are sized like the PowerBI workshop, but Module 1 setup (especially Ruby/Jekyll) can take a long time in the room. | Strongly encourage pre-workshop setup, or steer people with trouble to Track B (browser only). |  |
| 5 | Module structure | Module 3 = Altair + Jekyll, Module 4 = Streamlit, Module 5 = linking the two + "where to go from here". | Change if you wanted three hands-on modules (e.g. split Altair and Jekyll). |  |

## Check by hand in live accounts

| # | Where | Description | Status |
|---|---|---|---|
| 6 | Lecture 1.2, Module 4 slides | Streamlit Cloud UI wording ("Create app", "Deploy a public app from GitHub", "Manage app", Settings → Sharing) is from the Fall 2026 IS445 lab screenshots. Click through once. |  |
| 7 | Lecture 1.2 screenshots (`module01/images/jekyll_setup`, `streamlit_setup`) | Reused from the PrairieLearn labs. They show IS445 names (`is445_demo`, "IS445 Jekyll Template"), and `jekyllWorking2025_line.png` shows your bookmarks bar. | Optional: retake. |  |
| 8 | Install page, Step 3 | Ruby advice is "3.3 or 3.4" (the template README says Ruby 4.0 also works; the PrairieLearn lab says avoid 4.0). Confirm which you want to recommend. |  |
| 9 | Colab | Colab's current Altair version wasn't checked. If Colab still ships Altair 5, the test notebook prints the upgrade command (`%pip install -U "altair>=6"`). The Module 3 notebook's code also runs on Altair 5, but its JSONs would then be vega-lite 5. Run both notebooks in Colab once. |  |
| 10 | Whole site after the first push | Open each module page, each slide deck, the notebook viewer links, the Colab links and `module03/any_site_starter/plot_page.html` on the live site. |  |

## Tested before the first commit

- Both notebooks run without errors on Altair 6.3 / pandas 3.1 / Python 3.12. All ready-made JSONs were regenerated with Altair 6.3 and declare vega-lite v6.4.1.
- `module03/jekyll_starter` (Altair 6 JSONs) was dropped into an unmodified copy of `online_cv_public_fa2026` and built with Jekyll. Headless Chrome confirmed all 4 plots and the dropdown draw on the project page. `any_site_starter/plot_page.html` (vega 6.2 / vega-lite 6.4.1 / vega-embed 7.0.2) also renders, with no console warnings.
- The Streamlit starter app runs with no exceptions in Streamlit's AppTest, including widget changes, on Streamlit 1.67 with Altair 6.3 (and earlier on 1.48 and 1.65).
- The workshop site builds with `bundle exec jekyll build`.

## Notes

- **Altair 6 everywhere** (env files `altair=6` / `altair>=6,<7`, Streamlit `requirements.txt`). The CV template still bundles vega-lite 5 JS (`assets/js/`). The v6 workshop plots draw fine on it, but every page logs "The input spec uses Vega-Lite v6.4.1, but the current version of Vega-Lite is v5..." in the browser console, and features that are new in vega-lite 6 won't work. Suggested follow-up (not done -- it's a separate repo): replace `vega.min.js`, `vega-lite.min.js` and `vega-embed.min.js` in `online_cv_public_fa2026/assets/js/` with vega 6 / vega-lite 6 / vega-embed 7 builds, then check the template's own older (v4/v5) example JSONs still render.
- `nbv.html` loaded nbviewer.js from rawgit.com, which shut down in 2019. It now uses the local `assets/js/nbv.js`. (The PowerBI repo has the same broken link, but nothing there uses it.)
- The 18 MB `module01/images/intro_naiman1-4.png` files were carried over from the PowerBI workshop. Optional: compress them.

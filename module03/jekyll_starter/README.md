# Jekyll starter files (Module 3)

Drop-in files for the [online CV template](https://github.com/jnaiman/online_cv_public_fa2026). They add a project page with four interactive Altair plots to your site. The folders here mirror the template's folders, so each file goes in the folder **with the same name** in your github.io repository:

```
jekyll_starter/                        your <username>.github.io repository
├── projects/
│   └── 2_my_altair_plots.md      →    projects/2_my_altair_plots.md
└── my_assets/
    ├── json/
    │   ├── mobility_scatter.json  →    my_assets/json/  (all four .json files)
    │   ├── mobility_dashboard.json
    │   ├── bars_by_state.json
    │   └── corgis_over_time.json
    └── pngs/
        └── altair_workshop_card.png → my_assets/pngs/altair_workshop_card.png
```

The `.json` files are exactly what [`module03/altair_to_json.ipynb`](../altair_to_json.ipynb) saves. Use these as-is, or replace them with your own.

## Option 1: upload in the browser (no installs)

1. Download the files: on GitHub, open each file and click the **Download raw file** (⬇️) button.
2. In your github.io repository on GitHub, click into the `my_assets/json` folder, then **Add file → Upload files**, drag in the four `.json` files, and **Commit changes**.
3. Do the same for `my_assets/pngs` (the `.png`) and `projects` (the `.md`).
4. Wait for the green check in the **Actions** tab, then open `https://<username>.github.io/projects/`.

> All three folders (`projects`, `my_assets/json`, `my_assets/pngs`) already exist in the template, so you only need to click into them. Uploading a file with the same name as an existing one replaces it.

## Option 2: copy locally and push

If you installed Jekyll and git on your computer ([Module 6](https://jnaiman.github.io/scholars_webviz2026/module06/) of the workshop), copy the files into the matching folders of your local clone, check them with `bundle exec jekyll serve` (open http://localhost:4008/projects/), then:

```bash
git add -A
git commit -m "add Altair project"
git push
```

## Not using the template?

See [`../any_site_starter`](../any_site_starter) for a plain HTML page that shows a `.json` plot on **any** website or GitHub Pages repository.

# Streamlit starter app (Module 4)

A small Streamlit app with sidebar widgets, Altair plots (including a selection that is sent back to Python), a vega-lite JSON plot from Module 3, and a data table.

| File | What it is |
|---|---|
| `streamlit_app.py` | the app -- all the Python code |
| `requirements.txt` | packages Streamlit Community Cloud installs before running the app |
| `corgis_over_time.json` | a plot saved with Altair in Module 3 (shown in the "A Module 3 plot" tab) |

## Put it online (no installs)

1. Download the three files (on GitHub: open each file → ⬇️ "Download raw file").
2. On GitHub, create a new **public** repository (tick "Add a README file"), then **Add file → Upload files**, drag in the three files, and **Commit changes**.
   * You can also upload them into a **folder** of a repository you already have (even your `<username>.github.io` one).
3. Go to [share.streamlit.io](https://share.streamlit.io/) → **Create app** → **Deploy a public app from GitHub**.
4. Pick the repository and branch (`main`), set **Main file path** to `streamlit_app.py` (or `your_folder/streamlit_app.py`), choose an App URL, and click **Deploy**.

To change the app, edit `streamlit_app.py` on GitHub (✏️) and commit -- the app rebuilds by itself.

## Run it on your computer

```bash
conda activate webviz            # or any Python with: pip install -r requirements.txt
streamlit run streamlit_app.py
```

Open http://localhost:8501, edit the file, save, and click **Rerun** in the app. When you're happy, `git add -A`, `git commit -m "..."`, `git push`.

## Adding packages

Every package you `import` must be listed in `requirements.txt` (one per line), or the online app will fail with `ModuleNotFoundError`. Altair is kept at version 5 to match the Jekyll template from Module 3.

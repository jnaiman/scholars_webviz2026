# Build scripts (not part of the website)

Jekyll ignores folders that start with `_` unless told otherwise, so nothing here is published.

## Notebooks

The workshop notebooks are generated, so edit the script and not the `.ipynb`:

```bash
conda activate webviz
python _tools/make_test_install_nb.py      # -> module01/test_install.ipynb
python _tools/make_altair_to_json_nb.py    # -> module03/altair_to_json.ipynb
```

The notebooks are committed **without outputs** (so they open cleanly in Colab).

## Refreshing the ready-made JSON files

The `.json` files in `module03/jekyll_starter/my_assets/json/`, `module03/any_site_starter/` and `module04/streamlit_starter/` are the output of `module03/altair_to_json.ipynb`. After changing that notebook, run it **outside the repo** and copy the results back:

```bash
mkdir -p /tmp/nb && cp module03/altair_to_json.ipynb /tmp/nb/ && cd /tmp/nb
jupyter nbconvert --to notebook --execute altair_to_json.ipynb --output executed.ipynb
cd -
cp /tmp/nb/my_json_files/{bars_by_state,corgis_over_time,mobility_dashboard,mobility_scatter}.json module03/jekyll_starter/my_assets/json/
cp /tmp/nb/my_json_files/{mobility_scatter,corgis_over_time}.json module03/any_site_starter/
cp /tmp/nb/my_json_files/mobility_scatter.html module03/any_site_starter/standalone_from_altair.html
cp /tmp/nb/my_json_files/corgis_over_time.json module04/streamlit_starter/
```

Use **Altair 5.x**. The online CV template bundles vega-lite 5.20, so the JSONs should declare a v5 schema.

The project-card image `module03/jekyll_starter/my_assets/pngs/altair_workshop_card.png` was rendered from `mobility_scatter.json` with [vl-convert](https://github.com/vega/vl-convert) (`pip install vl-convert-python`):

```python
import json, vl_convert as vlc
spec = json.load(open("mobility_scatter.json")); spec["width"] = 560; spec["height"] = 330
open("altair_workshop_card.png", "wb").write(vlc.vegalite_to_png(json.dumps(spec), vl_version="5.20", scale=1.5))
```

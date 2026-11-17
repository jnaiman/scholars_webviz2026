"""Builds module03/altair_to_json.ipynb.  Re-run after editing:
    python _tools/make_altair_to_json_nb.py

To refresh the ready-made JSON files in module03/jekyll_starter and
module03/any_site_starter, see _tools/README.md.
"""
import nbformat as nbf
from pathlib import Path

md, code = nbf.v4.new_markdown_cell, nbf.v4.new_code_cell
REPO = "jnaiman/scholars_webviz2026"

cells = [
md(f"""# Module 3: From Altair plots to JSON files for your website

In this notebook we'll:
1. make a few **interactive plots** with [Altair](https://altair-viz.github.io/),
2. save each one as a **`.json` file** (a vega-lite "spec"), and
3. get those files ready to **upload to your Jekyll site** (Lecture 3.2).

**How to run it**
* **Track A (local):** `conda activate webviz`, then `jupyter lab`, and open this notebook.
* **Track B (browser only):** [open this notebook in Google Colab](https://colab.research.google.com/github/{REPO}/blob/main/module03/altair_to_json.ipynb).

Run the cells in order (`Shift+Enter`).  Every plot is interactive once it shows up -- try hovering, clicking and dragging!

**Don't want to run code today?**  The JSON files this notebook makes are already saved in the workshop's
[`module03/jekyll_starter`](https://github.com/{REPO}/tree/main/module03/jekyll_starter) folder, ready to upload."""),

md("## 0. Imports and data"),
code("""import os
import pandas as pd
import altair as alt

print("altair", alt.__version__)   # should be 5.x -- see the Module 1 test notebook if not

# Every JSON file we make goes in this folder
OUT = "my_json_files"
os.makedirs(OUT, exist_ok=True)"""),
md("""We'll use two datasets from the IS445 course's data repository:

* **mobility** -- for 741 US regions: how likely a child from a low-income family is to move up in income as an adult
  ("Mobility"), plus population, income, schools and more.  ([more info](http://www.stat.cmu.edu/~cshalizi/uADA/15/hw/01/hw-01.pdf))
* **corgis** -- the number of corgis born in each country, each year (from the [Cardigan Archives](http://cardiped.net/)).
  Yes, really."""),
code("""mobility_url = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv"
corgis_url = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/corgs_per_country_over_time_columns_2020.csv"

mobility = pd.read_csv(mobility_url)
mobility.head()"""),

md("""## 1. Altair in one minute

Every Altair plot has the same three parts:

```python
alt.Chart(DATA).mark_TYPE().encode(CHANNEL="COLUMN:TYPE", ...)
```

* **`Chart(...)`** -- the data: a pandas DataFrame *or* a URL to a CSV/JSON file
* **`mark_...()`** -- the shape that represents each row: `mark_bar`, `mark_point`, `mark_circle`, `mark_line`, `mark_rect`, ...
* **`encode(...)`** -- which column goes on which visual "channel": `x`, `y`, `color`, `size`, `tooltip`, ...

The letter after the colon tells Altair what *kind* of data the column is:

| Code | Type | Example |
|---|---|---|
| `:Q` | quantitative (a number) | `Income:Q` |
| `:N` | nominal (a category, no order) | `State:N` |
| `:O` | ordinal (a category with an order) | `Years:O` |
| `:T` | temporal (a date/time) | `Date:T` |

These map onto the "perception channels" from Module 2: position (`x`, `y`) is the most accurate, so put your most important variable there."""),

md("""## 2. Plot 1: a bar chart, with data from a URL

Here we give Altair the **URL** of the data instead of a DataFrame.  The saved JSON then just *points* to the
data online, so the file is tiny.  The catch: the data must stay online at that address, and Altair can only
do calculations that vega-lite knows how to do (like `count()` below), not arbitrary pandas code."""),
code("""bars = alt.Chart(mobility_url).mark_bar().encode(
    x=alt.X("State:N", sort="-y", title="State"),
    y=alt.Y("count():Q", title="Number of regions in the dataset"),
    tooltip=["State:N", "count():Q"],
).properties(
    title="How many regions does each state have?",
    width="container",   # fill the width of the web page it's placed on
    height=300,
)
bars"""),
md("""`width="container"` makes the plot as wide as whatever it sits in on a web page.  In the notebook it may
look narrow -- that's fine, it will fill the page on your website."""),
code("""bars.save(f"{OUT}/bars_by_state.json")
print(os.path.getsize(f"{OUT}/bars_by_state.json"), "bytes -- tiny, because the data stays at the URL")"""),

md("""## 3. Plot 2: an interactive scatter plot with a dropdown

Now we start from the **DataFrame**.  The data gets copied *into* the JSON file, so the file works on its
own anywhere -- but keep only the columns you need so the file stays small.

We add three kinds of interactivity:
* **tooltips** on hover,
* **zoom/pan** with `.interactive()`,
* a **dropdown menu** that highlights one state, made with a *selection parameter* bound to an input widget."""),
code("""scatter_df = mobility[["Name", "State", "Population", "Income", "Mobility"]].dropna()

# A selection that is controlled by a dropdown menu ("binding") listing every state
states = sorted(scatter_df["State"].unique())
pick_state = alt.selection_point(
    fields=["State"],
    bind=alt.binding_select(options=[None] + states, labels=["All"] + states, name="Highlight a state: "),
)

scatter = alt.Chart(scatter_df).mark_circle().encode(
    x=alt.X("Income:Q", title="Average household income ($)"),
    y=alt.Y("Mobility:Q", title="Upward mobility"),
    size=alt.Size("Population:Q", scale=alt.Scale(range=[10, 400]), legend=None),
    # colored when it matches the dropdown (or nothing is picked), gray otherwise
    color=alt.condition(pick_state, alt.value("#1f77b4"), alt.value("lightgray")),
    opacity=alt.condition(pick_state, alt.value(0.8), alt.value(0.2)),
    tooltip=["Name:N", "State:N", alt.Tooltip("Population:Q", format=","),
             alt.Tooltip("Income:Q", format="$,.0f"), alt.Tooltip("Mobility:Q", format=".3f")],
).add_params(
    pick_state
).properties(
    title="Upward mobility vs. income (dot size = population)",
    width="container",
    height=400,
).interactive()

scatter"""),
code("""scatter.save(f"{OUT}/mobility_scatter.json")
print(round(os.path.getsize(f"{OUT}/mobility_scatter.json") / 1024), "KB -- bigger, the data is inside the file")"""),

md("""## 4. Plot 3: a linked "dashboard"

Two plots side by side, where **dragging a box on the left plot filters the right plot**.  This is a
*brush* (an interval selection).

When plots sit side by side (`|`, or `alt.hconcat`), give each one a fixed `width` in pixels --
`"container"` doesn't work for combined plots."""),
code("""brush = alt.selection_interval(encodings=["x", "y"])

heatmap = alt.Chart(mobility_url).mark_rect().encode(
    x=alt.X("Student_teacher_ratio:Q", bin=alt.Bin(maxbins=10), title="Student/teacher ratio"),
    y=alt.Y("State:O"),
    color=alt.Color("count():Q", title="# regions"),
).properties(
    width=250, height=450,
).add_params(brush)

histogram = alt.Chart(mobility_url).mark_bar().encode(
    x=alt.X("Mobility:Q", bin=alt.Bin(maxbins=20), title="Upward mobility",
            axis=alt.Axis(format=".2f", labelAngle=-45)),
    y=alt.Y("count():Q", title="# regions"),
).transform_filter(
    brush   # only count the regions inside the brushed box
).properties(
    width=300, height=450,
)

dashboard = (heatmap | histogram).properties(
    title="Drag a box on the left to filter the right"
)
dashboard"""),
code("""dashboard.save(f"{OUT}/mobility_dashboard.json")"""),

md("""## 5. Plot 4: reshaping data first -- corgis over time

The corgis file is in **"wide"** format: one row per year and one *column per country*.  Altair (like most
plotting tools) wants **"long"** format: one row per *observation* (year + country + count).  pandas' `melt`
does the reshaping."""),
code("""corgis_wide = pd.read_csv(corgis_url)
corgis_wide.iloc[:3, :6]"""),
code("""corgis = corgis_wide.melt(id_vars="Years", var_name="Country", value_name="Corgis born")

# The last year in the file (2020) was only partly recorded, so leave it out
corgis = corgis[corgis["Years"] < 2020]

# Keep the 6 countries with the most corgis overall, so the plot stays readable
top6 = corgis.groupby("Country")["Corgis born"].sum().nlargest(6).index
corgis = corgis[corgis["Country"].isin(top6)]
corgis.head()"""),
md("""This time the interactivity is **clicking the legend**: click a country to highlight it
(shift-click to pick more than one; double-click empty space to reset)."""),
code("""pick_country = alt.selection_point(fields=["Country"], bind="legend")

corgi_lines = alt.Chart(corgis).mark_line(strokeWidth=2.5).encode(
    x=alt.X("Years:Q", axis=alt.Axis(format="d"), title="Year"),
    y=alt.Y("Corgis born:Q"),
    color=alt.Color("Country:N", title="Country (click me!)"),
    opacity=alt.condition(pick_country, alt.value(1), alt.value(0.1)),
    tooltip=["Country:N", "Years:Q", "Corgis born:Q"],
).add_params(
    pick_country
).properties(
    title="Corgis born per year, top 6 countries",
    width="container",
    height=350,
)
corgi_lines"""),
code("""corgi_lines.save(f"{OUT}/corgis_over_time.json")"""),

md("""## 6. Get your JSON files

Here's everything we saved:"""),
code("""for f in sorted(os.listdir(OUT)):
    print(f"{f:28s} {os.path.getsize(os.path.join(OUT, f)) / 1024:7.1f} KB")"""),
md("""* **Track A (local):** the files are in the `my_json_files` folder next to this notebook.  Copy them into
  `my_assets/json/` in your github.io folder.
* **Track B (Colab):** run the next cell to download them all as one zip file (or use the folder icon in the
  left sidebar and right click → Download on each file)."""),
code("""import sys
if "google.colab" in sys.modules:
    import shutil
    from google.colab import files
    shutil.make_archive("my_json_files", "zip", OUT)
    files.download("my_json_files.zip")
else:
    print("Not in Colab -- your files are in:", os.path.abspath(OUT))"""),

md("""## 7. Bonus: a stand-alone web page for any plot

Altair can also save a plot as a complete **`.html`** web page.  Double-click it to open it in a browser, or
upload it to *any* GitHub Pages repository (no Jekyll template needed) and link to it."""),
code("""scatter.save(f"{OUT}/mobility_scatter.html")
print("open", os.path.abspath(f"{OUT}/mobility_scatter.html"), "in your browser")"""),

md("""## Next: put them on your website!

Head back to **Lecture 3.2** to upload these JSON files to `my_assets/json/` on your github.io site and make a
project page that shows them.

**Try it yourself:** change a plot above -- a different column, mark, color scheme
(`scale=alt.Scale(scheme="viridis")`), or title -- re-run, re-save, and re-upload.  The
[Altair example gallery](https://altair-viz.github.io/gallery/index.html) is a great place to steal ideas from:
every example works the same way (`chart.save("name.json")`)."""),
]

nb = nbf.v4.new_notebook()
nb["cells"] = cells
nb["metadata"] = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python"},
}
out = Path(__file__).resolve().parent.parent / "module03" / "altair_to_json.ipynb"
nbf.write(nb, out)
print("wrote", out)

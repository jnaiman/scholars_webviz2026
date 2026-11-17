"""Builds module01/test_install.ipynb.  Re-run after editing:
    python _tools/make_test_install_nb.py
"""
import nbformat as nbf
from pathlib import Path

md, code = nbf.v4.new_markdown_cell, nbf.v4.new_code_cell
REPO = "jnaiman/scholars_webviz2026"

cells = [
md(f"""# Test your setup -- Bolashak Scholars Web Viz Workshop, Module 1

This notebook checks that you can:
1. import the Python packages we use (`pandas`, `altair`, and -- if you installed locally -- `streamlit`),
2. read a dataset from the web,
3. make an interactive Altair plot, and
4. save that plot as a `.json` file (this is what we'll put on our websites in Module 3).

**How to run it:** run each cell in order with `Shift+Enter`, or use "Run All".

* **Track A (local):** open it with `jupyter lab` from a Terminal/Anaconda Prompt where you ran `conda activate webviz`.
* **Track B (browser only):** [open it in Google Colab](https://colab.research.google.com/github/{REPO}/blob/main/module01/test_install.ipynb) and use **Runtime → Run all**.
"""),
md("""## 1. Check the packages

You should see version numbers and no red error messages.  If something is missing, see the
"Troubleshooting" section of the workshop's Installation & Setup Instructions page."""),
code("""import sys
print("Python version:", sys.version.split()[0])

import pandas as pd
print("pandas version:", pd.__version__)

import altair as alt
print("altair version:", alt.__version__)

# Are we running in Google Colab?
IN_COLAB = "google.colab" in sys.modules

try:
    import streamlit
    print("streamlit version:", streamlit.__version__)
except ImportError:
    if IN_COLAB:
        print("streamlit: not installed -- that's fine in Colab (you'll use Streamlit Cloud instead)")
    else:
        print("streamlit: NOT FOUND -- did you run `conda activate webviz` before `jupyter lab`?")"""),
md("""### Altair version check

This workshop uses **Altair 6**, which saves plots as **vega-lite version 6** files.
Older Altair versions mostly work too, but some examples may look different.
This cell tells you which one you have."""),
code("""major = int(alt.__version__.split(".")[0])
if major >= 6:
    print(f"Altair {alt.__version__} -- perfect!")
else:
    print(f"You have Altair {alt.__version__}.  Please upgrade to Altair 6:")
    if IN_COLAB:
        print('   run   %pip install -U "altair>=6"   in a new cell, then Runtime -> Restart session, and run this notebook again')
    else:
        print('   run   conda install -c conda-forge altair=6   in your Terminal/Anaconda Prompt and restart this notebook')"""),
md("""## 2. Read a dataset from the web

We'll use the **mobility** dataset from the IS445 course.  "Mobility" here measures how easy it is for
a child born into a low-income family to move up in income as an adult, for different US regions,
along with lots of information about each region (population, income, schools, etc.).
[More info](http://www.stat.cmu.edu/~cshalizi/uADA/15/hw/01/hw-01.pdf)."""),
code("""mobility_url = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv"
df = pd.read_csv(mobility_url)
print(df.shape[0], "rows and", df.shape[1], "columns")
df.head()"""),
md("""## 3. Make an interactive Altair plot

Each dot is one region.  Try it out once the plot appears:
* **hover** over a dot to see its name (a "tooltip"),
* **scroll** to zoom and **click-and-drag** to pan."""),
code("""# Only give Altair the columns the plot uses -- the data gets saved inside the
# plot's file in step 4, so fewer columns = a smaller, faster-loading file.
plot_df = df[["Name", "State", "Income", "Mobility"]]

chart = alt.Chart(plot_df).mark_circle(size=40, opacity=0.6).encode(
    x=alt.X("Income:Q", title="Average household income ($)"),
    y=alt.Y("Mobility:Q", title="Mobility (chance of moving up)"),
    color=alt.Color("State:N", legend=None),
    tooltip=["Name:N", "State:N", "Income:Q", "Mobility:Q"],
).properties(
    title="Upward mobility vs. income for US regions",
    width=500,
    height=350,
).interactive()

chart"""),
md("""## 4. Save the plot as a JSON file

Altair is a Python "front end" for **vega-lite**, a format for describing plots in a `.json` text file.
Web browsers know how to draw vega-lite plots, so saving this file is all we need to put the plot on a website."""),
code("""chart.save("my_first_chart.json")

import os
print("Saved my_first_chart.json --", round(os.path.getsize("my_first_chart.json") / 1024), "KB")
print("(Colab: click the folder icon in the left sidebar to find and download it.)")"""),
md("""Let's peek at the start of the file -- it's just text!"""),
code("""print(open("my_first_chart.json").read()[:400], "...")"""),
md("""## 🎉 All done!

If every cell ran and you saw the plot, your Python setup is ready.

Keep `my_first_chart.json` -- in **Module 3** we'll upload a file just like it to your github.io site.

**Optional (Track A):** to check Streamlit, run `streamlit hello` in your Terminal/Anaconda Prompt.
A demo app should open in your browser; stop it with `CTRL+C`."""),
]

nb = nbf.v4.new_notebook()
nb["cells"] = cells
nb["metadata"] = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python"},
}
out = Path(__file__).resolve().parent.parent / "module01" / "test_install.ipynb"
nbf.write(nb, out)
print("wrote", out)

# =============================================================================
#  Streamlit starter app -- Bolashak Scholars Web Viz Workshop, Module 4
#
#  Run it on your computer (Track A):
#      conda activate webviz
#      streamlit run streamlit_app.py
#  then open http://localhost:8501.  Edit this file, save, and click "Rerun"
#  (or "Always rerun") in the app's top-right corner.
#
#  Put it online (both tracks): this file + requirements.txt (+ the .json file)
#  in a PUBLIC GitHub repository, then "Create app" on share.streamlit.io.
#  Every commit to the repository updates the live app.
#
#  Streamlit runs this whole script from top to bottom every time a viewer
#  touches a widget.  That's the main idea to remember!
# =============================================================================

import json
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

# -----------------------------------------------------------------------------
# 1. Page settings and text
# -----------------------------------------------------------------------------
st.set_page_config(page_title="My Web Viz App", page_icon="📊", layout="wide")

st.title("My first Streamlit app 📊")  # <-- change me!

st.markdown(
    """
This app explores **upward mobility**: how likely a child from a low-income
family in each US region is to move up in income as an adult.
Use the controls in the sidebar to filter the data.

*(Text in Streamlit is written in Markdown, just like a Jupyter text cell.)*
"""
)

# -----------------------------------------------------------------------------
# 2. Load the data
#    @st.cache_data means "only download this once", instead of on every rerun
# -----------------------------------------------------------------------------
MOBILITY_URL = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv"


@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df[["Name", "State", "Population", "Income", "Mobility",
               "Student_teacher_ratio", "Urban"]].dropna()


mobility = load_data(MOBILITY_URL)

# -----------------------------------------------------------------------------
# 3. Widgets in the sidebar
#    Each widget returns its current value -- a normal Python variable.
# -----------------------------------------------------------------------------
st.sidebar.header("Filters")

all_states = sorted(mobility["State"].unique())
chosen_states = st.sidebar.multiselect(
    "States (leave empty for all)", all_states, default=["IL", "CA", "TX"]
)

min_inc, max_inc = int(mobility["Income"].min()), int(mobility["Income"].max())
income_range = st.sidebar.slider(
    "Average household income ($)", min_inc, max_inc, (min_inc, max_inc), step=1000
)

urban_only = st.sidebar.checkbox("Urban regions only")

color_by = st.sidebar.radio("Color the dots by", ["State", "Urban"], horizontal=True)

# Use the widget values to filter the data with ordinary pandas
filtered = mobility[mobility["Income"].between(*income_range)]
if chosen_states:
    filtered = filtered[filtered["State"].isin(chosen_states)]
if urban_only:
    filtered = filtered[filtered["Urban"] == 1]

st.sidebar.metric("Regions shown", f"{len(filtered)} of {len(mobility)}")

# -----------------------------------------------------------------------------
# 4. Plots -- the same Altair code as in Module 3, shown with st.altair_chart
#    Tabs keep the page tidy.
# -----------------------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs(
    ["Scatter plot", "Select points", "A Module 3 plot", "The data"]
)

with tab1:
    st.subheader("Upward mobility vs. income")
    scatter = alt.Chart(filtered).mark_circle(opacity=0.7).encode(
        x=alt.X("Income:Q", title="Average household income ($)"),
        y=alt.Y("Mobility:Q", title="Upward mobility"),
        size=alt.Size("Population:Q", scale=alt.Scale(range=[10, 400]), legend=None),
        color=alt.Color(f"{color_by}:N"),
        tooltip=["Name", "State", "Population", "Income", "Mobility"],
    ).properties(height=450).interactive()
    st.altair_chart(scatter)
    st.caption("Dot size = population.  Scroll to zoom, drag to pan, hover for details.")

with tab2:
    st.subheader("Drag a box to select regions")
    st.write(
        "Streamlit can send what you select in an Altair plot **back to Python**. "
        "Drag a box over some dots, and the table below shows just those regions."
    )
    brush = alt.selection_interval(name="brush")
    selectable = alt.Chart(filtered).mark_circle(size=60).encode(
        x="Income:Q",
        y="Mobility:Q",
        color=alt.condition(brush, alt.Color("State:N"), alt.value("lightgray")),
        tooltip=["Name", "State", "Mobility"],
    ).add_params(brush).properties(height=400)

    # on_select="rerun": re-run this script whenever the selection changes
    event = st.altair_chart(selectable, on_select="rerun")

    box = event.selection.get("brush", {}) if event else {}
    if box:
        picked = filtered[
            filtered["Income"].between(*box["Income"])
            & filtered["Mobility"].between(*box["Mobility"])
        ]
        st.write(f"**{len(picked)} regions selected** -- average mobility "
                 f"{picked['Mobility'].mean():.3f}")
        st.dataframe(picked, hide_index=True)
    else:
        st.info("Nothing selected yet -- drag a box on the plot.")

with tab3:
    st.subheader("Reusing a JSON file from Module 3")
    st.write(
        "Any vega-lite `.json` file saved with `chart.save(...)` can be shown with "
        "`st.vega_lite_chart`.  This one is in the same GitHub repository as this app."
    )
    json_file = Path(__file__).parent / "corgis_over_time.json"
    if json_file.exists():
        spec = json.loads(json_file.read_text())
        st.vega_lite_chart(spec)
    else:
        st.warning("Upload corgis_over_time.json next to streamlit_app.py to see this plot.")

with tab4:
    st.subheader("The filtered data")
    st.dataframe(filtered, hide_index=True)
    st.download_button(
        "Download as CSV", filtered.to_csv(index=False), file_name="mobility_filtered.csv"
    )

# -----------------------------------------------------------------------------
# 5. Write-up
# -----------------------------------------------------------------------------
st.header("What do you see?")
st.markdown(
    """
Replace this with a short write-up of your own: what should viewers notice,
and why did you choose these plots, colors and controls?  (See Module 2!)

Data: [mobility.csv](https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv)
from the IS445 course data repository.
"""
)

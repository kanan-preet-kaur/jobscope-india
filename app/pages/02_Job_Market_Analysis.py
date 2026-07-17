import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go


from utils.loader import load_data
from utils.theme import apply_page_config, inject_theme_css

from components.sidebar import render_sidebar
from components.metrics import metric_card



# =====================================
# PROJECT THEME
# SAME AS EDA NOTEBOOK
# =====================================


PRIMARY = "#6D28D9"
SECONDARY = "#8B5CF6"
ACCENT = "#A78BFA"

PINK = "#EC4899"
MAGENTA = "#D946EF"
INDIGO = "#4F46E5"
CYAN = "#06B6D4"


SUCCESS = "#22C55E"
WARNING = "#F59E0B"
DANGER = "#EF4444"


TEXT = "#0F172A"
MUTED = "#64748B"

GRID = "#E2E8F0"

FONT = "Arial"



# =====================================
# PLOT STYLE
# SAME AS EDA
# =====================================


def style_plot(fig):

    fig.update_layout(

        template="plotly_dark",

        plot_bgcolor="#0F172A",

        paper_bgcolor="#0F172A",


        font=dict(
            family=FONT,
            size=13,
            color="#F8FAFC"
        ),


        title=dict(

            x=0.5,

            xanchor="center",

            font=dict(
                size=20,
                family=FONT,
                color="#F8FAFC"
            )

        ),


        margin=dict(
            l=40,
            r=40,
            t=65,
            b=35
        ),


        hovermode="x unified",


        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            borderwidth=0
        )

    )


    fig.update_xaxes(

        showgrid=False,

        zeroline=False,

        showline=False,

        color="#CBD5E1"

    )


    fig.update_yaxes(

        showgrid=True,

        gridcolor="#334155",

        griddash="dot",

        gridwidth=0.8,

        zeroline=False,

        showline=False,

        color="#CBD5E1"

    )


    return fig



# =====================================
# INITIALIZATION
# =====================================


apply_page_config()

inject_theme_css()

render_sidebar()



# =====================================
# LOAD DATA
# =====================================


df = load_data()



# =====================================
# HERO SECTION
# =====================================


st.markdown(
"""
<div class="hero-section">


<h1>
💼 Job Market Analysis
</h1>


<p>

Exploring hiring trends, job demand,
salary ranges, and geographic patterns
across India's employment ecosystem.

</p>


</div>
""",
unsafe_allow_html=True
)



st.write("")



# =====================================
# PAGE INTRODUCTION
# =====================================


st.markdown(
"""
<div class="content-card">


<h3>
📌 What This Analysis Covers
</h3>


<p>

This section examines how opportunities
are distributed across job roles, locations,
and salary ranges.

The analysis highlights where hiring demand
is concentrated and what roles offer stronger
career opportunities.

</p>


</div>
""",
unsafe_allow_html=True
)



st.write("")

# =====================================
# JOB MARKET SNAPSHOT
# =====================================


st.markdown(
"""
<h2 class="section-heading">
📊 Job Market Snapshot
</h2>
""",
unsafe_allow_html=True
)



col1, col2, col3, col4 = st.columns(
    4,
    gap="large"
)



with col1:

    metric_card(
        "Total Job Listings",
        f"{len(df):,}",
        "💼"
    )



with col2:

    metric_card(
        "Unique Job Roles",
        f"{df['title'].nunique():,}",
        "👨‍💻"
    )



with col3:

    metric_card(
        "Locations Covered",
        f"{df['location'].nunique():,}",
        "📍"
    )



with col4:

    metric_card(
        "Companies Hiring",
        f"{df['companyName'].nunique():,}",
        "🏢"
    )



st.divider()



# =====================================
# JOB MARKET EXPLORER
# =====================================


st.markdown(
"""
<h2 class="section-heading">
🎛️ Job Market Explorer
</h2>
""",
unsafe_allow_html=True
)



filter_col1, filter_col2 = st.columns(
    2,
    gap="large"
)



with filter_col1:


    selected_locations = st.multiselect(

        "Select Locations",

        options=sorted(
            df["location"]
            .dropna()
            .unique()
        ),

        default=[]

    )



with filter_col2:


    selected_roles = st.multiselect(

        "Select Job Roles",

        options=sorted(
            df["title"]
            .dropna()
            .unique()
        ),

        default=[]

    )



filtered_df = df.copy()



if selected_locations:

    filtered_df = filtered_df[
        filtered_df["location"]
        .isin(selected_locations)
    ]



if selected_roles:

    filtered_df = filtered_df[
        filtered_df["title"]
        .isin(selected_roles)
    ]



st.divider()



# =====================================
# CHART 5
# MOST IN-DEMAND JOB TITLES
# EXACT EDA CODE
# =====================================


st.markdown(
"""
<h2 class="section-heading">
🔥 Most In-Demand Job Titles
</h2>
""",
unsafe_allow_html=True
)



top_jobs = (

    filtered_df["title"]

    .dropna()

    .str.strip()

    .value_counts()

    .head(10)

    .sort_values(
        ascending=True
    )

)



fig = px.bar(

    x=top_jobs.values,

    y=top_jobs.index,

    orientation="h",

    title="Top 10 Most In-Demand Job Titles",

    text=top_jobs.values,

    color=top_jobs.values,


    color_continuous_scale=[

        "#F3E8FF",

        "#E9D5FF",

        "#D8B4FE",

        "#C084FC",

        "#A855F7",

        "#9333EA",

        "#7E22CE",

        "#6B21A8",

        "#581C87"

    ]

)



fig.update_coloraxes(
    showscale=False
)



fig.update_traces(

    textposition="outside",

    cliponaxis=False,


    marker=dict(

        line=dict(

            color="white",

            width=0.8

        )

    ),


    hovertemplate=(

        "<b>%{y}</b><br>"

        "Job Postings: %{x:,}"

        "<extra></extra>"

    )

)



fig.update_xaxes(

    title="Number of Job Postings"

)



fig.update_yaxes(

    title="Job Title"

)



fig = style_plot(fig)



st.plotly_chart(

    fig,

    use_container_width=True

)

st.markdown(
"""
<div class="insight-box">


<div class="insight-header">

🔥 Hiring Demand Insight

</div>



<div class="insight-text">


Software engineering and development roles
dominate hiring activity across the dataset.


The demand pattern shows that a relatively
small group of technical roles contributes a
large share of employment opportunities.


<span class="highlight">
Core software roles remain among the strongest
career opportunities in India's technology market.
</span>


</div>


</div>
""",
unsafe_allow_html=True
)

# =====================================
# CHART 13
# SALARY RANGE SPREAD BY JOB TITLE
# EXACT EDA CODE
# =====================================


st.markdown(
"""
<h2 class="section-heading">
💰 Salary Range Spread by Job Title
</h2>
""",
unsafe_allow_html=True
)



salary_range = (

    filtered_df[

        (filtered_df["minimumSalary"] > 0) &

        (filtered_df["maximumSalary"] > 0)

    ]

    .groupby(
        "title",
        as_index=False
    )

    .agg(

        MinSalary=(
            "minimumSalary",
            "median"
        ),

        MaxSalary=(
            "maximumSalary",
            "median"
        ),

        Jobs=(
            "title",
            "count"
        )

    )

)



salary_range = (

    salary_range[

        salary_range["Jobs"] >= 20

    ]

    .sort_values(
        "MaxSalary",
        ascending=False
    )

    .head(12)

    .sort_values(
        "MinSalary"
    )

)



fig = go.Figure()



# Connecting line

fig.add_trace(

    go.Scatter(

        x=salary_range["MinSalary"],

        y=salary_range["title"],

        mode="lines",

        line=dict(

            color=MUTED,

            width=3

        ),

        showlegend=False,

        hoverinfo="skip"

    )

)



# Draw connectors

for _, row in salary_range.iterrows():

    fig.add_shape(

        type="line",

        x0=row["MinSalary"],

        x1=row["MaxSalary"],

        y0=row["title"],

        y1=row["title"],

        line=dict(

            color=MUTED,

            width=3

        )

    )





# Minimum salary points

fig.add_trace(

    go.Scatter(

        x=salary_range["MinSalary"],

        y=salary_range["title"],

        mode="markers",

        name="Minimum Salary",

        marker=dict(

            size=11,

            color=PRIMARY,

            line=dict(

                color="white",

                width=1

            )

        ),

        hovertemplate=

        "<b>%{y}</b><br>"

        "Minimum Salary: ₹%{x:,.0f}"

        "<extra></extra>"

    )

)





# Maximum salary points

fig.add_trace(

    go.Scatter(

        x=salary_range["MaxSalary"],

        y=salary_range["title"],

        mode="markers",

        name="Maximum Salary",

        marker=dict(

            size=11,

            color=CYAN,

            line=dict(

                color="white",

                width=1

            )

        ),


        hovertemplate=

        "<b>%{y}</b><br>"

        "Maximum Salary: ₹%{x:,.0f}"

        "<extra></extra>"

    )

)





# Salary axis in Lakhs

max_salary = salary_range["MaxSalary"].max()



tick_step = 500000



tick_vals = np.arange(

    0,

    max_salary + tick_step,

    tick_step

)



tick_text = [

    f"₹{int(x/100000)}L"

    for x in tick_vals

]





fig.update_xaxes(

    title="Salary (INR)",

    tickmode="array",

    tickvals=tick_vals,

    ticktext=tick_text

)



fig.update_yaxes(

    title="Job Title"

)



fig.update_layout(

    title="Salary Range Spread by Job Title"

)



fig = style_plot(fig)



st.plotly_chart(

    fig,

    use_container_width=True

)

st.markdown(
"""
<div class="insight-box">


<div class="insight-header">

💎 Salary Potential Insight

</div>



<div class="insight-text">


Senior technical and architecture-focused
roles demonstrate significantly wider salary
ranges compared with general development
positions.


Roles with larger compensation spreads
indicate greater opportunity for salary growth
through experience, specialization, and
advanced expertise.


<span class="highlight">
Higher responsibility roles unlock stronger
earning potential.
</span>


</div>


</div>
""",
unsafe_allow_html=True
)



# =====================================
# JOB MARKET ANALYSIS SUMMARY
# =====================================

st.divider()

st.markdown(
"""
<h2 class="section-heading">
📌 Job Market Analysis Summary
</h2>
""",
unsafe_allow_html=True
)


col1, col2 = st.columns(2, gap="large")


with col1:

    st.markdown(
    """
    <div class="insight-box">

    <div class="insight-header">
    📍 Hiring Distribution
    </div>

    <div class="insight-text">

    • Job opportunities are concentrated across
    major employment hubs in India.

    • Metropolitan locations continue to dominate
    overall hiring activity.

    • Regional differences highlight variations in
    job availability and market demand.

    </div>

    </div>
    """,
    unsafe_allow_html=True
    )



with col2:

    st.markdown(
    """
    <div class="insight-box">

    <div class="insight-header">
    💼 Top Job Opportunities
    </div>

    <div class="insight-text">

    • Certain job roles contribute significantly
    to overall hiring demand.

    • Technology, management, and specialised roles
    remain among the most visible opportunities.

    • Market demand varies strongly by role and
    industry requirements.

    </div>

    </div>
    """,
    unsafe_allow_html=True
    )



col3, col4 = st.columns(2, gap="large")



with col3:

    st.markdown(
    """
    <div class="insight-box">

    <div class="insight-header">
    🏢 Market Concentration
    </div>

    <div class="insight-text">

    • Hiring demand is distributed across a wide
    range of companies.

    • A small group of organisations contribute
    significantly to visible job postings.

    • Company hiring patterns reveal differences
    in workforce requirements.

    </div>

    </div>
    """,
    unsafe_allow_html=True
    )



with col4:

    st.markdown(
    """
    <div class="insight-box">

    <div class="insight-header">
    🎯 Key Takeaway
    </div>

    <div class="insight-text">

    The Indian job market is driven by location,
    role demand, and organisational hiring trends.

    Understanding these patterns helps candidates
    identify stronger career opportunities and
    align their skills with market needs.

    </div>

    </div>
    """,
    unsafe_allow_html=True
    )
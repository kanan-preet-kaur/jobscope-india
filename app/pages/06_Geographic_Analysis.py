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
# PLOT STYLE FUNCTION
# SAME AS OTHER PAGES
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
# GEOGRAPHIC DATASET
# =====================================

geo_df = df.copy()

# =====================================
# HERO SECTION
# =====================================

st.markdown(
"""
<div class="hero-section">

<h1>
🌍 Geographic Analysis
</h1>

<p>

Discover how employment opportunities are
distributed across India's major cities and
technology hubs.

Explore regional hiring trends, salary
distribution, and the geographic concentration
of jobs across thousands of postings.

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

This section explores the geographical
distribution of job opportunities across the
Indian job market.

The analysis identifies leading hiring cities,
regional salary patterns, and how employment
opportunities are concentrated across different
locations.

</p>

</div>
""",
unsafe_allow_html=True
)

st.write("")


# =====================================
# GEOGRAPHIC SNAPSHOT
# =====================================

st.markdown(
"""
<h2 class="section-heading">
📊 Geographic Snapshot
</h2>
""",
unsafe_allow_html=True
)

location_counts = df["location"].value_counts()

top_city = location_counts.idxmax()

average_jobs = location_counts.mean()

col1, col2, col3, col4 = st.columns(
    4,
    gap="large"
)

with col1:

    metric_card(
        "Locations",
        f"{df['location'].nunique():,}",
        "🌍"
    )

with col2:

    metric_card(
        "Top Hiring City",
        top_city,
        "🏙️"
    )

with col3:

    metric_card(
        "Largest Market",
        f"{location_counts.max():,}",
        "📈"
    )

with col4:

    metric_card(
        "Average Jobs / City",
        f"{average_jobs:.0f}",
        "📑"
    )

st.divider()


# =====================================
# ANALYSIS INTRO
# =====================================

st.markdown(
"""
<div class="section-banner">

<h3>
🌍 Geographic Intelligence
</h3>

<p>

The following analysis highlights regional
hiring activity, city-wise employment trends,
and geographic salary distribution using
cleaned job market data.

</p>

</div>
""",
unsafe_allow_html=True
)

st.divider()

# =====================================
# CHART 4
# HIRING SHARE BY TOP LOCATIONS
# FROM EDA NOTEBOOK
# =====================================

st.markdown(
"""
<h2 class="section-heading">
🌍 Hiring Share by Top Locations
</h2>
""",
unsafe_allow_html=True
)

location_share = (
    df["location"]
    .value_counts()
    .head(8)
)

fig = px.pie(
    values=location_share.values,
    names=location_share.index,
    title="Hiring Share by Top Locations",
    hole=0.42,
    color_discrete_sequence=[
        "#312E81",
        "#4338CA",
        "#4F46E5",
        "#6366F1",
        "#818CF8",
        "#A5B4FC",
        "#C7D2FE",
        "#E0E7FF"
    ]
)

fig.update_traces(
    textposition="inside",
    textinfo="percent+label",
    textfont=dict(
        size=11,
        color="white"
    ),
    marker=dict(
        line=dict(
            color="white",
            width=2
        )
    ),
    hovertemplate=(
        "<b>%{label}</b><br>"
        "Job Postings: %{value:,}<br>"
        "Share: %{percent}"
        "<extra></extra>"
    )
)

fig = style_plot(fig)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={
        "displayModeBar": False
    }
)

st.markdown(
"""
<div class="insight-box">

<div class="insight-header">

🌍 Geographic Hiring Insight

</div>

<div class="insight-text">

Bengaluru accounts for the largest share of
job postings, reaffirming its position as
India's leading technology hub.

Hyderabad, Pune, Chennai and Mumbai
collectively contribute a significant
proportion of total hiring activity.

<span class="highlight">

Employment opportunities remain heavily
concentrated in metropolitan cities with
mature IT ecosystems.

</span>

Regional hiring patterns highlight the
dominance of established technology and
business centers.

</div>

</div>
""",
unsafe_allow_html=True
)

st.write("")

# =====================================
# CHART 14
# LOCATION VS MOST DEMANDED SKILLS
# FROM EDA NOTEBOOK
# =====================================

st.markdown(
"""
<h2 class="section-heading">
🌍 Location vs Most Demanded Skills
</h2>
""",
unsafe_allow_html=True
)

skills_df = df[["location", "tagsAndSkills"]].copy()

skills_df = skills_df.dropna()

skills_df["tagsAndSkills"] = (
    skills_df["tagsAndSkills"]
    .astype(str)
    .str.split(",")
)

skills_df = skills_df.explode("tagsAndSkills")

skills_df["tagsAndSkills"] = (
    skills_df["tagsAndSkills"]
    .astype(str)
    .str.strip()
)

skills_df = skills_df[
    skills_df["tagsAndSkills"] != ""
]

top_locations = (
    skills_df["location"]
    .value_counts()
    .head(10)
    .index
)

top_skills = (
    skills_df["tagsAndSkills"]
    .value_counts()
    .head(15)
    .index
)

filtered_skills = skills_df[
    skills_df["location"].isin(top_locations)
    &
    skills_df["tagsAndSkills"].isin(top_skills)
]

heatmap_data = (
    filtered_skills
    .groupby(
        ["location", "tagsAndSkills"]
    )
    .size()
    .unstack(fill_value=0)
)

fig = px.imshow(

    heatmap_data,

    text_auto="d",

    color_continuous_scale="PuRd",

    aspect="auto",

    labels=dict(

        x="Skill",

        y="Location",

        color="Job Postings"

    )

)

fig.update_layout(

    title_text="Location vs Most Demanded Skills",

    title_x=0.5,

    xaxis_title="Skill",

    yaxis_title="Location",

    xaxis_tickangle=45,

    coloraxis_colorbar=dict(
        len=0.75
    )

)

fig.update_traces(

    xgap=0.5,

    ygap=0.5,

    hoverongaps=False

)

fig = style_plot(fig)

st.plotly_chart(

    fig,

    use_container_width=True,

    config={
        "displayModeBar": False
    }

)

st.markdown(
"""
<div class="insight-box">

<div class="insight-header">

🌍 Regional Skills Insight

</div>

<div class="insight-text">

Major technology hubs exhibit the widest variety
of technical skills demanded by employers.

Certain cities demonstrate specialization in
specific technologies, reflecting regional
industry ecosystems.

<span class="highlight">

Metropolitan areas consistently advertise a
broader technology stack than smaller cities,
helping job seekers align skill development
with preferred work locations.

</span>

</div>

</div>
""",
unsafe_allow_html=True
)

st.write("")

# =====================================
# GEOGRAPHIC ANALYSIS SUMMARY
# =====================================

st.divider()

st.markdown(
"""
<h2 class="section-heading">
📌 Geographic Analysis Summary
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

    🌆 Hiring Hotspots

    </div>

    <div class="insight-text">

    India's technology recruitment is heavily
    concentrated in metropolitan cities,
    particularly Bengaluru, Hyderabad,
    Pune, Chennai, and Mumbai.

    These cities continue to drive the
    country's employment landscape.

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

    📈 Regional Opportunities

    </div>

    <div class="insight-text">

    While leading technology hubs dominate
    recruitment, opportunities are gradually
    expanding across additional cities as
    organizations broaden their geographic
    presence.

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

    🛠 Regional Skill Demand

    </div>

    <div class="insight-text">

    Different cities exhibit distinct
    technology preferences, reflecting
    specialized industry ecosystems and
    local employer requirements.

    Understanding these patterns helps
    professionals target relevant skills.

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

    Geographic location remains an important
    factor in India's job market, influencing
    hiring volume, technology demand, and
    career opportunities.

    Aligning skills with regional hiring
    trends can significantly improve career
    prospects.

    </div>

    </div>
    """,
    unsafe_allow_html=True
    )
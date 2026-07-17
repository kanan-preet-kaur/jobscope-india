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
# SAME AS EDA NOTEBOOK
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
# EXPERIENCE DATASET
# SAME FILTERING AS EDA NOTEBOOK
# =====================================

experience_df = df[
    df["averageExperience"] >= 0
].copy()


# =====================================
# HERO SECTION
# =====================================

st.markdown(
"""
<div class="hero-section">

<h1>
👨‍💼 Experience Analysis
</h1>

<p>

Explore how professional experience influences
hiring demand, salary progression, and career
opportunities across India's evolving job market.

Discover hiring trends across experience levels,
salary growth over time, and the relationship
between experience and compensation.

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

This section explores the role of professional
experience in shaping recruitment trends across
the Indian job market.

The analysis examines hiring demand across
experience levels, salary progression with
experience, and the relationship between
professional expertise and compensation.

</p>

</div>
""",
unsafe_allow_html=True
)

st.write("")


# =====================================
# EXPERIENCE SNAPSHOT
# =====================================

st.markdown(
"""
<h2 class="section-heading">
📊 Experience Snapshot
</h2>
""",
unsafe_allow_html=True
)

experience_df = df[
    df["averageExperience"] >= 0
].copy()

experience_counts = (
    experience_df["averageExperience"]
    .value_counts()
    .sort_index()
)

most_common_experience = (
    experience_counts.idxmax()
)

highest_experience = (
    experience_df["averageExperience"]
    .max()
)

average_experience = (
    experience_df["averageExperience"]
    .mean()
)

col1, col2, col3, col4 = st.columns(
    4,
    gap="large"
)

with col1:

    metric_card(
        "Average Experience",
        f"{average_experience:.1f} Yrs",
        "👨‍💼"
    )

with col2:

    metric_card(
        "Most Common",
        f"{int(most_common_experience)} Yrs",
        "📈"
    )

with col3:

    metric_card(
        "Maximum Experience",
        f"{int(highest_experience)} Yrs",
        "🚀"
    )

with col4:

    metric_card(
        "Job Records",
        f"{len(experience_df):,}",
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
👨‍💼 Experience Intelligence
</h3>

<p>

The following analysis highlights hiring demand,
career progression, and salary growth across
different experience levels using cleaned job
market data.

</p>

</div>
""",
unsafe_allow_html=True
)

st.divider()

# =====================================
# CHART 10
# JOB POSTINGS BY EXPERIENCE LEVEL
# FROM EDA NOTEBOOK
# =====================================

st.markdown(
"""
<h2 class="section-heading">
📈 Job Postings by Experience Level
</h2>
""",
unsafe_allow_html=True
)

experience_df = df.copy()

experience_df["ExperienceGroup"] = pd.cut(
    experience_df["averageExperience"],
    bins=[0, 2, 5, 8, 12, 50],
    labels=[
        "0–2 Years",
        "3–5 Years",
        "6–8 Years",
        "9–12 Years",
        "12+ Years"
    ]
)

job_counts = (
    experience_df["ExperienceGroup"]
    .value_counts(sort=False)
    .reset_index()
)

job_counts.columns = [
    "Experience Level",
    "Job Postings"
]

fig = px.bar(
    job_counts,
    x="Experience Level",
    y="Job Postings",
    text="Job Postings",
    color="Job Postings",
    color_continuous_scale=[
        "#ECFEFF",
        "#CFFAFE",
        "#A5F3FC",
        "#67E8F9",
        "#22D3EE",
        "#06B6D4",
        "#0891B2"
    ],
    title="Job Postings by Experience Level"
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
        "<b>%{x}</b><br>"
        "Job Postings: %{y:,}"
        "<extra></extra>"
    )
)

fig.update_xaxes(
    title="Experience Level"
)

fig.update_yaxes(
    title="Job Postings"
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

📈 Experience Demand Insight

</div>

<div class="insight-text">

Mid-level experience requirements account for
the largest proportion of job postings.

Entry-level opportunities exist but represent
a smaller share of the overall market.

Demand gradually shifts toward experienced
professionals as organizational complexity
increases.

<span class="highlight">

The market currently favors candidates with
several years of practical industry experience.

</span>

</div>

</div>
""",
unsafe_allow_html=True
)

st.write("")

# =====================================
# CHART 15
# SALARY DISTRIBUTION ACROSS EXPERIENCE LEVELS
# FROM EDA NOTEBOOK
# =====================================

st.markdown(
"""
<h2 class="section-heading">
💰 Salary Distribution Across Experience Levels
</h2>
""",
unsafe_allow_html=True
)

experience_salary = df[
    (df["maximumSalary"] > 0)
].copy()

experience_salary["maximumSalaryLakhs"] = (
    experience_salary["maximumSalary"] / 100000
)

experience_salary["Experience Bracket"] = pd.cut(
    experience_salary["averageExperience"],
    bins=[0, 2, 5, 8, 12, 50],
    labels=[
        "0–2 Years",
        "3–5 Years",
        "6–8 Years",
        "9–12 Years",
        "12+ Years"
    ],
    include_lowest=True
)

fig = px.box(
    experience_salary,
    x="Experience Bracket",
    y="maximumSalaryLakhs",
    color="Experience Bracket",
    category_orders={
        "Experience Bracket": [
            "0–2 Years",
            "3–5 Years",
            "6–8 Years",
            "9–12 Years",
            "12+ Years"
        ]
    },
    color_discrete_sequence=[
        "#CFFAFE",
        "#A5F3FC",
        "#67E8F9",
        "#22D3EE",
        "#0891B2"
    ],
    points=False,
    title="Salary Distribution Across Experience Levels"
)

fig.update_traces(
    line=dict(width=2),
    marker=dict(
        line=dict(
            color="white",
            width=1
        )
    ),
    hovertemplate=(
        "<b>%{x}</b><br>"
        "Maximum Salary: ₹%{y:.1f}L"
        "<extra></extra>"
    )
)

fig.update_xaxes(
    title="Experience"
)

fig.update_yaxes(
    title="Maximum Salary (Lakhs INR)",
    range=[0, 60]
)

fig.update_layout(
    showlegend=False
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

💰 Salary Progression Insight

</div>

<div class="insight-text">

Salary ceilings generally increase as
professional experience grows, confirming
experience as a major driver of compensation.

The growth rate becomes less pronounced at
higher experience levels, suggesting diminishing
salary gains after reaching senior positions.

Considerable variation exists among professionals
with similar experience, indicating that
<span class="highlight">

specialization, company, and role

</span>

also influence compensation levels.

</div>

</div>
""",
unsafe_allow_html=True
)

# =====================================
# EXPERIENCE ANALYSIS SUMMARY
# =====================================

st.divider()

st.markdown(
"""
<h2 class="section-heading">
📌 Experience Analysis Summary
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

    👨‍💼 Hiring Trends

    </div>

    <div class="insight-text">

    Recruitment demand is concentrated around
    professionals with a few years of industry
    experience, reflecting employers' preference
    for candidates capable of contributing with
    minimal onboarding.

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

    💰 Salary Growth

    </div>

    <div class="insight-text">

    Compensation generally increases alongside
    professional experience, with the most
    significant salary progression occurring
    after candidates move beyond entry-level
    positions.

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

    📈 Market Variability

    </div>

    <div class="insight-text">

    Professionals with similar years of
    experience often receive substantially
    different salaries, highlighting the impact
    of specialization, employer, and job role
    on compensation.

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

    Experience remains one of the strongest
    predictors of hiring demand and earning
    potential, but continuous skill development
    and specialization play an equally important
    role in maximizing career growth.

    </div>

    </div>
    """,
    unsafe_allow_html=True
    )

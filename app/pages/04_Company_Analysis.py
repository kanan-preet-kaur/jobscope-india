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

PRIMARY="#6D28D9"
SECONDARY="#8B5CF6"
ACCENT="#A78BFA"

PINK="#EC4899"
MAGENTA="#D946EF"
INDIGO="#4F46E5"
CYAN="#06B6D4"

SUCCESS="#22C55E"
WARNING="#F59E0B"
DANGER="#EF4444"

TEXT="#0F172A"
MUTED="#64748B"

GRID="#E2E8F0"

FONT="Arial"

# =====================================
# PLOT STYLE
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

df=load_data()
# =====================================
# HERO SECTION
# =====================================

st.markdown(
"""
<div class="hero-section">

<h1>
🏢 Company Analysis
</h1>

<p>

Discover the organizations, hiring leaders,
and employer trends shaping India's evolving
job market.

Explore the most reviewed companies, hiring
market share, and regional skill demand across
thousands of job postings.

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

This section explores employer hiring activity
and company presence across the Indian job
market.

The analysis identifies the most reviewed
organizations, recruitment market share,
and regional demand for skills across
different locations.

</p>

</div>
""",
unsafe_allow_html=True
)

st.write("")


# =====================================
# COMPANY SNAPSHOT
# =====================================

st.markdown(
"""
<h2 class="section-heading">
📊 Company Snapshot
</h2>
""",
unsafe_allow_html=True
)

company_counts = df["companyName"].value_counts()

review_df = (
    df.groupby("companyName")
    .agg(
        AvgReviews=("ReviewsCount", "mean"),
        Jobs=("companyName", "count")
    )
    .reset_index()
)

top_recruiter = company_counts.idxmax()

most_reviewed = (
    review_df
    .sort_values("AvgReviews", ascending=False)
    .iloc[0]["companyName"]
)

largest_market_share = company_counts.idxmax()

col1, col2, col3, col4 = st.columns(
    4,
    gap="large"
)

with col1:

    metric_card(
        "Companies",
        f"{df['companyName'].nunique():,}",
        "🏢"
    )

with col2:

    metric_card(
        "Top Recruiter",
        top_recruiter,
        "📈"
    )

with col3:

    metric_card(
        "Most Reviewed",
        most_reviewed,
        "⭐"
    )

with col4:

    metric_card(
        "Largest Recruiter",
        largest_market_share,
        "👑"
    )

st.divider()


# =====================================
# ANALYSIS INTRO
# =====================================

st.markdown(
"""
<div class="section-banner">

<h3>
🏢 Company Intelligence
</h3>

<p>

The following analysis highlights employer
reputation, recruitment dominance, and regional
hiring patterns using cleaned job market data.

</p>

</div>
""",
unsafe_allow_html=True
)

st.divider()

# =====================================
# CHART 6
# MOST HEAVILY REVIEWED COMPANIES
# FROM EDA NOTEBOOK
# =====================================

st.markdown(
"""
<h2 class="section-heading">
⭐ Most Heavily Reviewed Companies
</h2>
""",
unsafe_allow_html=True
)

company_reviews = (
    df.groupby("companyName", as_index=False)
      .agg(
          ReviewsCount=("ReviewsCount", "mean")
      )
      .sort_values("ReviewsCount", ascending=False)
      .head(15)
)

company_reviews["ReviewsCount"] = pd.to_numeric(
    company_reviews["ReviewsCount"],
    errors="coerce"
)

fig = px.treemap(

    company_reviews,

    path=["companyName"],

    values="ReviewsCount",

    color="ReviewsCount",

    color_continuous_scale=[
        "#EDE9FE",
        "#DDD6FE",
        "#C4B5FD",
        "#A78BFA",
        "#8B5CF6",
        "#7C3AED",
        "#6D28D9"
    ],

    title="Most Heavily Reviewed Companies"

)

fig.update_traces(

    textinfo="label+value",

    marker=dict(
        line=dict(
            color="white",
            width=2
        )
    ),

    hovertemplate=(

        "<b>%{label}</b><br>"

        "Average Reviews: %{value:,.0f}"

        "<extra></extra>"

    )

)

fig.update_coloraxes(
    showscale=False
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

⭐ Company Reputation Insight

</div>

<div class="insight-text">

Large organizations receive substantially more
employee reviews than smaller companies.

Companies such as
<span class="highlight">

TCS, Accenture and Infosys

</span>

demonstrate strong employer visibility due to
their large workforce.

Higher review counts generally indicate more
established organizations with greater hiring
activity, while employer reputation data is
considerably richer for large enterprises than
for smaller firms.

</div>

</div>
""",
unsafe_allow_html=True
)

st.write("")

# =====================================
# CHART 12
# MARKET SHARE OF JOB POSTINGS
# FROM EDA NOTEBOOK
# =====================================

st.markdown(
"""
<h2 class="section-heading">
📊 Market Share of Job Postings
</h2>
""",
unsafe_allow_html=True
)

company_jobs = (
    df.groupby("companyName")
      .agg(
          JobPostings=("companyName", "count"),
          Reviews=("ReviewsCount", "mean")
      )
      .reset_index()
)

company_jobs["Company Size"] = np.where(
    company_jobs["Reviews"] >= company_jobs["Reviews"].median(),
    "Large Companies",
    "Smaller Companies"
)

market_share = (
    company_jobs.groupby("Company Size")["JobPostings"]
    .sum()
    .reset_index()
)

fig = px.pie(

    market_share,

    names="Company Size",

    values="JobPostings",

    hole=0.55,

    color="Company Size",

    color_discrete_map={
        "Large Companies": INDIGO,
        "Smaller Companies": ACCENT
    },

    title="Market Share of Job Postings"

)

fig.update_traces(

    textposition="inside",

    textinfo="percent+label",

    marker=dict(
        line=dict(
            color="white",
            width=2
        )
    ),

    hovertemplate=(

        "<b>%{label}</b><br>"

        "Job Postings: %{value:,}<br>"

        "Market Share: %{percent}"

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

📊 Market Share Insight

</div>

<div class="insight-text">

Large organizations contribute a substantial
proportion of total job postings, demonstrating
their continued dominance in the hiring market.

Smaller companies collectively represent a
meaningful share of employment opportunities,
despite posting fewer jobs individually.

<span class="highlight">

The Indian technology job market maintains a
healthy balance between established enterprises
and emerging businesses.

</span>

Job seekers should consider both segments, as
large firms provide hiring volume while smaller
companies often offer specialized roles and
faster career growth.

</div>

</div>
""",
unsafe_allow_html=True
)

st.write("")



# =====================================
# COMPANY ANALYSIS SUMMARY
# =====================================

st.divider()

st.markdown(
"""
<h2 class="section-heading">
📌 Company Analysis Summary
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

    🏢 Recruitment Leaders

    </div>

    <div class="insight-text">

    Large organizations dominate India's hiring
    landscape, contributing the majority of job
    opportunities while maintaining strong
    employer visibility through extensive
    employee reviews.

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

    ⭐ Employer Reputation

    </div>

    <div class="insight-text">

    Companies with higher review volumes are
    generally well-established organizations,
    providing richer employer insights and
    stronger indicators of workplace reputation.

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

    🌍 Regional Hiring Patterns

    </div>

    <div class="insight-text">

    Major metropolitan cities exhibit broader
    technology demand, while different regions
    develop distinct hiring preferences and
    specialized skill ecosystems.

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

    India's recruitment landscape is shaped by
    established enterprises, diverse regional
    talent hubs, and evolving skill demands,
    offering opportunities across both large
    corporations and emerging companies.

    </div>

    </div>
    """,
    unsafe_allow_html=True
    )
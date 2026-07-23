import streamlit as st

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.warning("Please register/login to access the dashboard.")
    st.switch_page("pages/00_Authentication.py")

import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

from itertools import combinations

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
# HERO SECTION
# =====================================

st.markdown(
"""
<div class="hero-section">

<h1>
🛠 Skills Analysis
</h1>

<p>

Discover the technologies, programming languages,
frameworks, and professional competencies driving
India's evolving job market.

Explore the most demanded skills, highest-paying
technologies, and relationships between skills
across thousands of job postings.

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

This section explores employer demand for
technical and professional skills across the
Indian job market.

The analysis identifies the most frequently
requested skills, the technologies associated
with premium salaries, and common skill
combinations appearing together in job postings.

</p>

</div>
""",
unsafe_allow_html=True
)

st.write("")
st.divider()


# =====================================
# SKILLS SNAPSHOT
# =====================================

st.markdown(
"""
<h2 class="section-heading">
📊 Skills Snapshot
</h2>
""",
unsafe_allow_html=True
)

skills = (
    df["tagsAndSkills"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
)

skill_counts = skills.value_counts()

skill_salary = (
    df[
        (df["maximumSalary"] > 0) &
        (df["tagsAndSkills"].notna())
    ][["tagsAndSkills","maximumSalary"]]
    .copy()
)

skill_salary["tagsAndSkills"] = (
    skill_salary["tagsAndSkills"]
    .str.split(",")
)

skill_salary = skill_salary.explode("tagsAndSkills")

skill_salary["tagsAndSkills"] = (
    skill_salary["tagsAndSkills"]
    .str.strip()
)

skill_salary = (
    skill_salary
    .groupby("tagsAndSkills", as_index=False)
    .agg(
        MedianSalary=("maximumSalary","median"),
        Jobs=("tagsAndSkills","count")
    )
)

skill_salary = skill_salary[
    skill_salary["Jobs"] >= 20
]

highest_paying_skill = (
    skill_salary
    .sort_values("MedianSalary",ascending=False)
    .iloc[0]["tagsAndSkills"]
)

col1,col2,col3,col4 = st.columns(
    4,
    gap="large"
)

with col1:

    metric_card(
        "Unique Skills",
        f"{skills.nunique():,}",
        "🛠"
    )

with col2:

    metric_card(
        "Skill Mentions",
        f"{len(skills):,}",
        "📈"
    )

with col3:

    metric_card(
        "Most Requested",
        skill_counts.idxmax(),
        "🏆"
    )

with col4:

    metric_card(
        "Highest Paying",
        highest_paying_skill,
        "💰"
    )

st.divider()
st.write("")


# =====================================
# CHART 8
# MOST FREQUENTLY DEMANDED SKILLS
# FROM EDA NOTEBOOK
# =====================================

st.markdown(
"""
<h2 class="section-heading">
🛠 Most Frequently Demanded Skills
</h2>
""",
unsafe_allow_html=True
)

skills = (
    df["tagsAndSkills"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
)

top_skills = (
    skills.value_counts()
    .head(15)
    .sort_values(ascending=True)
)

fig = px.bar(

    x=top_skills.values,

    y=top_skills.index,

    orientation="h",

    title="Most Frequently Demanded Skills",

    text=top_skills.values,

    color=top_skills.values,

    color_continuous_scale=[
        "#FCE7F3",
        "#FBCFE8",
        "#F9A8D4",
        "#F472B6",
        "#EC4899",
        "#DB2777",
        "#BE185D"
    ]

)

fig.update_coloraxes(
    showscale=False
)

fig.update_xaxes(
    title="Number of Job Postings"
)

fig.update_yaxes(
    title="Skill"
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

fig = style_plot(fig)

st.plotly_chart(
    fig,
    use_container_width=True,
    config={
        "displayModeBar": False
    }
)

# =====================================
# INSIGHT
# =====================================

st.markdown(
"""
<div class="insight-box">

<div class="insight-header">

🛠 Skills Demand Insight

</div>

<div class="insight-text">

Employer demand is concentrated around a relatively
small group of technical and professional skills.

Core technologies and business competencies appear
consistently across thousands of job postings,
indicating that these skills form the foundation
of today's employment landscape.

<span class="highlight">

Building expertise in these high-demand skills
can significantly improve employability across
multiple industries.

</span>

</div>

</div>
""",
unsafe_allow_html=True
)

st.write("")



# =====================================
# CHART 11
# MOST FREQUENTLY CO-OCCURRING SKILLS
# FROM EDA NOTEBOOK
# =====================================

st.markdown(
"""
<h2 class="section-heading">
🔥 Most Frequently Co-occurring Skills
</h2>
""",
unsafe_allow_html=True
)

# DATA PROCESSING

skill_df = (
    df["tagsAndSkills"]
    .dropna()
    .str.split(",")
)

pairs = []

for skills in skill_df:

    skills = list(
        set(
            [s.strip() for s in skills if s.strip()]
        )
    )

    pairs.extend(
        combinations(skills, 2)
    )

pair_df = (
    pd.DataFrame(
        pairs,
        columns=["Skill1", "Skill2"]
    )
    .value_counts()
    .reset_index(name="Count")
)

top_skills = (
    pd.concat(
        [
            pair_df["Skill1"],
            pair_df["Skill2"]
        ]
    )
    .value_counts()
    .head(12)
    .index
)

pair_df = pair_df[
    pair_df["Skill1"].isin(top_skills)
    &
    pair_df["Skill2"].isin(top_skills)
]

co_matrix = pd.pivot_table(
    pair_df,
    values="Count",
    index="Skill1",
    columns="Skill2",
    fill_value=0
)

co_matrix = co_matrix.add(
    co_matrix.T,
    fill_value=0
)

for skill in co_matrix.index:
    co_matrix.loc[skill, skill] = 0


# PLOTLY HEATMAP

fig = px.imshow(

    co_matrix,

    text_auto=".0f",

    color_continuous_scale="RdPu",

    aspect="auto"

)

fig.update_layout(

    title={

        "text":"Most Frequently Co-occurring Skills",

        "x":0.5,

        "font":dict(
            size=20,
            family="Arial"
        )

    },

    xaxis=dict(

        title="Skill",

        tickfont=dict(size=9)

    ),

    yaxis=dict(

        title="Skill",

        tickfont=dict(size=9)

    ),

    coloraxis_colorbar=dict(
        len=0.75
    )

)

fig = style_plot(fig)

st.plotly_chart(

    fig,

    use_container_width=True,

    config={
        "displayModeBar":False
    }

)

# =====================================
# INSIGHT
# =====================================

st.markdown(
"""
<div class="insight-box">

<div class="insight-header">

🔥 Skill Relationship Insight

</div>

<div class="insight-text">

Employers increasingly seek combinations of
complementary technologies rather than expertise
in a single tool.

Frequently co-occurring skills reveal the
technology stacks most commonly demanded across
industries.

<span class="highlight">

Learning related technologies together can
significantly improve employability and prepare
candidates for modern software development,
analytics, and enterprise roles.

</span>

</div>

</div>
""",
unsafe_allow_html=True
)

st.write("")

# =====================================
# CHART 9
# HIGHEST PAYING SKILLS
# FROM EDA NOTEBOOK
# =====================================

st.markdown(
"""
<h2 class="section-heading">
💰 Highest Paying Skills
</h2>
""",
unsafe_allow_html=True
)

skill_salary = (
    df[
        (df["maximumSalary"] > 0) &
        (df["tagsAndSkills"].notna())
    ][["tagsAndSkills", "maximumSalary"]]
    .copy()
)

skill_salary["tagsAndSkills"] = (
    skill_salary["tagsAndSkills"]
    .str.split(",")
)

skill_salary = skill_salary.explode("tagsAndSkills")

skill_salary["tagsAndSkills"] = (
    skill_salary["tagsAndSkills"]
    .str.strip()
)

skill_salary = (
    skill_salary
    .groupby("tagsAndSkills", as_index=False)
    .agg(
        medianSalary=("maximumSalary", "median"),
        jobs=("tagsAndSkills", "count")
    )
)

skill_salary = skill_salary[
    skill_salary["jobs"] >= 20
]

skill_salary = (
    skill_salary
    .sort_values("medianSalary", ascending=False)
    .head(15)
    .sort_values("medianSalary")
)

skill_salary["SalaryLabel"] = (
    "₹" +
    (skill_salary["medianSalary"]/100000)
    .round(1)
    .astype(str)
    + "L"
)

fig = px.bar(

    skill_salary,

    x="medianSalary",

    y="tagsAndSkills",

    orientation="h",

    text="SalaryLabel",

    color="medianSalary",

    color_continuous_scale=[
        "#FCE7F3",
        "#FBCFE8",
        "#F9A8D4",
        "#F472B6",
        "#EC4899",
        "#DB2777",
        "#BE185D"
    ],

    title="Highest Paying Skills"

)

fig.update_coloraxes(
    showscale=False
)

max_salary = skill_salary["medianSalary"].max()

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

    title="Median Maximum Salary (INR)",

    tickmode="array",

    tickvals=tick_vals,

    ticktext=tick_text

)

fig.update_yaxes(
    title="Skill"
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

        "Median Salary: ₹%{x:,.0f}<br>"

        "Job Postings: %{customdata[0]:,}"

        "<extra></extra>"

    ),

    customdata=skill_salary[["jobs"]]

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

💰 Highest Paying Skills Insight

</div>

<div class="insight-text">

Medical specializations dominate the highest-paying
skills, with <span class="highlight">Interventional
Cardiology</span> offering the highest median salary
ceiling.

Specialized healthcare skills consistently command
higher salary ceilings than most technical and
professional skills.

Emerging AI skills such as
<span class="highlight">LLMs</span> and
<span class="highlight">PyTorch</span>
also appear among the highest-paying skills,
reflecting growing demand for advanced AI expertise.

The chart highlights that niche, specialized skills
generally offer significantly higher earning
potential than broad, general-purpose competencies.

</div>

</div>
""",
unsafe_allow_html=True
)



# =====================================
# SKILLS ANALYSIS SUMMARY
# =====================================

st.divider()

st.markdown(
"""
<h2 class="section-heading">
📌 Skills Analysis Summary
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
    🚀 Most In-Demand Skills
    </div>

    <div class="insight-text">

    • Sales and Management dominate overall demand.

    • Python is the most requested technical skill.

    • SQL, SAP, CSS, Java and C# consistently
    appear across thousands of job postings.

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
    💰 Highest Paying Skills
    </div>

    <div class="insight-text">

    • Medical specializations offer the highest
    salary ceilings.

    • LLMs and PyTorch rank among the highest
    paying AI skills.

    • Specialized expertise commands premium
    compensation.

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
    🔗 Skill Relationships
    </div>

    <div class="insight-text">

    • Employers rarely hire for isolated skills.

    • Modern technology stacks require multiple
    complementary technologies.

    • Learning related skills together improves
    employability.

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

    The strongest career outcomes come from
    combining high-demand technologies with
    specialized expertise and complementary
    skill sets.

    </div>

    </div>
    """,
    unsafe_allow_html=True
    )   
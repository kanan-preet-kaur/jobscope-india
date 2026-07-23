import streamlit as st

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.warning("Please register/login to access the dashboard.")
    st.switch_page("pages/00_Authentication.py")

import pandas as pd
import numpy as np

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
# HOME METRICS
# =====================================

jobs = len(df)

companies = df["companyName"].nunique()

locations = df["location"].nunique()


# =====================================
# COMPENSATION METRICS
# =====================================

salary_df = df[
    (df["averageSalary"] > 0) &
    (df["averageSalary"] <= df["averageSalary"].quantile(0.99))
].copy()


# =====================================
# SKILLS METRICS
# =====================================

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
    .sort_values(
        "MedianSalary",
        ascending=False
    )
    .iloc[0]["tagsAndSkills"]
)


# =====================================
# EXPERIENCE METRICS
# =====================================

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
    experience_df["averageExperience"].max()
)

average_experience = (
    experience_df["averageExperience"].mean()
)


# =====================================
# COMPANY METRICS
# =====================================

company_counts = (
    df["companyName"]
    .value_counts()
)

review_df = (
    df.groupby("companyName")
    .agg(
        AvgReviews=("ReviewsCount","mean"),
        Jobs=("companyName","count")
    )
    .reset_index()
)

top_recruiter = (
    company_counts.idxmax()
)

most_reviewed = (
    review_df
    .sort_values(
        "AvgReviews",
        ascending=False
    )
    .iloc[0]["companyName"]
)


# =====================================
# GEOGRAPHIC METRICS
# =====================================

location_counts = (
    df["location"]
    .value_counts()
)

top_city = (
    location_counts.idxmax()
)

average_jobs = (
    location_counts.mean()
)

# =====================================
# HERO SECTION
# =====================================

st.markdown(
"""
<div class="hero-section">

<h1>
🏆 Executive Insights & Key Findings
</h1>

<p>

A consolidated overview of the most important
insights discovered throughout the JobScope India
analysis.

This page summarizes hiring trends, salary
patterns, employer demand, experience
requirements, skill intelligence, and geographic
distribution into a single executive dashboard.

</p>

</div>
""",
unsafe_allow_html=True
)

st.write("")


# =====================================
# EXECUTIVE OVERVIEW
# =====================================

st.markdown(
"""
<div class="content-card">

<h3>
📌 Executive Overview
</h3>

<p>

This section combines the most significant
findings from every analytical module into one
comprehensive executive summary.

Instead of exploring individual charts, the
dashboard presents the overall picture of India's
technology job market using the same metrics and
insights from the previous analysis pages.

</p>

</div>
""",
unsafe_allow_html=True
)

st.write("")
st.divider()

# =====================================
# EXECUTIVE DASHBOARD
# =====================================

st.markdown(
"""
<h2 class="section-heading">
📊 Executive Dashboard
</h2>
""",
unsafe_allow_html=True
)

row1_col1,row1_col2,row1_col3,row1_col4 = st.columns(
    4,
    gap="large"
)

with row1_col1:

    metric_card(
        "Total Jobs",
        f"{jobs:,}",
        "💼"
    )

with row1_col2:

    metric_card(
        "Companies",
        f"{companies:,}",
        "🏢"
    )

with row1_col3:

    metric_card(
        "Locations",
        f"{locations:,}",
        "🌍"
    )

with row1_col4:

    metric_card(
        "Unique Skills",
        f"{skills.nunique():,}",
        "🛠"
    )

st.write("")

row2_col1,row2_col2,row2_col3,row2_col4 = st.columns(
    4,
    gap="large"
)

with row2_col1:

    metric_card(
        "Average Salary",
        f"₹{salary_df['averageSalary'].mean()/100000:.2f}L",
        "💰"
    )

with row2_col2:

    metric_card(
        "Median Salary",
        f"₹{salary_df['averageSalary'].median()/100000:.2f}L",
        "📈"
    )

with row2_col3:

    metric_card(
        "Maximum Salary",
        f"₹{salary_df['maximumSalary'].max()/100000:.1f}L",
        "🚀"
    )

with row2_col4:

    metric_card(
        "Most Requested Skill",
        skill_counts.idxmax(),
        "🏆"
    )

st.write("")
st.divider()


# =====================================
# ANALYSIS INTRO
# =====================================

st.markdown(
"""
<div class="section-banner">

<h3>
🚀 Executive Summary
</h3>

<p>

The following section consolidates the insights
obtained from Compensation, Job Market, Skills,
Company, Experience, and Geographic analyses into
one complete executive report.

</p>

</div>
""",
unsafe_allow_html=True
)

st.write("")
st.divider()

# =====================================
# EXECUTIVE INSIGHTS
# =====================================

st.markdown(
"""
<h2 class="section-heading">
📈 Executive Insights
</h2>
""",
unsafe_allow_html=True
)

left, right = st.columns(
    [1.45, 1],
    gap="large"
)

# =====================================
# LEFT COLUMN
# =====================================

with left:

    st.markdown(
    """
    <div class="insight-box">

    <div class="insight-header">

    💰 Compensation Trends

    </div>

    <div class="insight-text">

    Salary growth demonstrates a strong positive
    relationship with professional experience.
    Senior-level professionals consistently command
    significantly higher compensation than
    entry-level candidates.

    </div>

    </div>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
    """
    <div class="insight-box">

    <div class="insight-header">

    🛠 Skills Intelligence

    </div>

    <div class="insight-text">

    Python, SQL, Java and cloud technologies
    continue to dominate employer demand, while
    specialized technical skills are associated
    with the highest salary offerings.

    </div>

    </div>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
    """
    <div class="insight-box">

    <div class="insight-header">

    🏢 Company Insights

    </div>

    <div class="insight-text">

    Large organizations contribute a substantial
    portion of total job postings, whereas highly
    reviewed employers generally represent mature
    and well-established companies.

    </div>

    </div>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
    """
    <div class="insight-box">

    <div class="insight-header">

    🌍 Geographic Distribution

    </div>

    <div class="insight-text">

    Hiring activity remains concentrated within
    India's major metropolitan technology hubs,
    with Bengaluru leading national recruitment,
    followed by Hyderabad, Pune, Chennai and
    Mumbai.

    </div>

    </div>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
    """
    <div class="insight-box">

    <div class="insight-header">

    🚀 Overall Market Outlook

    </div>

    <div class="insight-text">

    India's technology job market continues to
    exhibit strong demand for skilled professionals,
    creating excellent opportunities for candidates
    possessing modern technical expertise and
    practical project experience.

    </div>

    </div>
    """,
    unsafe_allow_html=True
    )

# =====================================
# RIGHT COLUMN
# =====================================

with right:

    st.markdown(
    f"""
    <div class="metric-card">

    <h3>

    🏆 Market Highlights

    </h3>

    <p><b>💼 Total Job Postings</b><br>{jobs:,}</p>

    <p><b>🏢 Companies Analysed</b><br>{companies:,}</p>

    <p><b>🌍 Locations Covered</b><br>{locations:,}</p>

    <p><b>🛠 Unique Skills</b><br>{skills.nunique():,}</p>

    <p><b>📍 Top Hiring City</b><br>{top_city}</p>

    <p><b>🏆 Most Requested Skill</b><br>{skill_counts.idxmax()}</p>

    </div>
    """,
    unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
    """
    <div class="metric-card">

    <h3>

    🎯 Career Takeaways

    </h3>


    ✅ Build strong programming fundamentals.

    ✅ Learn complementary technologies instead
    of isolated tools.

    ✅ Develop real-world projects alongside
    technical skills.

    ✅ Continuously upskill with emerging
    technologies.


    ✅ Focus on specialization to improve
    long-term career growth and salary potential.

    </div>
    """,
    unsafe_allow_html=True
    )

st.write("")
st.divider()

# =====================================
# FINAL CONCLUSION
# =====================================

st.markdown(
"""
<h2 class="section-heading">
🎯 Final Conclusion
</h2>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="content-card">

<h3>

Executive Summary

</h3>

<p>

The analysis of approximately <b>98,000</b> job postings
provides valuable insights into India's rapidly evolving
employment landscape.

Across all analytical dimensions, the market demonstrates
consistent demand for skilled professionals, particularly
those possessing strong programming expertise, practical
industry experience, and modern technology skills.

Salary growth closely follows professional experience,
while metropolitan technology hubs continue to dominate
national hiring activity. At the same time, employers
increasingly seek candidates with complementary technical
skill sets rather than isolated competencies.

Overall, the findings highlight a dynamic job market where
continuous learning, specialization, and practical project
experience remain the strongest drivers of career growth.

</p>

</div>
""",
unsafe_allow_html=True
)

st.write("")
st.divider()


# =====================================
# PROJECT HIGHLIGHTS
# =====================================

st.markdown(
"""
<h2 class="section-heading">
🏅 Project Highlights
</h2>
""",
unsafe_allow_html=True
)

st.write("")

col1,col2,col3,col4 = st.columns(4)

with col1:
    metric_card(
        "Interactive Pages",
        "8",
        "📄"
    )

with col2:
    metric_card(
        "Visualizations",
        "15",
        "📊"
    )

with col3:
    metric_card(
        "Records Analysed",
        "97,929",
        "📑"
    )

with col4:
    metric_card(
        "Technologies",
        "Python + Plotly + Streamlit",
        "🚀"
    )

st.write("")
st.divider()

# =====================================
# FOOTER
# =====================================

st.markdown(
"""
<div class="hero-section" style="padding:30px;text-align:center;">

<h2>

✨ Thank You for Exploring JobScope India ✨

</h2>

<p>

JobScope India transforms thousands of Indian job
postings into actionable insights through
interactive visualizations, statistical analysis,
and business intelligence.

Built using <b>Python, NumPy, Pandas, Matplotlib, Seaborn, Plotly, and
Streamlit</b>, this dashboard demonstrates how
data analytics can uncover meaningful patterns in
India's evolving employment market.

</p>

</div>
""",
unsafe_allow_html=True
)
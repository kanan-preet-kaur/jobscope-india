import streamlit as st

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.session_state.show_auth_message = True
    st.switch_page("pages/00_Authentication.py")

import pandas as pd
import numpy as np

import plotly.express as px


from utils.loader import load_data
from utils.theme import apply_page_config, inject_theme_css

from components.sidebar import render_sidebar
from components.metrics import metric_card

# =====================================
# PROJECT THEME
# =====================================


# Primary Color Palette

PRIMARY = "#6D28D9"      
SECONDARY = "#8B5CF6"    
ACCENT = "#A78BFA"       

PINK = "#EC4899"
MAGENTA = "#D946EF"
INDIGO = "#4F46E5"
CYAN = "#06B6D4"



# Semantic Colors

SUCCESS = "#22C55E"
WARNING = "#F59E0B"
DANGER = "#EF4444"



# Text & Layout

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

        # FORCE PLOTLY BACKGROUND
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
# SALARY DATASET
# SAME FILTERING AS EDA
# =====================================

salary_df = df[
    (df["averageSalary"] > 0) &
    (df["averageSalary"] <= df["averageSalary"].quantile(0.99))
].copy()



# =====================================
# HERO SECTION
# =====================================

st.markdown(
"""
<div class="hero-section">

<h1>
💰 Compensation Analysis
</h1>

<p>
Understanding salary patterns, compensation
distribution, and earning potential across
India's employment landscape.
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

This section explores how compensation varies
across the Indian job market.

The analysis focuses on salary distribution,
salary variability, and the relationship between
professional experience and earning potential.

</p>


</div>
""",
unsafe_allow_html=True
)



st.write("")
st.divider()


# =====================================
# COMPENSATION SNAPSHOT
# =====================================


st.markdown(
"""
<h2 class="section-heading">
📊 Compensation Snapshot
</h2>
""",
unsafe_allow_html=True
)

st.write("")

col1, col2, col3, col4 = st.columns(
    4,
    gap="large"
)



with col1:

    metric_card(
        "Average Salary",
        f"₹{salary_df['averageSalary'].mean()/100000:.2f}L",
        "💰"
    )



with col2:

    metric_card(
        "Median Salary",
        f"₹{salary_df['averageSalary'].median()/100000:.2f}L",
        "📈"
    )



with col3:

    metric_card(
        "Maximum Salary",
        f"₹{salary_df['maximumSalary'].max()/100000:.1f}L",
        "🚀"
    )



with col4:

    metric_card(
        "Job Records",
        f"{len(salary_df):,}",
        "📑"
    )


st.write("")
st.divider()


# =====================================
# SALARY EXPLORER
# =====================================


st.markdown(
"""
<h2 class="section-heading">
🎛️ Salary Explorer
</h2>
""",
unsafe_allow_html=True
)



filter_container = st.container()



with filter_container:


    filter_col1, filter_col2 = st.columns(
        2,
        gap="large"
    )


    with filter_col1:

        experience_range = st.slider(

            "Experience Range (Years)",

            min_value=int(
                df["averageExperience"].min()
            ),

            max_value=int(
                df["averageExperience"].max()
            ),

            value=(

                int(
                    df["averageExperience"].min()
                ),

                int(
                    df["averageExperience"].max()
                )

            )

        )



    with filter_col2:


        salary_range = st.slider(

            "Average Salary Range (Lakhs)",

            min_value=0,

            max_value=int(
                salary_df["averageSalary"].max()/100000
            ),

            value=(

                0,

                int(
                    salary_df["averageSalary"].max()/100000
                )

            )

        )



filtered_salary_df = salary_df[

    (salary_df["averageExperience"] >= experience_range[0])

    &

    (salary_df["averageExperience"] <= experience_range[1])

    &

    (salary_df["averageSalary"] >= salary_range[0] * 100000)

    &

    (salary_df["averageSalary"] <= salary_range[1] * 100000)

].copy()



st.divider()



# =====================================
# CHART 1
# DISTRIBUTION OF AVERAGE SALARIES
# FROM EDA NOTEBOOK
# =====================================


st.markdown(
"""
<h2 class="section-heading">
📈 Distribution of Average Salaries
</h2>
""",
unsafe_allow_html=True
)



fig = px.histogram(

    filtered_salary_df,

    x="averageSalary",

    nbins=35,

    title="Distribution of Average Salaries",

    opacity=0.88,

    color_discrete_sequence=[PRIMARY]

)



# Salary axis in Lakhs
max_salary = filtered_salary_df["averageSalary"].max()


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

    title="Average Salary (INR)",

    tickmode="array",

    tickvals=tick_vals,

    ticktext=tick_text

)



fig.update_yaxes(

    title="Number of Job Postings"

)



fig.update_traces(

    marker=dict(

        line=dict(

            color="rgba(255,255,255,0.35)",

            width=0.7

        )

    ),


    hovertemplate=(

        "<b>Average Salary</b><br>"

        "₹%{x:,.0f}<br><br>"

        "<b>Job Postings</b><br>"

        "%{y:,}"

        "<extra></extra>"

    )

)



fig = style_plot(fig)



st.plotly_chart(

    fig,

    use_container_width=True

)


# =====================================
# INSIGHT CARD
# =====================================

st.markdown(
"""
<div class="insight-box">


<div class="insight-header">

💡 Salary Distribution Insight

</div>


<div class="insight-text">

The salary distribution is 
<span class="highlight">
positively skewed
</span>,
indicating that most job opportunities are
concentrated within the lower-to-middle
compensation range.




A smaller segment of premium-paying roles
creates a long salary tail, highlighting the
impact of specialised skills and premium
positions on earning potential.

</div>


</div>
""",
unsafe_allow_html=True
)

# =====================================
# CHART 2
# SALARY OUTLIER ANALYSIS
# FROM EDA NOTEBOOK
# =====================================


st.markdown(
"""
<h2 class="section-heading">
📦 Salary Distribution with Outliers
</h2>
""",
unsafe_allow_html=True
)



fig = px.box(

    filtered_salary_df,

    x="averageSalary",

    title="Average Salary Distribution with Outliers",

    color_discrete_sequence=[SECONDARY],

    points="outliers"

)



# Salary axis in Lakhs

max_salary = filtered_salary_df["averageSalary"].max()


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

    title="Average Salary (INR)",

    tickmode="array",

    tickvals=tick_vals,

    ticktext=tick_text

)



fig.update_yaxes(

    title=""

)



fig.update_traces(


    width=0.45,


    marker=dict(

        size=5,

        opacity=0.75,

        line=dict(

            color="white",

            width=0.5

        )

    ),


    line=dict(

        width=2

    ),


    hovertemplate=(

        "<b>Average Salary</b><br>"

        "₹%{x:,.0f}"

        "<extra></extra>"

    )

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

📦 Salary Variability Insight

</div>



<div class="insight-text">

Most salaries remain concentrated within a
stable compensation range, while a smaller
number of roles create significant outliers.


These high-value positions demonstrate how
<span class="highlight">
specialised skills, seniority, and role complexity
</span>
influence compensation levels.

</div>


</div>
""",
unsafe_allow_html=True
)

# =====================================
# CHART 3
# AVERAGE SALARY BY EXPERIENCE LEVEL
# FROM EDA NOTEBOOK
# =====================================


st.markdown(
"""
<h2 class="section-heading">
📈 Average Salary by Experience Level
</h2>
""",
unsafe_allow_html=True
)



experience_salary = (

    filtered_salary_df
    .groupby("averageExperience")["averageSalary"]
    .mean()
    .reset_index()
    .sort_values("averageExperience")

)



fig = px.line(

    experience_salary,

    x="averageExperience",

    y="averageSalary",

    title="Average Salary by Experience Level",

    markers=True,

    color_discrete_sequence=[CYAN]

)



# Salary axis in Lakhs

max_salary = experience_salary["averageSalary"].max()


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

    title="Average Experience (Years)"

)



fig.update_yaxes(

    title="Average Salary (INR)",

    tickmode="array",

    tickvals=tick_vals,

    ticktext=tick_text

)



fig.update_traces(

    line=dict(

        width=3

    ),


    marker=dict(

        size=8,

        line=dict(

            color="white",

            width=1

        )

    ),


    hovertemplate=(

        "<b>Experience</b><br>"

        "%{x:.1f} Years"

        "<br><br>"

        "<b>Average Salary</b><br>"

        "₹%{y:,.0f}"

        "<extra></extra>"

    )

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

📈 Experience vs Compensation Trend

</div>



<div class="insight-text">

Salary shows a clear upward trend as
professional experience increases.


Experience acts as one of the strongest market
signals, with experienced professionals gaining
access to
<span class="highlight">
higher earning potential
</span>
through advanced responsibilities and expertise.

</div>


</div>
""",
unsafe_allow_html=True
)

# =====================================
# COMPENSATION ANALYSIS SUMMARY
# =====================================

st.divider()

st.markdown(
"""
<h2 class="section-heading">
📌 Compensation Analysis Summary
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
    💰 Salary Distribution
    </div>

    <div class="insight-text">

    • Most job opportunities are concentrated
    within the lower-to-middle salary range.

    • The compensation distribution is positively
    skewed due to a smaller number of premium roles.

    • Average salary is influenced by high-paying
    positions, making median salary a better
    indicator of typical earnings.

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
    📈 Experience & Salary Growth
    </div>

    <div class="insight-text">

    • Compensation shows a positive relationship
    with professional experience.

    • Experienced professionals gain access to
    higher-value opportunities.

    • Seniority and expertise remain important
    factors influencing earning potential.

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
    🚀 Premium Compensation
    </div>

    <div class="insight-text">

    • High-paying roles represent a smaller segment
    of the overall job market.

    • Specialized skills and advanced expertise
    create significant salary advantages.

    • Premium opportunities are associated with
    greater responsibility and role complexity.

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

    Compensation growth depends on a combination
    of experience, specialization, and market demand.

    Professionals can maximize earning potential
    by developing advanced skills aligned with
    high-value opportunities.

    </div>

    </div>
    """,
    unsafe_allow_html=True
    )
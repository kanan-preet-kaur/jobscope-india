import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from utils.loader import load_job_data
from utils.styling import apply_custom_css, get_theme_colors

# 1. Page Configuration
st.set_page_config(page_title="Company Analysis", layout="wide")
apply_custom_css()
colors = get_theme_colors()

# 2. Data Loading
df, _ = load_job_data()

# 3. Page Title
st.markdown('<p class="main-title">Company Analysis</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Evaluating hiring scale and employer footprint in the Indian market.</p>', unsafe_allow_html=True)

# 4. Data Processing for Charts
company_jobs = df.groupby("companyName").agg(
    JobPostings=("companyName", "count"),
    Reviews=("ReviewsCount", "mean")
).reset_index()

company_jobs["Company Size"] = np.where(
    company_jobs["Reviews"] >= company_jobs["Reviews"].median(),
    "Large Companies", "Smaller Companies"
)
market_share = company_jobs.groupby("Company Size")["JobPostings"].sum().reset_index()

# 5. Row 1: Market Share by Company Size (Pie/Donut)
st.subheader("Market Share of Job Postings")
fig1 = px.pie(
    market_share, names="Company Size", values="JobPostings", hole=0.55,
    color_discrete_map={"Large Companies": colors['primary'], "Smaller Companies": colors['success']}
)
fig1.update_traces(textinfo="percent+label")
st.plotly_chart(fig1, use_container_width=True)

st.markdown('''
    <div class="info-panel">
        <div class="panel-title">Insight</div>
        <div class="panel-desc">
            Larger organizations maintain a dominant share of job postings. However, 
            smaller companies collectively contribute a significant portion of roles, 
            often offering more specialized niches for career growth.
        </div>
    </div>
''', unsafe_allow_html=True)

st.write("---")

# 6. Row 2: Most Heavily Reviewed Companies (Treemap)
st.subheader("Most Heavily Reviewed Companies")
company_reviews = df.groupby("companyName", as_index=False).agg(
    ReviewsCount=("ReviewsCount", "mean")
).sort_values("ReviewsCount", ascending=False).head(15)

fig2 = px.treemap(
    company_reviews, path=["companyName"], values="ReviewsCount",
    color="ReviewsCount", color_continuous_scale="Blues"
)
st.plotly_chart(fig2, use_container_width=True)

st.markdown('''
    <div class="info-panel">
        <div class="panel-title">Insight</div>
        <div class="panel-desc">
            Review volume correlates strongly with company size and hiring frequency. 
            Large enterprises like TCS, Accenture, and Infosys possess the highest 
            employer visibility, acting as benchmarks for the broader job market.
        </div>
    </div>
''', unsafe_allow_html=True)
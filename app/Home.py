import streamlit as st
import pandas as pd
import numpy as np
import os
from utils.loader import load_job_data
from utils.styling import apply_custom_css, get_theme_colors

# 1. Page Configuration
st.set_page_config(
    page_title="JobScope India | Home",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inject Premium CSS Styles
apply_custom_css()
colors = get_theme_colors()

# 3. Load Cleaned Dataset
df, is_mock = load_job_data()

st.markdown('<h1 class="main-title">JobScope India</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Indian Job Market Intelligence Dashboard • Professional Insights Terminal</p>', unsafe_allow_html=True)

if is_mock is not None and not is_mock.empty:
    st.info("💡 **Development Sandbox Active**: The cleaned dataset file `cleaned_job_market.csv` was not found. Using simulated data for testing.")

# 4. Global KPIs
market_salaries = df[df["averageSalary"] > 0]["averageSalary"]

avg_salary = market_salaries.mean() / 100000  # Convert to Lakhs
total_listings = len(df)
avg_exp = df["averageExperience"].mean()
total_companies = df["companyName"].nunique()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""
        <div class="metric-card hero">
            <div class="metric-title">Positions Tracked</div>
            <div class="metric-value">{total_listings:,}</div>
            <div class="metric-desc">Total Active Job Openings</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-card standard">
            <div class="metric-title">Average Package</div>
            <div class="metric-value">₹{avg_salary:.2f} LPA</div>
            <div class="metric-desc">Baseline Market Compensation</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-card standard">
            <div class="metric-title">Required Experience</div>
            <div class="metric-value">{avg_exp:.1f} Yrs</div>
            <div class="metric-desc">Average Professional Tenure</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="metric-card standard">
            <div class="metric-title">Hiring Firms</div>
            <div class="metric-value">{total_companies}</div>
            <div class="metric-desc">Distinct Corporate Entities</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

col_left, col_right = st.columns([7, 4])

with col_left:
    st.subheader("🎯 Project Purpose & Scope")
    st.markdown(
        """
        **JobScope India** is an interactive, end-to-end analytical dashboard built to demystify India's modern 
        job landscape, wage distributions, and core technical expectations. By running live aggregates over tech-hiring datasets, 
        this dashboard lets you discover salary benchmarks, explore regional high-opportunity locations, and analyze which skills 
        hold the most competitive leverage.
        """
    )
    
    st.subheader("📚 Dataset Provenance")
    st.markdown("""
        <div class="info-panel">
            <div class="panel-title">Source Information & Scale</div>
            <div class="panel-desc">
                This dashboard is powered by the <b>Indian Job Market Dataset (2025-2026)</b>, 
                a high-resolution dataset sourced from <b>Kaggle</b> featuring <b>97,000+ 
                granular data points</b>. It captures the complex post-2025 Indian 
                hiring landscape, offering comprehensive insights into:
                <br><br>
                <ul>
                    <li><b>Market Benchmarks:</b> Detailed salary distributions (LPA) and compensation brackets.</li>
                    <li><b>Talent Requirements:</b> Required experience tiers, educational qualifications, and technical skill tags.</li>
                    <li><b>Industry Dynamics:</b> Company ratings, size, location trends, and remote/hybrid work flexibility.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="info-panel">
            <div class="panel-title">Data Integrity & Processing</div>
            <div class="panel-desc">
                To ensure high-fidelity analytical outputs, the raw data from Kaggle has 
                undergone rigorous preprocessing. This includes deduplication, handling 
                of missing salary/experience values via median imputation, and 
                normalization of job titles and location clusters. The resulting 
                <i>Cleaned Snapshot</i> serves as a reliable baseline for salary 
                predictions, trend analysis, and skill-demand forecasting.
            </div>
        </div>
    """, unsafe_allow_html=True)
    
with col_right:
    st.subheader("⚡ Core Navigation Modules")
    modules = [
        ("💻 Compensation Analysis", "Visualize packages, distributions, and earning percentiles."),
        ("📈 Job Market Dynamics", "Examine overall market indicators, trends, and correlations."),
        ("🛠️ Skills Analysis", "Track in-demand technical toolsets and tag associations."),
        ("🏢 Company Insights", "Compare top hiring organizations and ratings metrics."),
        ("🎓 Experience Profiling", "Evaluate tenure thresholds and hiring expectation curves.")
    ]
    for title, desc in modules:
        st.markdown(f"""
            <div class="info-panel">
                <div class="panel-title">{title}</div>
                <div class="panel-desc">{desc}</div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("---") 
st.subheader("📊 Dataset Overview")
st.dataframe(df.head(15), use_container_width=True)
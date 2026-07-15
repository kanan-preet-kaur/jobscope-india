import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
from utils.loader import load_job_data
from utils.styling import apply_custom_css, get_theme_colors

# 1. Page Config & Professional Theme Colors
st.set_page_config(
    page_title="Compensation Analysis",
    page_icon="💰",
    layout="wide"
)

# YOUR exact project theme constants
PRIMARY_BLUE  = "#1E3A8A"
SUCCESS_GREEN = "#10B981"
ACCENT_AMBER  = "#F59E0B"
MUTED_SLATE   = "#64748B"
TEXT_DARK     = "#1E293B"
GRID          = "#E2E8F0"

# YOUR exact rcParams configuration
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"
plt.rcParams["axes.edgecolor"] = "#CBD5E1"
plt.rcParams["axes.linewidth"] = 1.2
plt.rcParams["text.color"] = TEXT_DARK
plt.rcParams["axes.labelcolor"] = TEXT_DARK
plt.rcParams["xtick.color"] = TEXT_DARK
plt.rcParams["ytick.color"] = TEXT_DARK
plt.rcParams["font.size"] = 11
plt.rcParams["axes.labelsize"] = 12
plt.rcParams["axes.titlesize"] = 18
plt.rcParams["axes.titleweight"] = "bold"
plt.rcParams["axes.grid"] = True
plt.rcParams["grid.color"] = GRID
plt.rcParams["grid.linestyle"] = "--"
plt.rcParams["grid.alpha"] = 0.6

sns.set_style("whitegrid")

# YOUR exact custom plot styling helper function
def style_plot(ax, title, xlabel, ylabel):
    ax.set_title(
        title,
        fontsize=18,
        fontweight="bold",
        pad=18
    )
    ax.set_xlabel(
        xlabel,
        fontsize=12,
        labelpad=14
    )
    ax.set_ylabel(
        ylabel,
        fontsize=12,
        labelpad=14
    )
    ax.tick_params(
        axis="both",
        labelsize=11
    )
    ax.grid(
        axis="y",
        linestyle="--",
        linewidth=0.7,
        alpha=0.6,
        color=GRID
    )
    sns.despine(left=False, bottom=False)

# Custom container styling for breathing space & card aesthetics
st.markdown("""
    <style>
    .reportview-container {
        background-color: #F8FAFC;
    }
    .metric-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        border: 1px solid #E2E8F0;
        text-align: center;
        margin-bottom: 2rem;
    }
    .insight-card {
        background-color: #F8FAFC;
        padding: 1.5rem;
        border-left: 4px solid #1E3A8A;
        border-radius: 4px 12px 12px 4px;
        margin-top: 1.5rem;
        margin-bottom: 3rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    .space-divider {
        margin-top: 4rem;
        margin-bottom: 4rem;
        border-bottom: 1px solid #E2E8F0;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Data Loading & Subsetting (using your exact processed path and logic)
@st.cache_data
def load_data():
    # Loading the processed data you cleaned
    df, is_mock = load_job_data()
    
    # YOUR exact salary subsetting logic
    salary_df = df[
        (df["averageSalary"] > 0) &
        (df["averageSalary"] <= df["averageSalary"].quantile(0.99))
    ].copy()
    
    return salary_df

salary_df = load_data()

# Header block with clean breathing space
st.markdown('<div style="margin-top: 2rem;"></div>', unsafe_allow_html=True)
st.title("💰 Salary & Compensation Analysis")
st.markdown(
    """
    <p style="font-size: 1.15rem; color: #64748B; margin-bottom: 3rem;">
    An in-depth evaluation of salary trends, range distributions, outlier metrics, and minimum vs. maximum salary bands.
    </p>
    """, 
    unsafe_allow_html=True
)

# 3. KPI / Metrics Cards
kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

with kpi_col1:
    st.markdown(f"""
        <div class="metric-card">
            <span style="color: #64748B; font-size: 0.9rem; font-weight: 600; text-transform: uppercase;">Median Salary</span>
            <h2 style="color: #1E3A8A; font-size: 2.2rem; margin: 0.5rem 0;">₹{salary_df["averageSalary"].median()/100000:.2f}L</h2>
            <span style="color: #10B981; font-size: 0.85rem;">Most representative market midpoint</span>
        </div>
    """, unsafe_allow_html=True)

with kpi_col2:
    st.markdown(f"""
        <div class="metric-card">
            <span style="color: #64748B; font-size: 0.9rem; font-weight: 600; text-transform: uppercase;">Maximum Salary Limit</span>
            <h2 style="color: #10B981; font-size: 2.2rem; margin: 0.5rem 0;">₹{salary_df["averageSalary"].max()/100000:.2f}L</h2>
            <span style="color: #64748B; font-size: 0.85rem;">99th percentile capping applied</span>
        </div>
    """, unsafe_allow_html=True)

with kpi_col3:
    st.markdown(f"""
        <div class="metric-card">
            <span style="color: #64748B; font-size: 0.9rem; font-weight: 600; text-transform: uppercase;">Total Active Postings</span>
            <h2 style="color: #F59E0B; font-size: 2.2rem; margin: 0.5rem 0;">{len(salary_df):,}</h2>
            <span style="color: #64748B; font-size: 0.85rem;">With valid disclosed salary data</span>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="space-divider"></div>', unsafe_allow_html=True)


# ==========================================
# CHART 1: SALARY DISTRIBUTION (EXACTLY YOURS)
# ==========================================
st.subheader("📊 Salary Distribution Profile")

fig1, ax1 = plt.subplots(figsize=(13, 6), dpi=150)
sns.histplot(
    data=salary_df,
    x="averageSalary",
    bins=35,
    color=PRIMARY_BLUE,
    edgecolor="white",
    linewidth=0.5,
    alpha=0.95,
    ax=ax1
)
ax1.xaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"₹{x/100000:.0f}L")
)
style_plot(
    ax1,
    "Distribution of Average Salaries",
    "Average Salary (INR)",
    "Number of Job Postings"
)
plt.tight_layout()

# Draw directly to dashboard!
st.pyplot(fig1)
plt.close(fig1)

st.markdown("""
    <div class="insight-card">
        <h4 style="color: #1E293B; margin-top:0;">💡 Chart 1 Insights</h4>
        <ul style="color: #475569; font-size: 0.95rem; line-height: 1.6; margin-bottom:0;">
            <li>The salary distribution is <strong>positively skewed</strong>, indicating that most job opportunities offer salaries within the lower-to-middle compensation range.</li>
            <li>A majority of job postings provide average annual salaries between <strong>₹2 lakh and ₹5 lakh</strong>.</li>
            <li>Only a relatively small proportion of positions offer substantially higher salaries, creating a long right tail.</li>
            <li>The distribution suggests that high-paying opportunities exist but represent a niche segment of the overall market.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="space-divider"></div>', unsafe_allow_html=True)


# ==========================================
# CHART 2: SALARY OUTLIER ANALYSIS (EXACTLY YOURS)
# ==========================================
st.subheader("📦 Outlier Spread & Dispersion")

fig2, ax2 = plt.subplots(figsize=(13, 3), dpi=150)
sns.boxplot(
    x=salary_df["averageSalary"],
    color=PRIMARY_BLUE,
    width=0.45,
    linewidth=1,
    fliersize=3,
    ax=ax2
)
ax2.xaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"₹{x/100000:.0f}L")
)
style_plot(
    ax2,
    "Average Salary Distribution with Outliers",
    "Average Salary (INR)",
    ""
)
plt.tight_layout()

# Draw directly to dashboard!
st.pyplot(fig2)
plt.close(fig2)

st.markdown("""
    <div class="insight-card">
        <h4 style="color: #1E293B; margin-top:0;">💡 Chart 2 Insights</h4>
        <ul style="color: #475569; font-size: 0.95rem; line-height: 1.6; margin-bottom:0;">
            <li>Most salaries are concentrated within a narrow range, while a limited number of jobs offer exceptionally high compensation.</li>
            <li>Several <strong>high-value outliers</strong> are visible, confirming the presence of premium-paying positions.</li>
            <li>The positive skew indicates that <strong>median salary</strong> is a more representative measure than the arithmetic mean.</li>
            <li>Salary variability increases considerably at higher compensation levels.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="space-divider"></div>', unsafe_allow_html=True)


# ==========================================
# CHART 7: MIN VS MAX SALARIES (EXACTLY YOURS)
# ==========================================
st.subheader("⚖️ Salary Range Disparity: Minimum vs Maximum")

fig7, ax7 = plt.subplots(figsize=(13, 6), dpi=150)
sns.histplot(
    salary_df["minimumSalary"],
    bins=35,
    color=PRIMARY_BLUE,
    alpha=0.55,
    label="Minimum Salary",
    edgecolor="white",
    ax=ax7
)
sns.histplot(
    salary_df["maximumSalary"],
    bins=25,
    color=SUCCESS_GREEN,
    alpha=0.45,
    label="Maximum Salary",
    edgecolor="white",
    ax=ax7
)
ax7.legend(facecolor="white", edgecolor=GRID, framealpha=1)
ax7.xaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"₹{int(x/100000)}L")
)
style_plot(
    ax7,
    "Distribution of Minimum and Maximum Salaries",
    "Salary (INR)",
    "Number of Job Postings"
)
plt.tight_layout()

# Draw directly to dashboard!
st.pyplot(fig7)
plt.close(fig7)

st.markdown("""
    <div class="insight-card" style="border-left-color: #10B981;">
        <h4 style="color: #1E293B; margin-top:0;">💡 Chart 3 Insights</h4>
        <ul style="color: #475569; font-size: 0.95rem; line-height: 1.6; margin-bottom:0;">
            <li>Maximum salaries exhibit considerably greater variation than minimum salaries.</li>
            <li>Many employers advertise broad salary ranges, reflecting flexibility based on candidate experience and skills.</li>
            <li>Minimum salaries remain relatively concentrated, while upper salary limits vary significantly.</li>
            <li>Wider salary ranges suggest <strong>stronger negotiation opportunities</strong> for qualified candidates.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div style="margin-bottom: 4rem;"></div>', unsafe_allow_html=True)
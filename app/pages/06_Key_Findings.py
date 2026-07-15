import streamlit as st
from utils.loader import load_job_data
from utils.styling import apply_custom_css

# Page Configuration
st.set_page_config(page_title="Executive Intelligence", layout="wide")
apply_custom_css()

# Load Data
df, _ = load_job_data()

st.markdown('<p class="main-title">Executive Intelligence Terminal</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Summary of Indian job market dynamics and strategic hiring trends.</p>', unsafe_allow_html=True)

# 1. KPI Stats Row
c1, c2, c3, c4 = st.columns(4)
c1.markdown(f'<div class="metric-card"><div class="metric-title">Market Reach</div><div class="metric-value">{df["location"].nunique()}</div><div class="metric-desc">Unique cities tracked</div></div>', unsafe_allow_html=True)
c2.markdown(f'<div class="metric-card"><div class="metric-title">Primary Hub</div><div class="metric-value">{df["location"].mode()[0]}</div><div class="metric-desc">Most active region</div></div>', unsafe_allow_html=True)
c3.markdown(f'<div class="metric-card"><div class="metric-title">Experience Avg</div><div class="metric-value">{df["averageExperience"].mean():.1f}y</div><div class="metric-desc">Baseline tenure</div></div>', unsafe_allow_html=True)
c4.markdown(f'<div class="metric-card"><div class="metric-title">Total Entities</div><div class="metric-value">{df["companyName"].nunique():,}</div><div class="metric-desc">Active firms</div></div>', unsafe_allow_html=True)

st.write("---")

# 2. Detailed Intelligence Panels
st.subheader("Actionable Strategic Findings")

col1, col2 = st.columns(2)

findings = [
    ("📈 Salary Acceleration", "Compensation data reveals a non-linear growth trajectory. Market value peaks significantly after the 5-year experience mark, suggesting a 'seniority premium' for specialized technical roles."),
    ("📍 Regional Clustering", "Hiring remains heavily anchored in Tier-1 metros. Data confirms that top-tier technical stacks are geographically bound to major hubs, limiting remote options for niche expert roles."),
    ("💻 The Core Stack", "Technical longevity is tied to 'The Core Stack' (Python, SQL, Java). Roles requiring these skills demonstrate higher job stability and lower turnover rates compared to emerging, volatile tech stacks."),
    ("⚖️ Scale & Stability", "Large enterprises prioritize volume-hiring of mid-level generalists, whereas smaller entities drive the demand for highly specialized 'Full-Stack' profiles to maximize operational agility.")
]

for i, (title, desc) in enumerate(findings):
    target = col1 if i % 2 == 0 else col2
    target.markdown(f"""
        <div class="info-panel">
            <div class="panel-title">{title}</div>
            <div class="panel-desc">{desc}</div>
        </div>
    """, unsafe_allow_html=True)

# 3. Final Summary Note
st.markdown("""
    <div class="info-panel" style="border-left: 4px solid #F59E0B;">
        <div class="panel-title">Final Verdict</div>
        <div class="panel-desc">
            The Indian job market is currently favoring <b>mid-career professionals (3-8 years)</b> who possess a 
            hybrid of core technical expertise and industry-specific domain knowledge. Employers are 
            increasingly screening for 'stack-compatibility' rather than isolated skill lists.
        </div>
    </div>
""", unsafe_allow_html=True)
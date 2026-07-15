import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.loader import load_job_data
from utils.styling import apply_custom_css, get_theme_colors

# 1. Page Configuration
st.set_page_config(page_title="Job Market Analysis", layout="wide")
apply_custom_css()
colors = get_theme_colors()

# 2. Data Loading
df, _ = load_job_data()

# 3. Page Title
st.markdown('<p class="main-title">Job Market Analysis</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Deep dive into hiring trends, locations, and demand patterns.</p>', unsafe_allow_html=True)

# 4. Row 1: Hiring Share by Top Locations
st.subheader("Hiring Share by Top Locations")
location_share = df["location"].value_counts().head(8)
fig1, ax1 = plt.subplots(figsize=(7, 5))
ax1.pie(location_share.values, labels=location_share.index, autopct="%1.1f%%", startangle=90,
        colors=sns.color_palette("Blues", len(location_share)), wedgeprops=dict(width=0.4, edgecolor="white"))
st.pyplot(fig1)
st.markdown('<div class="info-panel"><div class="panel-title">Insight</div><div class="panel-desc">Bengaluru leads as India\'s primary tech hub, followed by Hyderabad and Pune. Hiring is heavily clustered in metropolitan areas with mature IT ecosystems.</div></div>', unsafe_allow_html=True)

st.write("---")

# 5. Row 2: Most In-Demand Job Titles
st.subheader("Top 10 Most In-Demand Job Titles")
top_jobs = df["title"].dropna().str.strip().value_counts().head(10).sort_values(ascending=True)
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.barh(top_jobs.index, top_jobs.values, color=colors['accent'])
ax2.set_xlabel("Number of Job Postings")
st.pyplot(fig2)
st.markdown('<div class="info-panel"><div class="panel-title">Insight</div><div class="panel-desc">Software engineering and developer roles dominate the hiring market. There is a sustained, concentrated demand for core technical software roles.</div></div>', unsafe_allow_html=True)

st.write("---")

# 6. Row 3: Job Postings by Experience Level
st.subheader("Job Opportunities by Experience")
experience_df = df.copy()
experience_df["ExperienceGroup"] = pd.cut(
    experience_df["averageExperience"], bins=[0, 2, 5, 8, 12, 50],
    labels=["0–2 Years", "3–5 Years", "6–8 Years", "9–12 Years", "12+ Years"]
)
job_counts = experience_df["ExperienceGroup"].value_counts(sort=False).reset_index()
job_counts.columns = ["Experience Level", "Job Postings"]

fig3, ax3 = plt.subplots(figsize=(10, 4))
sns.barplot(data=job_counts, x="Experience Level", y="Job Postings", color=colors['primary'], ax=ax3)
st.pyplot(fig3)
st.markdown('<div class="info-panel"><div class="panel-title">Insight</div><div class="panel-desc">Mid-level experience requirements (3–8 years) account for the largest proportion of job postings, favoring professionals with practical industry experience.</div></div>', unsafe_allow_html=True)
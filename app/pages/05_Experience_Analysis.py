import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from utils.loader import load_job_data
from utils.styling import apply_custom_css

# Page Setup
st.set_page_config(page_title="Experience Analysis", layout="wide")
apply_custom_css()
df, _ = load_job_data()

st.markdown('<p class="main-title">Experience & Salary Correlation</p>', unsafe_allow_html=True)

# Sidebar Filter
exp_filter = st.sidebar.slider("Select Experience Range (Years)", 
                               int(df["averageExperience"].min()), 
                               int(df["averageExperience"].max()), 
                               (0, 10))
filtered_df = df[(df["averageExperience"] >= exp_filter[0]) & (df["averageExperience"] <= exp_filter[1])]

# KPI Row
c1, c2, c3 = st.columns(3)
c1.markdown(f'<div class="metric-card"><div class="metric-title">Avg Experience</div><div class="metric-value">{df["averageExperience"].mean():.1f} Yrs</div></div>', unsafe_allow_html=True)
c2.markdown(f'<div class="metric-card"><div class="metric-title">Entry-Level Jobs</div><div class="metric-value">{len(df[df["averageExperience"] <= 2]):,}</div></div>', unsafe_allow_html=True)
c3.markdown(f'<div class="metric-card"><div class="metric-title">Total Postings</div><div class="metric-value">{len(filtered_df):,}</div></div>', unsafe_allow_html=True)

# 1. Chart 3: Average Salary by Experience Level
st.subheader("Average Salary by Experience Level")
experience_salary = filtered_df.groupby("averageExperience")["averageSalary"].mean().reset_index().sort_values("averageExperience")
fig1, ax1 = plt.subplots(figsize=(12, 6))
sns.lineplot(data=experience_salary, x="averageExperience", y="averageSalary", marker="o", linewidth=2.8, color="#10B981", ax=ax1)
st.pyplot(fig1)
st.markdown('<div class="info-panel"><div class="panel-title">Insight</div><div class="panel-desc">Salary increases consistently with experience. The largest growth occurs after moving beyond entry-level positions.</div></div>', unsafe_allow_html=True)

st.write("---")

# 2. Chart 10: Job Postings by Experience Level
st.subheader("Job Postings by Experience Level")
experience_df = filtered_df.copy()
experience_df["ExperienceGroup"] = pd.cut(experience_df["averageExperience"], bins=[0, 2, 5, 8, 12, 50], labels=["0–2 Years", "3–5 Years", "6–8 Years", "9–12 Years", "12+ Years"])
job_counts = experience_df["ExperienceGroup"].value_counts(sort=False).reset_index()
fig2 = px.bar(job_counts, x="ExperienceGroup", y="count", color="count", text="count")
st.plotly_chart(fig2, use_container_width=True)
st.markdown('<div class="info-panel"><div class="panel-title">Insight</div><div class="panel-desc">Mid-level experience requirements account for the largest proportion of job postings.</div></div>', unsafe_allow_html=True)

st.write("---")

# 3. Chart 15: Experience vs. Salary Ceiling
st.subheader("Salary Distribution Across Experience Levels")
experience_salary_plot = filtered_df[filtered_df["maximumSalary"] > 0].copy()
experience_salary_plot["maximumSalaryLakhs"] = experience_salary_plot["maximumSalary"] / 100000
experience_salary_plot["Experience Bracket"] = pd.cut(experience_salary_plot["averageExperience"], bins=[0, 2, 5, 8, 12, 50], labels=["0–2 Years", "3–5 Years", "6–8 Years", "9–12 Years", "12+ Years"])
fig3, ax3 = plt.subplots(figsize=(12, 7))
sns.boxplot(data=experience_salary_plot, x="Experience Bracket", y="maximumSalaryLakhs", color="#1E3A8A", showfliers=False, ax=ax3)
st.pyplot(fig3)
st.markdown('<div class="info-panel"><div class="panel-title">Insight</div><div class="panel-desc">Salary ceilings increase as experience grows, though gains plateau at higher seniority levels.</div></div>', unsafe_allow_html=True)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.loader import load_job_data
from utils.styling import apply_custom_css, get_theme_colors

# 1. Page Configuration
st.set_page_config(page_title="Skills Analysis", layout="wide")
apply_custom_css()
colors = get_theme_colors()

# 2. Data Loading
df, _ = load_job_data()

# 3. Page Title
st.markdown('<p class="main-title">Skills Analysis</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Understanding the technical requirements and skill clusters of the Indian job market.</p>', unsafe_allow_html=True)

# 4. Row 1: Most Frequently Demanded Skills
st.subheader("Most Frequently Demanded Skills")
skills = df["tagsAndSkills"].dropna().str.split(",").explode().str.strip()
top_skills = skills.value_counts().head(12).sort_values(ascending=True)

fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.barh(top_skills.index, top_skills.values, color=colors['accent'])
ax1.set_xlabel("Number of Job Postings")
st.pyplot(fig1)

st.markdown('''
    <div class="info-panel">
        <div class="panel-title">Insight</div>
        <div class="panel-desc">
            Technical skills like Python, SQL, and Java remain the backbone of hiring. 
            However, a mix of communication and sales skills indicates that employers 
            value a hybrid skill set for many roles.
        </div>
    </div>
''', unsafe_allow_html=True)

st.write("---")

# 5. Row 2: Most Frequently Co-occurring Skills (Heatmap)
st.subheader("Frequently Co-occurring Skills")
from itertools import combinations
skill_df = df["tagsAndSkills"].dropna().str.split(",")
pairs = []
for skills_list in skill_df:
    skills_list = list(set([s.strip() for s in skills_list if s.strip()]))
    pairs.extend(combinations(skills_list, 2))

pair_df = pd.DataFrame(pairs, columns=["Skill1", "Skill2"]).value_counts().reset_index(name="Count")
top_skills_list = pd.concat([pair_df["Skill1"], pair_df["Skill2"]]).value_counts().head(10).index
pair_df = pair_df[pair_df["Skill1"].isin(top_skills_list) & pair_df["Skill2"].isin(top_skills_list)]

co_matrix = pd.pivot_table(pair_df, values="Count", index="Skill1", columns="Skill2", fill_value=0)
co_matrix = co_matrix.add(co_matrix.T, fill_value=0)

fig2, ax2 = plt.subplots(figsize=(10, 8))
sns.heatmap(co_matrix, cmap="Blues", annot=True, fmt=".0f", linewidths=0.5, linecolor="white", ax=ax2)
st.pyplot(fig2)

st.markdown('''
    <div class="info-panel">
        <div class="panel-title">Insight</div>
        <div class="panel-desc">
            Technologies tend to cluster by industry stack (e.g., frontend/backend/database). 
            Learning complementary skills within these clusters significantly boosts 
            your profile's relevance in the market.
        </div>
    </div>
''', unsafe_allow_html=True)
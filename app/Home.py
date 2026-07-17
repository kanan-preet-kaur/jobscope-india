import streamlit as st

from utils.loader import load_data
from services.dashboard_metrics import get_dashboard_metrics

from components.metrics import metric_card
from components.headers import page_header
from components.sidebar import render_sidebar

from utils.theme import apply_page_config, inject_theme_css

from config import (
    PROJECT_NAME,
    PROJECT_TAGLINE
)


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

dashboard_metrics = get_dashboard_metrics(df)



# =====================================
# HERO SECTION
# =====================================


page_header(
    title=PROJECT_NAME,
    subtitle=PROJECT_TAGLINE
)


st.markdown(
"""
<div class="hero-container">

<div class="hero-badge">
📊 Data Analytics Dashboard
</div>


<h3>
Understanding India's Employment Landscape
</h3>


<p>
Transforming thousands of job listings into meaningful insights
about salaries, skills, companies, locations, and hiring trends.
</p>


</div>

""",
unsafe_allow_html=True
)



st.write("")



# =====================================
# KEY METRICS
# =====================================


st.markdown(
"""
<div class="section-title">
<h2>📈 Market Overview</h2>
<p>
A quick snapshot of the Indian job market analysed through JobScope India.
</p>
</div>
""",
unsafe_allow_html=True
)



col1, col2, col3, col4 = st.columns(
    4,
    gap="large"
)



with col1:

    metric_card(
        "Total Jobs",
        f"{dashboard_metrics['total_jobs']:,}",
        "💼"
    )



with col2:

    metric_card(
        "Companies",
        f"{dashboard_metrics['total_companies']:,}",
        "🏢"
    )



with col3:

    metric_card(
        "Locations",
        f"{dashboard_metrics['total_locations']:,}",
        "📍"
    )



with col4:

    metric_card(
        "Skills",
        f"{dashboard_metrics['total_unique_skills']:,}",
        "🛠️"
    )




st.divider()



# =====================================
# PROJECT STORY
# =====================================


st.markdown(
"""
<div class="section-title">

<h2>
🚀 About JobScope India
</h2>

<p>
A data-driven platform designed to uncover patterns
within India's employment ecosystem.
</p>

</div>
""",
unsafe_allow_html=True
)



left, right = st.columns(
    [2,1],
    gap="large"
)



with left:


    st.markdown(
"""
<div class="content-card">

JobScope India is a data analytics dashboard built to understand
the rapidly evolving Indian employment landscape.

Using a dataset containing almost **98,000 job postings**, this platform
uncovers:

<ul>

<li>📈 Hiring demand trends</li>

<li>💰 Salary patterns</li>

<li>🏢 Company-wise opportunities</li>

<li>📍 Location-based hiring insights</li>

<li>🛠️ Most demanded skills</li>

<li>🎓 Experience requirements</li>

</ul>


The objective is to convert raw job market data into meaningful insights
that help students, professionals, recruiters, and career planners make
better decisions.

</div>
""",
unsafe_allow_html=True
)



with right:


    st.markdown(
"""
<div class="info-card">

<h3>
📊 JobScope India Snapshot
</h3>


<div class="snapshot-item">

<b>Total Job Listings: </b>
{:,}

</div>



<div class="snapshot-item">

<b>Companies Analysed: </b>
{:,}

</div>



<div class="snapshot-item">

<b>Locations Covered: </b>
{:,}

</div>



<div class="snapshot-item">

<b>Unique Skills Identified: </b>
{:,}

</div>
</div>

""".format(
    dashboard_metrics["total_jobs"],
    dashboard_metrics["total_companies"],
    dashboard_metrics["total_locations"],
    dashboard_metrics["total_unique_skills"]
),
unsafe_allow_html=True
)



st.divider()

# =====================================
# DATASET INFORMATION
# =====================================


st.markdown(
"""
<div class="section-title">

<h2>
📂 About the Dataset
</h2>

<p>
Understanding the data foundation behind JobScope India.
</p>

</div>
""",
unsafe_allow_html=True
)



dataset_left, dataset_right = st.columns(
    [1.8,1],
    gap="large"
)



with dataset_left:


    st.markdown(
"""
<div class="content-card">


The analysis is powered by the **Indian Job Market Dataset 2025**,
a large collection of job listings representing employment opportunities
across different industries and professional domains in India.


The dataset provides detailed information about:

<ul>

<li>💼 Job roles and titles</li>

<li>🏢 Companies and employer information</li>

<li>📍 Hiring locations</li>

<li>💰 Salary ranges</li>

<li>🛠 Required skills</li>

<li>🎓 Experience requirements</li>

<li>📅 Job posting information</li>

</ul>


After performing data cleaning, preprocessing, and feature engineering,
the raw job listings were transformed into a structured analytical dataset
for uncovering meaningful insights about India's employment ecosystem.


</div>

""",
unsafe_allow_html=True
)




with dataset_right:
    st.markdown(
"""
<div class="info-card">


<h3>
📊 Dataset Snapshot
</h3>


<div class="mini-stat">

<p>
Original Dataset
</p>

<h2>
97,929
</h2>

<span>
Job Listings
</span>

</div>



<div class="mini-stat">

<p>
Original Features
</p>

<h2>
17
</h2>

<span>
Attributes
</span>

</div>



<div class="mini-stat">

<p>
Processed Features
</p>

<h2>
19
</h2>

<span>
Analytical Columns
</span>

</div>



</div>

""",
unsafe_allow_html=True
)



st.divider()



# =====================================
# DATASET FEATURES
# =====================================


st.markdown(
"""
<div class="section-title">

<h2>
🧩 Dataset Structure
</h2>

<p>
Key information captured within the dataset.
</p>

</div>
""",
unsafe_allow_html=True
)



feature_data = {

"Category": [

"💼 Job Information",

"🏢 Company Details",

"📍 Location Data",

"💰 Salary Data",

"🛠 Skills",

"🎓 Experience",

"📅 Job Metadata"

],

"Information Available": [

"Job titles, roles, identifiers",

"Company names, ratings, reviews",

"Hiring locations and cities",

"Minimum and maximum salary ranges",

"Required skills and technologies",

"Required experience levels",

"Posting dates and job attributes"

]

}



dataset_features = st.dataframe(
    feature_data,
    use_container_width=True,
    hide_index=True
)



st.divider()



# =====================================
# CLEANED DATA PREVIEW
# =====================================


st.markdown(
"""
<div class="section-title">

<h2>
🔍 Cleaned Dataset Preview
</h2>

<p>
First 15 records after data cleaning and preprocessing.
</p>

</div>
""",
unsafe_allow_html=True
)



with st.container():


    st.dataframe(
        df.head(15),
        use_container_width=True,
        height=450
    )

st.divider()

# =====================================
# FEATURES / ANALYTICS
# =====================================


st.markdown(
"""
<div class="section-title">

<h2>
🔍 What You Can Explore
</h2>

<p>
Discover meaningful patterns and trends hidden within India's employment data.
</p>

</div>
""",
unsafe_allow_html=True
)



feature1, feature2, feature3 = st.columns(
    3,
    gap="large"
)



with feature1:

    st.markdown(
"""
<div class="content-card">


<h3>
💰 Salary Intelligence
</h3>


<p>
Analyze salary ranges, compensation patterns,
and earning potential across different roles
and experience levels.
</p>


</div>

""",
unsafe_allow_html=True
)




with feature2:

    st.markdown(
"""
<div class="content-card">


<h3>
📍 Market Geography
</h3>


<p>
Explore hiring distribution across different
locations and identify major employment hubs.
</p>


</div>

""",
unsafe_allow_html=True
)




with feature3:

    st.markdown(
"""
<div class="content-card">


<h3>
🛠 Skill Demand
</h3>


<p>
Identify the most frequently requested skills
and understand changing market requirements.
</p>


</div>

""",
unsafe_allow_html=True
)



st.divider()



# =====================================
# FUTURE SCOPE
# =====================================


st.markdown(
"""
<div class="section-title">

<h2>
🚀 Future Scope
</h2>

<p>
Planned enhancements to make JobScope India more powerful.
</p>

</div>
""",
unsafe_allow_html=True
)



future1, future2, future3 = st.columns(
    3,
    gap="large"
)



with future1:

    st.markdown(
"""
<div class="content-card">

<h3>
🤖 Advanced Analytics
</h3>


<p>
Implement predictive analytics and machine learning
models to forecast hiring trends and salary patterns.
</p>


</div>
""",
unsafe_allow_html=True
)




with future2:

    st.markdown(
"""
<div class="content-card">

<h3>
🧠 NLP-Based Insights
</h3>


<p>
Extract deeper insights from job descriptions
through natural language processing techniques.
</p>


</div>
""",
unsafe_allow_html=True
)




with future3:

    st.markdown(
"""
<div class="content-card">

<h3>
🌐 Real-Time Data Integration
</h3>


<p>
Connect live job sources to provide continuously
updated employment insights.
</p>


</div>
""",
unsafe_allow_html=True
)




st.divider()



# =====================================
# TECHNOLOGY STACK
# =====================================


st.markdown(
"""
<div class="section-title">

<h2>
⚙️ Built With
</h2>

<p>
Technologies used to build the JobScope India analytics platform.
</p>

</div>
""",
unsafe_allow_html=True
)



stack = [

"Python",

"Pandas",

"NumPy",

"Matplotlib",

"Plotly",

"Streamlit",

"Data Visualization"

]



cols = st.columns(
len(stack),
gap="small"
)



for col, item in zip(cols, stack):

    with col:

        st.markdown(
        f"""
        <div class="tech-pill">

        {item}

        </div>
        """,
        unsafe_allow_html=True
        )




st.divider()



# =====================================
# FOOTER
# =====================================


st.markdown(
"""
<div class="footer">


<h3>
JobScope India
</h3>


<p>
Data-Driven Insights for India's Employment Landscape
</p>


<p>
Built with ❤️ by <b>Kanan Preet Kaur</b>
</p>


</div>
""",
unsafe_allow_html=True
)
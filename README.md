# 🇮🇳 JobScope India

### India's Job Market Intelligence Platform

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-5A9BD5?style=for-the-badge)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

**Transforming India's employment data into actionable intelligence through interactive analytics, salary benchmarking, hiring trends, and workforce insights.**

🌐 **Live Demo:** *Coming Soon*  
🔗 **GitHub Repository:** *https://github.com/kanan-preet-kaur/jobscope-india*

</div>

---

# 📌 Overview

**JobScope India** is a full-stack data analytics platform built to help students, recruiters, working professionals, and mentors understand India's rapidly evolving job market through interactive business intelligence.

Using **97,929 real-world job listings**, the platform uncovers hiring trends, salary distributions, in-demand skills, company activity, experience requirements, and geographic opportunities through an intuitive and modern dashboard.

Beyond analytics, the project demonstrates the complete lifecycle of building a real-world software product—from data preprocessing and exploratory analysis to authentication, modular architecture, reusable components, and deployment-ready development.

---

# 🚀 Why JobScope India?

The Indian job market is constantly evolving, yet many students and professionals struggle to answer questions such as:

- Which companies are hiring the most?
- Which cities offer the best opportunities?
- Which skills are currently in demand?
- How do salaries vary across industries and experience levels?
- What does the overall hiring landscape look like?

JobScope India answers these questions through interactive visualizations and business insights, making employment data easier to understand and enabling better career decisions.

---

# ✨ Features

### 📊 Interactive Analytics

- Comprehensive dashboard with 15+ interactive visualizations
- KPI cards summarizing key market statistics
- Interactive charts powered by Plotly
- Clean, responsive, and modern UI

### 📈 Market Intelligence

- Compensation & Salary Analysis
- Job Market Analysis
- Skills Demand Analysis
- Company Hiring Analysis
- Experience-Level Analysis
- Geographic Hiring Trends
- Business Insights & Key Findings

### 🔐 Authentication

- Secure User Registration
- User Login System
- Password Hashing using Passlib & bcrypt
- SQLite Database Integration
- Session Management
- Protected Dashboard Pages

---

# ⭐ What Makes This Project Different?

Unlike a traditional Streamlit dashboard, **JobScope India** was designed as a complete software product.

The project focuses not only on extracting insights from data but also on building an application that is modular, secure, scalable, and easy to maintain.

It demonstrates concepts such as:

- Modular project architecture
- Separation of concerns
- Reusable UI components
- Secure authentication workflow
- Database integration
- Session management
- Custom UI/UX using CSS
- Deployment-ready application structure

---

# 📊 Dataset

| Metric | Value |
|---------|------:|
| Records | **97,929** |
| Features | **19** |
| Companies | **18,617** |
| Locations | **10,064** |
| Unique Skills | **59,438** |

**Source:** Kaggle – Indian Job Market Dataset (2025–2026)

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| **Programming** | Python |
| **Data Analysis** | Pandas, NumPy |
| **Visualization** | Plotly, Matplotlib, Seaborn |
| **Dashboard Development** | Streamlit |
| **Database** | SQLite |
| **Authentication** | Passlib, bcrypt |
| **Development Tools** | Jupyter Notebook, Git, GitHub, VS Code |

---

# 📂 Project Structure

# 📂 Project Structure

```text
jobscope-india/
│
├── app/
│   │
│   ├── Home.py                          # Landing page & dashboard overview
│   ├── config.py                        # Project-wide constants & configuration
│   │
│   ├── assets/
│   │   ├── css/
│   │   │   └── main.css                 # Global styling
│   │   │
│   │   └── icons/
│   │       └── logo.png                 # Application logo
│   │
│   ├── components/
│   │   ├── __init__.py
│   │   ├── headers.py                   # Page headers
│   │   ├── metrics.py                   # KPI metric cards
│   │   └── sidebar.py                   # Navigation sidebar
│   │
│   ├── database/
│   │   ├── auth.py                      # Authentication logic
│   │   ├── database.py                  # SQLite database connection
│   │   └── users.py                     # User registration & login operations
│   │
│   ├── pages/
│   │   ├── 00_Authentication.py         # Login & Registration
│   │   ├── 01_Compensation_Analysis.py  # Salary & compensation insights
│   │   ├── 02_Job_Market_Analysis.py    # Hiring trends & market overview
│   │   ├── 03_Skills_Analysis.py        # Skills demand analysis
│   │   ├── 04_Company_Analysis.py       # Company hiring analysis
│   │   ├── 05_Experience_Analysis.py    # Experience-level analysis
│   │   ├── 06_Geographic_Analysis.py    # Geographic hiring trends
│   │   └── 07_Key_Findings.py           # Business insights & conclusions
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── dashboard_metrics.py         # Dashboard KPI calculations
│   │
│   └── utils/
│       ├── __init__.py
│       ├── loader.py                    # Dataset loading utilities
│       └── theme.py                     # Streamlit theme & page configuration
│
├── data/
│   ├── raw/
│   │   └── indian-job-market-dataset-2025.xlsx
│   │
│   └── processed/
│       └── cleaned_job_market.csv
│
├── notebooks/
│   ├── 01_data_understanding.ipynb      # Dataset exploration
│   ├── 02_data_cleaning.ipynb           # Data preprocessing
│   └── 03_exploratory_data_analysis.ipynb # Exploratory Data Analysis (EDA)
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# 📊 Dashboard Overview

| Page | Description |
|------|-------------|
| 🏠 Home | Platform overview and key market metrics |
| 🔐 Authentication | User registration and login |
| 💰 Compensation Analysis | Salary distributions and compensation insights |
| 📈 Job Market Analysis | Hiring trends and employment landscape |
| 🛠️ Skills Analysis | Most in-demand skills and technologies |
| 🏢 Company Analysis | Company hiring activity and recruiter insights |
| 👨‍💼 Experience Analysis | Experience-wise hiring patterns |
| 🌍 Geographic Analysis | Regional hiring trends across India |
| 📌 Key Findings | Summary of business insights and observations |

---

# 📈 Home Dashboard Metrics

The landing dashboard provides a quick snapshot of the Indian job market through key indicators including:

- 💼 Total Job Postings
- 🏢 Total Companies
- 📍 Hiring Locations
- 🛠️ Unique Skills

These metrics provide users with an immediate overview before exploring detailed analyses.

---

# 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/kanan-preet-kaur/jobscope-india
```

### Navigate to the Project

```bash
cd jobscope-india
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app/Home.py
```

---

# 💡 Skills Demonstrated

This project provided practical experience in both **Data Analytics** and **Software Engineering**, including:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Interactive Data Visualization
- Business Intelligence Dashboard Design
- Authentication & Authorization
- SQLite Database Integration
- Password Security
- Session Management
- Modular Application Development
- Reusable Component Design
- UI/UX Design with Custom CSS
- Git & GitHub Workflow
- Deployment-Ready Project Organization

---

# 🔮 Future Enhancements

- 🤖 Machine Learning-Based Salary Prediction
- 📝 NLP Analysis of Job Descriptions
- 📊 Advanced Workforce Analytics
- 🌐 Real-Time Job Market Data Integration

---

# 👩‍💻 Author

**Kanan Preet Kaur**

B.Tech Computer Science & Engineering

Passionate about **Data Analytics**, **Software Engineering**, **Data Visualization**, and building impactful applications.

**GitHub:** *https://github.com/kanan-preet-kaur*

**LinkedIn:** *https://www.linkedin.com/in/kanan-preet-kaur/*

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

**Built with ❤️ using Python, Streamlit, Pandas, NumPy, Plotly, Matplotlib, Seaborn, SQLite, Passlib & bcrypt**

</div>

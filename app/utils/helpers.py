import os
import pandas as pd
import streamlit as st

@st.cache_data
def load_job_data():
    """
    Centralized loader to find the cleaned dataset regardless of 
    whether the app is run from root or from a subpage.
    """
    # 1. Get the path to the directory where 'loader.py' lives
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Look for 'data/processed/cleaned_job_market.csv' 
    # relative to the project root (one level up from /utils)
    project_root = os.path.dirname(current_dir)
    data_path = os.path.join(project_root, "data", "processed", "cleaned_job_market.csv")
    
    # Verify the file exists
    if not os.path.exists(data_path):
        st.error(f"Could not find the dataset at: {data_path}")
        return pd.DataFrame(), pd.DataFrame()
    
    # 3. Load the dataframe
    df = pd.read_csv(data_path)
    
    # 4. Perform your exact cleaning/subsetting logic here so 
    # every page gets the same filtered data
    salary_df = df[
        (df["averageSalary"] > 0) &
        (df["averageSalary"] <= df["averageSalary"].quantile(0.99))
    ].copy()
    
    return df, salary_df
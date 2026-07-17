from pathlib import Path
import pandas as pd
import streamlit as st


@st.cache_data(show_spinner=False)
def load_data():
    """
    Load the cleaned dataset once and cache it.
    """

    project_root = Path(__file__).resolve().parents[2]

    data_path = (
        project_root
        / "data"
        / "processed"
        / "cleaned_job_market.csv"
    )

    df = pd.read_csv(data_path)

    return df
import streamlit as st
from pathlib import Path
from config import COLORS
from config import LOGO_PATH


from config import LOGO_PATH

def apply_page_config():

    st.set_page_config(
        page_title="JobScope India | Analytics Dashboard",
        page_icon=str(LOGO_PATH),
        layout="wide",
        initial_sidebar_state="expanded"
    )


def inject_theme_css():

    st.markdown(
        f"""
        <style>

        /* =====================================
           MAIN APPLICATION
        ====================================== */

        .stApp {{
            background-color: {COLORS["background"]};
            color: {COLORS["text_primary"]};
        }}



        /* =====================================
           SIDEBAR
        ====================================== */

        section[data-testid="stSidebar"] {{

            background-color: #111827;

        }}


        section[data-testid="stSidebar"] * {{

            color: #F8FAFC;

        }}


        section[data-testid="stSidebar"] .stCaption {{

            color:#94A3B8;

        }}


        /* Sidebar navigation */

        div[data-testid="stSidebarNav"] span {{

            color:#CBD5E1 !important;

        }}


        div[data-testid="stSidebarNav"] span:hover {{

            color:white !important;

        }}


        div[data-testid="stSidebarNavLink"] {{

            background-color:transparent;

        }}


        div[data-testid="stSidebarNavLink"]:hover {{

            background-color:#1E293B;

            border-radius:10px;

        }}



        /* =====================================
           REMOVE STREAMLIT HEADER
        ====================================== */

        header {{
            visibility:hidden;
        }}



        /* =====================================
           TYPOGRAPHY
        ====================================== */

        h1,h2,h3,h4 {{
            color:{COLORS["text_primary"]};
        }}


        p {{
            color:{COLORS["text_secondary"]};
        }}



        /* =====================================
           CARDS
        ====================================== */

        .card {{

            background:{COLORS["card"]};

            padding:20px;

            border-radius:16px;

            border:1px solid rgba(255,255,255,0.08);

            box-shadow:
            0px 10px 30px rgba(0,0,0,0.25);

        }}


        </style>
        """,
        unsafe_allow_html=True
    )

    css_path = Path(__file__).parent.parent / "assets" / "css" / "main.css"

    with open(css_path, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
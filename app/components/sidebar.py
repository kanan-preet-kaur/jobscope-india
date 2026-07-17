import streamlit as st
from config import PROJECT_NAME, PROJECT_TAGLINE, LOGO_PATH


def render_sidebar():

    with st.sidebar:

        # ===============================
        # BRAND SECTION
        # ===============================

        try:
            st.image(
                LOGO_PATH,
                width=90
            )

        except:
            st.markdown(
                "📊",
                unsafe_allow_html=True
            )


        st.markdown(
            f"""
            <h2 style="
            margin-bottom:0px;
            ">
            {PROJECT_NAME}
            </h2>
            """,
            unsafe_allow_html=True
        )


        st.caption(
            "Analytics • Insights • Careers"
        )


        st.divider()


        # ===============================
        # PROJECT INFO
        # ===============================

        st.markdown(
            """
            ### 📌 About

            Explore India's technology job market through
            interactive analytics covering:

            - Salaries
            - Skills
            - Companies
            - Hiring trends
            - Experience patterns

            """
        )


        st.divider()


        st.markdown(
            """
            ### 🚀 Built With

            🐍 Python   
            🔢 NumPy  
            🗃️ Pandas  
            📉 Matplotlib  
            🌊 Seaborn  
            📊 Plotly  
            🎨 Streamlit

            """
        )


        st.divider()


        st.caption(
            "JobScope India © 2026"
        )
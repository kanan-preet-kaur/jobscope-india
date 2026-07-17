import streamlit as st


def page_header(
    title: str,
    subtitle: str,
):
    st.markdown(
        f"""
        <div style="
            padding:22px;
            border-radius:18px;
            background:linear-gradient(
                135deg,
                #182033 0%,
                #111827 100%
            );
            margin-bottom:24px;
        ">

        <h1 style="
            color:white;
            margin-bottom:8px;
        ">
        {title}
        </h1>

        <p style="
            color:#E2E8F0;
            font-size:18px;
            margin:0;
        ">
        {subtitle}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )
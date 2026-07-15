import streamlit as st

def render_insights_card(title, insights):
    st.markdown(f"""
        <div style="background-color: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 8px; padding: 16px; margin-top: 15px;">
            <h4 style="color: #1E3A8A; margin-top: 0;">💡 {title}</h4>
            <ul style="margin-bottom: 0; padding-left: 20px; color: #1E293B;">
                {"".join([f"<li>{item}</li>" for item in insights])}
            </ul>
        </div>
    """, unsafe_allow_html=True)
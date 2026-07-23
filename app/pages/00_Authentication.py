import streamlit as st

from utils.theme import apply_page_config, inject_theme_css
from components.sidebar import render_sidebar
from database.auth import register_user, login_user
import sqlite3


# =====================================
# INITIALIZATION
# =====================================

apply_page_config()

inject_theme_css()

render_sidebar()

# =====================================
# SECTION 1: HERO SECTION
# =====================================

from config import LOGO_PATH

logo_col, text_col = st.columns([2, 5], vertical_alignment="center")

with logo_col:
    st.image(
        LOGO_PATH,
        width=250
    )

with text_col:

    st.markdown(
        """
        <div class="hero-section">
            <h1>JobScope India</h1>
            <h3><i>India's Job Market Intelligence Platform</i></h3>
            <p>
                Analyze India's evolving employment landscape through
                interactive dashboards and intelligent data visualizations.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()


# =====================================
# SECTION 2: INTRODUCTION CARD
# =====================================

st.markdown(
    """
    <div class="content-card" style="text-align: center;">
        <h3>📌 Intelligence at Your Fingertips</h3>
        <p>
            JobScope India aggregates data across industries, skills, and regions to provide professionals and recruiters with high-precision labor market insights.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.divider()


# =====================================
# CONDITIONAL VIEW CONTROL
# =====================================

is_authenticated = st.session_state.get("authenticated", False)
user_name = st.session_state.get("user_name", "User")


if is_authenticated:
    # =====================================
    # SECTION 5: AUTHENTICATED STATE VIEW
    # =====================================

    st.markdown(
        f"""
        <div class="content-card" style="text-align: center; border-left: 4px solid #10B981;">
            <h2>🎉 Welcome Back, {user_name}!</h2>
            <p>You are successfully signed in to JobScope India. You now have full access to all dashboard analytics and report views.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    if st.button("🚀 Open Dashboard", use_container_width=True):
        st.switch_page("Home.py")

    st.write("")
    st.write("")

    # Authenticated Benefits Showcase
    st.markdown(
        """
        <h2 class="section-heading">
        💡 Your Platform Access
        </h2>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4, gap="medium")

    with col1:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-icon">📊</div>
                <div class="metric-title">Employment Analytics</div>
                <div class="metric-value">Unlocked</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-icon">💼</div>
                <div class="metric-title">Market Intelligence</div>
                <div class="metric-value">Unlocked</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-icon">📈</div>
                <div class="metric-title">Salary Benchmark</div>
                <div class="metric-value">Unlocked</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-icon">🎯</div>
                <div class="metric-title">Career Trends</div>
                <div class="metric-value">Unlocked</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

else:
    # =====================================
    # SECTION 3: MAIN AUTHENTICATION AREA
    # =====================================

    st.markdown(
        """
        <h2 class="section-heading">
        📝 Access Platform
        </h2>
        """,
        unsafe_allow_html=True,
    )

    left_col, right_col = st.columns([1, 1], gap="large")

    # --- LEFT COLUMN: AUTHENTICATION CARD ---
    with left_col:
        st.markdown(
            """
            <div class="content-card">
            """,
            unsafe_allow_html=True,
        )

        create_tab, signin_tab = st.tabs(["Create Account", "Sign In"])

        # Create Account Tab
        with create_tab:
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            password = st.text_input("Password", type="password")

            st.write("")

            register = st.button(
                "🚀 Create Account", use_container_width=True
            )

            if register:
                if not name or not email or not password:
                    st.error("Please fill in all fields.")
                else:
                    try:
                        register_user(name, email, password)
                        st.success("Account created successfully!")
                        st.session_state.authenticated = True
                        st.session_state.user_name = name
                        st.switch_page("Home.py")
                    except sqlite3.IntegrityError:
                        st.error("An account with this email already exists.")
                    except Exception as e:
                        st.error(f"Error: {e}")

        # Sign In Tab
        with signin_tab:
            login_email = st.text_input("Email Address", key="login_email")
            login_password = st.text_input(
                "Password", type="password", key="login_password"
            )

            st.write("")

            login = st.button("🔑 Log In", use_container_width=True)

            if login:
                user_name_found = login_user(login_email, login_password)

                if user_name_found:
                    st.session_state.authenticated = True
                    st.session_state.user_name = user_name_found
                    st.success("Logged in successfully!")
                    st.switch_page("Home.py")
                else:
                    st.error("Invalid email or password.")

        st.markdown(
            """
            </div>
            """,
            unsafe_allow_html=True,
        )

    # --- RIGHT COLUMN: PLATFORM BENEFITS & CONTEXT ---
    with right_col:
        st.markdown(
            """
            <h2 class="section-heading">
            🚀 Why Choose JobScope?
            </h2>
            """,
            unsafe_allow_html=True,
        )

        # Show KPI cards for Create Account state, or simple Info card for Sign In state
        # In Streamlit, right_col renders statically alongside the tabs
        b1, b2 = st.columns(2, gap="medium")

        with b1:
            st.markdown(
                """
                <div class="metric-card">
                    <div class="metric-icon">📊</div>
                    <div class="metric-title">Employment Analytics</div>
                    <div class="metric-value">Dashboard Access</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with b2:
            st.markdown(
                """
                <div class="metric-card">
                    <div class="metric-icon">💼</div>
                    <div class="metric-title">Market Intelligence</div>
                    <div class="metric-value">360° Scope</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.write("")

        b3, b4 = st.columns(2, gap="medium")

        with b3:
            st.markdown(
                """
                <div class="metric-card">
                    <div class="metric-icon">📈</div>
                    <div class="metric-title">Salary Insights</div>
                    <div class="metric-value">Industry Data</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with b4:
            st.markdown(
                """
                <div class="metric-card">
                    <div class="metric-icon">🎯</div>
                    <div class="metric-title">Career Discovery</div>
                    <div class="metric-value">Data-Driven</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


st.divider()

# =====================================
# SECTION 4: PLATFORM HIGHLIGHTS
# =====================================

st.write("")
st.write("")

st.markdown(
    """
    <h2 class="section-heading">
    🌐 Platform Metrics & Coverage
    </h2>
    """,
    unsafe_allow_html=True,
)

m1, m2, m3, m4 = st.columns(4, gap="medium")

with m1:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-icon">💼</div>
            <div class="metric-title">Tracked Jobs</div>
            <div class="metric-value">97K+</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with m2:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-icon">⚡</div>
            <div class="metric-title">In-Demand Skills</div>
            <div class="metric-value">59K+</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with m3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-icon">🏙️</div>
            <div class="metric-title">Locations</div>
            <div class="metric-value">10K+</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with m4:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-icon">🏢</div>
            <div class="metric-title">Active Companies</div>
            <div class="metric-value">18K+</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
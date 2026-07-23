# ============================================================
# JOBSCOPE INDIA - APPLICATION CONFIGURATION
# ============================================================

PROJECT_NAME = "JobScope India"

PROJECT_TAGLINE = (
    "Interactive analytics platform exploring India's "
    "job market trends, salaries, skills, and hiring insights."
)

PROJECT_DESCRIPTION = """
JobScope India transforms raw job market data into actionable
career insights using interactive visual analytics.
"""

# ============================================================
# BRANDING
# ============================================================

from pathlib import Path

BASE_DIR = Path(__file__).parent

LOGO_PATH = BASE_DIR / "assets" / "icons" / "logo.png"


# ============================================================
# THEME COLORS
# ============================================================

COLORS = {

    # Main brand
    "primary": "#2563EB",
    "secondary": "#7C3AED",

    # Background
    "background": "#0F172A",
    "surface": "#111827",
    "card": "#1E293B",

    # Text
    "text_primary": "#F8FAFC",
    "text_secondary": "#CBD5E1",

    # Accent
    "success": "#10B981",
    "warning": "#F59E0B",
    "danger": "#EF4444",

}


# ============================================================
# DASHBOARD SETTINGS
# ============================================================

PAGE_LAYOUT = "wide"

PAGE_TITLE = "JobScope India | Analytics Dashboard"
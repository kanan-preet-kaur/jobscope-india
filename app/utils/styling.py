import streamlit as st

def get_theme_colors():
    return {
        "primary": "#1E3A8A",      # Midnight/Steel Blue
        "success": "#10B981",      # Mint Green
        "accent": "#F59E0B",       # Warm Amber
        "muted": "#64748B",        # Slate Muted Gray
        "dark": "#1E293B"          # Text Dark Black
    }

def apply_custom_css():
    colors = get_theme_colors()
    st.markdown(f"""
        <style>
        .stApp {{
            background-color: #F8FAFC;
        }}
        .main-title {{
            font-size: 2.5rem !important;
            font-weight: 800 !important;
            color: {colors['primary']};
            margin-bottom: 0.2rem !important;
        }}
        .subtitle {{
            font-size: 1.1rem !important;
            color: {colors['muted']};
            margin-bottom: 2rem !important;
        }}
        .metric-card {{
            background-color: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 22px;
            box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
            margin-bottom: 1rem;
        }}
        .metric-card.hero {{
            background: linear-gradient(135deg, {colors['primary']} 0%, #1D4ED8 100%);
            color: #FFFFFF;
            border: none;
        }}
        .metric-title {{
            font-size: 0.85rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 6px;
        }}
        .metric-card.hero .metric-title {{ color: #DBEAFE; }}
        .metric-card.standard .metric-title {{ color: {colors['muted']}; }}
        
        .metric-value {{
            font-size: 2.2rem;
            font-weight: 700;
            line-height: 1;
        }}
        .metric-card.hero .metric-value {{ color: #FFFFFF; }}
        .metric-card.standard .metric-value {{ color: {colors['dark']}; }}
        
        .metric-desc {{
            font-size: 0.8rem;
            margin-top: 8px;
            color: #94A3B8;
        }}
        .metric-card.hero .metric-desc {{ color: #93C5FD; }}
        
        .info-panel {{
            background-color: #FFFFFF;
            border-left: 4px solid {colors['primary']};
            border-radius: 8px;
            padding: 18px;
            margin-bottom: 12px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }}
        .panel-title {{
            font-weight: 700;
            color: {colors['dark']};
            margin-bottom: 4px;
        }}
        .panel-desc {{
            font-size: 0.9rem;
            color: #475569;
        }}
        </style>
    """, unsafe_allow_html=True)
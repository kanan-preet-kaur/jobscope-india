import streamlit as st

def apply_global_filters(df):
    st.sidebar.header("🔍 Interactive Filters")
    
    # 1. Location Filter
    locations = sorted(df['location'].unique().tolist()) if 'location' in df.columns else []
    selected_locations = st.sidebar.multiselect("Select Job Locations", locations, default=locations[:4])
    
    # 2. Experience Filter
    min_exp, max_exp = 0, 15
    if 'averageExperience' in df.columns:
        min_exp = int(df['averageExperience'].min())
        max_exp = int(df['averageExperience'].max())
    selected_exp = st.sidebar.slider("Experience Range (Years)", min_exp, max_exp, (min_exp, max_exp))
    
    # Filter dataset
    filtered_df = df.copy()
    if selected_locations:
        filtered_df = filtered_df[filtered_df['location'].isin(selected_locations)]
    if 'averageExperience' in filtered_df.columns:
        filtered_df = filtered_df[
            (filtered_df['averageExperience'] >= selected_exp[0]) & 
            (filtered_df['averageExperience'] <= selected_exp[1])
        ]
        
    return filtered_df
import streamlit as st\
import pandas as pd\
import plotly.graph_objects as go\
from datetime import datetime\
\
# --- CONFIGURATION ---\
st.set_page_config(page_title="MorningOS", page_icon="\uc0\u9728 \u65039 ", layout="wide")\
\
# --- CUSTOM CSS FOR THE "OS" FEEL ---\
st.markdown("""\
    <style>\
    .main \{ background-color: #0e1117; color: #ffffff; \}\
    .stMetric \{ background-color: #161b22; border-radius: 10px; padding: 15px; border: 1px solid #30363d; \}\
    </style>\
    """, unsafe_allow_html=True)\
\
# --- APP LOGIC ---\
st.title("\uc0\u9728 \u65039  MorningOS v1.0")\
st.subheader(f"Status Report: \{datetime.now().strftime('%A, %b %d, %2026')\}")\
\
# --- PILLAR 1: FINANCIALS ---\
with st.expander("\uc0\u55357 \u56496  Financial Targets", expanded=True):\
    col1, col2 = st.columns(2)\
    nw_current = col1.number_input("Current Net Worth (CAD)", value=850000)\
    save_current = col2.number_input("Current Savings (CAD)", value=130000)\
    \
    # Progress Bars\
    st.write(f"Net Worth Progress: **\{int((nw_current/900000)*100)\}%**")\
    st.progress(nw_current/900000)\
\
# --- PILLAR 2: FITNESS PERFORMANCE ---\
with st.expander("\uc0\u55356 \u57291 \u65039  Fitness Excellence", expanded=True):\
    c1, c2, c3 = st.columns(3)\
    squat = c1.number_input("Est. Squat 1RM", value=315)\
    bench = c2.number_input("Est. Bench 1RM", value=225)\
    cardio = c3.selectbox("Weekly Cardio Done?", ["0/2", "1/2", "2/2"])\
    \
    # Simple Strength Trend Chart\
    strength_data = pd.DataFrame(\{"Lift": ["Squat", "Bench"], "Current": [squat, bench], "Target": [405, 275]\})\
    fig = go.Figure(data=[\
        go.Bar(name='Current', x=strength_data['Lift'], y=strength_data['Current'], marker_color='#1f77b4'),\
        go.Bar(name='Target', x=strength_data['Lift'], y=strength_data['Target'], marker_color='#2ca02c')\
    ])\
    fig.update_layout(barmode='group', height=300, margin=dict(l=20, r=20, t=20, b=20))\
    st.plotly_chart(fig, use_container_width=True)\
\
# --- PILLAR 3: FATHERHOOD & GRATITUDE ---\
with st.expander("\uc0\u10084 \u65039  Relationship & Fatherhood", expanded=True):\
    presence = st.slider("Presence Quality (1-10)", 1, 10, 8)\
    gratitude = st.checkbox("Expressed Gratitude to Wife Today?")\
    if gratitude:\
        st.success("Dopamine loop closed. Relationship equity increased.")\
\
# --- THE DAILY PROMPT ---\
st.markdown("---")\
st.info("**Neuroscience Anchor:** *Your cortisol peaks 30-45 mins after waking. Use this time for 'Deep Work' or your 60-min strength session before the AWS pings begin.*")}

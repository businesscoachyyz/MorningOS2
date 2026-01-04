import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Basic Page Setup
st.set_page_config(page_title="MorningOS", page_icon="☀️")

st.title("☀️ MorningOS v1.0")
st.write(f"Logged in: {datetime.now().strftime('%A, %b %d, %2026')}")

# --- PILLAR 1: FINANCIALS ---
st.header("💰 Financial Targets")
nw_current = st.number_input("Current Net Worth (CAD)", value=850000)
save_current = st.number_input("Current Savings (CAD)", value=130000)

nw_pct = min(nw_current / 900000, 1.0)
st.write(f"Net Worth Goal Progress: **{int(nw_pct * 100)}%**")
st.progress(nw_pct)

# --- PILLAR 2: FITNESS ---
st.header("🏋️ Fitness Excellence")
col1, col2 = st.columns(2)
squat = col1.number_input("Current Squat (lbs)", value=315)
bench = col2.number_input("Current Bench (lbs)", value=225)

# --- PILLAR 3: FAMILY & GRATITUDE ---
st.header("❤️ Family Pillar")
presence = st.slider("Presence Rating (1-10)", 1, 10, 8)
gratitude = st.checkbox("Did I express gratitude to my wife today?")

if gratitude:
    st.success("Dopamine loop closed. Great work.")

st.divider()
st.info("System Online. Ready for Sunday Weekly Review.")

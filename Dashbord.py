import streamlit as st
from components.sidebar import sidebar
from components.stat_card import stat_card
from components.grade_distribution import grade_distribution
from components.performance_chart import performance_chart
from components.score_distribution import score_distribution
st.set_page_config(layout="wide")

with open("styles/bootstrap.html") as f:
    st.markdown(f.read(), unsafe_allow_html=True)
with open("styles/custom.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)    

st.sidebar.title("Instractor dashboard")
if st.sidebar.button("Dashboard"):
    st.session_state.page = "Dashboard"
if st.sidebar.button("Statistics"):
    st.session_state.page = "Statistics"
if st.sidebar.button("Settings"):
    st.session_state.page = "Settings"
if st.sidebar.button("Logout"):
    st.session_state.page = "Logout"

st.markdown("<h3>Students Performance Statistics</h3>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1: stat_card("Total Students", "24")
with c2: stat_card("Average Score", "62%")
with c3: stat_card("Maximum Score", "98%")
with c4: stat_card("At Risk", "3", positive=False)
    
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    grade_distribution()
with col2:
    performance_chart()

col_left, col_center, col_right = st.columns([1, 2, 1])
with col_center:
    score_distribution()

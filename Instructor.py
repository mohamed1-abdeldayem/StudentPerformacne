import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import date

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    
    page_title="Class Performance Statistics",
    layout="wide",
)

# ------------------ GLOBAL CSS (DARK MODE) ------------------
st.markdown("""
<style>

/* App background */
.stApp {
    background-color: #0f172a;
    color: #e5e7eb;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #020617;
    border-right: 1px solid #1e293b;
}

/* Sidebar title */
.sidebar-title {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 20px;
    color: #38bdf8;
}

/* Sidebar buttons */
.sidebar-btn button {
    width: 100%;
    background: none;
    border: none;
    text-align: left;
    padding: 12px 16px;
    font-size: 15px;
    border-radius: 8px;
    color: #cbd5f5;
}

/* Active sidebar */
.sidebar-btn-active button {
    background-color: #1e293b;
    color: #38bdf8;
    font-weight: 600;
}

/* Hover */
.sidebar-btn button:hover {
    background-color: #020617;
}

/* Navbar */
.navbar {
    background-color: #020617;
    border-bottom: 1px solid #1e293b;
}

/* Inputs */
input {
    background-color: #020617 !important;
    color: #e5e7eb !important;
    border-radius: 20px !important;
    border: 1px solid #1e293b !important;
}

/* Metric cards */
[data-testid="metric-container"] {
    background-color: #020617;
    border-radius: 14px;
    padding: 20px;
    border: 1px solid #1e293b;
}

/* Metric text */
[data-testid="metric-container"] * {
    color: #e5e7eb !important;
}

/* Divider */
hr {
    border-color: #1e293b;
}

/* Footer */
.footer {
    color: #64748b;
    text-align: center;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
st.sidebar.markdown("<div class='sidebar-title'>🎓 Student Predictor</div>", unsafe_allow_html=True)
st.sidebar.markdown("---")

if "menu" not in st.session_state:
    st.session_state.menu = "Statistics"

def sidebar_button(label, key):
    active = st.session_state.menu == key
    css = "sidebar-btn-active" if active else "sidebar-btn"
    st.sidebar.markdown(f"<div class='{css}'>", unsafe_allow_html=True)
    if st.sidebar.button(label, key=key):
        st.session_state.menu = key
    st.sidebar.markdown("</div>", unsafe_allow_html=True)

sidebar_button("🏠 Dashboard", "Dashboard")
sidebar_button("📊 Statistics", "Statistics")


st.sidebar.markdown("---")
st.sidebar.button("🚪 Logout")

# ------------------ NAVBAR ------------------
nav1, nav2, nav3 = st.columns([2, 4, 1])

with nav1:
    st.markdown("### 🎓 Student Predictor")

with nav2:
    st.text_input("Search...", label_visibility="collapsed")

with nav3:
    st.markdown("👤 Ahmed")

st.markdown("---")

# ------------------ MAIN TITLE ------------------
st.title("Class Performance Statistics")

# ------------------ FILTERS ------------------
f1, f2, f3 = st.columns([2, 1, 1])

with f1:
    st.date_input(
        "📅 Date Range",
        (date(2024, 4, 1), date(2024, 4, 30))
    )

with f2:
    st.button("🔍 Filters")

with f3:
    st.button("⬇️ Export Data")

st.markdown("---")

# ------------------ KPIs ------------------
k1, k2, k3, k4 = st.columns(4)

k1.metric("Average Grade", "88.5%", "▲ 2.3% from last period")
k2.metric("Minimum Grade", "62%", "▲ 1.5% from last period")
k3.metric("Maximum Grade", "98%", "▼ 0.5% from last period")
k4.metric("Pass Rate", "92.5%", "▲ 0.8% from last period")

st.markdown("---")

# ------------------ DATA ------------------
grade_data = pd.DataFrame({
    "Grade": ["A", "B", "C", "D", "F"],
    "Students": [15, 20, 10, 3, 2]
})

performance_data = pd.DataFrame({
    "Assessment": ["Assign 1", "Assign 2", "Midterm", "Final Exam"],
    "Average Score": [85, 88, 82, 87]
})

# ------------------ CHARTS ------------------
c1, c2 = st.columns(2)

with c1:
    st.subheader("Grade Distribution")
    st.caption("Overview of student grades across the class.")
    fig1 = px.bar(
        grade_data,
        x="Grade",
        y="Students",
        text="Students",
        color="Grade",
        color_discrete_sequence=["#fb7185", "#2dd4bf", "#94a3b8", "#fde047", "#ef4444"]
    )
    fig1.update_layout(
        plot_bgcolor="#020617",
        paper_bgcolor="#020617",
        font_color="#e5e7eb",
        showlegend=False
    )
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    st.subheader("Class Performance Over Time")
    st.caption("Average scores across recent assignments and exams.")
    fig2 = px.line(
        performance_data,
        x="Assessment",
        y="Average Score",
        markers=True,
        line_shape="spline",
        color_discrete_sequence=["#38bdf8"]
    )
    fig2.update_layout(
        plot_bgcolor="#020617",
        paper_bgcolor="#020617",
        font_color="#e5e7eb"
    )
    fig2.update_yaxes(range=[80, 92])
    st.plotly_chart(fig2, use_container_width=True)

# ------------------ FOOTER ------------------
st.markdown(
    "<div class='footer'>© 2025 Student Predictor. All rights reserved.</div>",
    unsafe_allow_html=True
)

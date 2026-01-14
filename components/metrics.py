import streamlit as st

def render_metrics(stats: dict):
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
         "Total Active Students",
        stats["total_students"]
    )

    col2.metric(
        "Students at Risk",
        stats["at_risk"]
    )

    col3.metric(
        "Average Predicted Score",
        stats["avg_score"]
    )

    col4.metric(
        "Highest Predicted Score",
        stats["highest_score"]
    )

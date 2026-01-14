import streamlit as st

def render_students_table(df):
    st.subheader("Student Roster")
    st.dataframe(df, use_container_width=True)

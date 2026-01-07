
import streamlit as st
def main():
    st.set_page_config(
        page_title="Student Performance Predictor",
        layout="wide",
        page_icon="🎓",
        initial_sidebar_state="collapsed"
    )
    
    
    st.switch_page("pages/student_performance_app.py")

if __name__ == "__main__":
    main()
# prediction_page.py
import streamlit as st
from components.grade_prediction_card import render_grade_prediction_card
from components.recommendations_card import render_recommendations_card
from components.footer import render_footer as render_exact_footer_from_image
from components.logout import render_logout_button
# Load Bootstrap and Custom CSS
def load_bootstrap():
    with open("styles/bootstrap.html", "r") as f:
        bootstrap_html = f.read()
    st.markdown(bootstrap_html, unsafe_allow_html=True)

def load_css():
    with open("styles/custom.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def render_prediction_page():
    load_css()
    load_bootstrap()
    
    # Ensure that prediction exists
    if "predicted_grade" not in st.session_state:
       st.warning("Please predict your grade first")
       st.stop() 
    grade=st.session_state.get("predicted_grade", 0)
    render_grade_prediction_card(grade=grade, show_buttons=True)
    inputs = st.session_state.get("inputs", {})
    # Render Recommendations Card
    render_recommendations_card(inputs)
    render_logout_button()
    render_exact_footer_from_image()
if __name__ == "__main__":
    st.set_page_config(
        page_title="Grade Prediction",
        layout="wide",
        page_icon="📊"
    )
    render_prediction_page()
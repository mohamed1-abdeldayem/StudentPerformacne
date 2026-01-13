from datetime import datetime
import streamlit as st
import sys
import os
import requests
from supabase import create_client, Client
from components.header import render_header
from components.input_form import render_input_form
from components.footer import render_footer
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

API_URL = "http://127.0.0.1:5000/predict"

st.set_page_config(
    page_title="Student Performance Predictor",
    layout="wide",
    page_icon="🎓"
)
@st.cache_resource
def init_supabase() -> Client:
        """Initialize Supabase client"""
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_ANON_KEY"]
        return create_client(url, key)

supabase = init_supabase()
if "user_id" not in st.session_state or "token" not in st.session_state:
    st.error("You must login first")
    st.switch_page("pages/Login.py")
    st.stop()

if st.session_state.role != "student":
    st.error("You are not authorized to access this page")
    st.switch_page("pages/Login.py")
    st.stop()    
    
def load_bootstrap():
    with open("styles/bootstrap.html", "r") as f:
        bootstrap_html = f.read()
    st.markdown(bootstrap_html, unsafe_allow_html=True)

def load_css():
    with open("styles/custom.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
def render_student_performance():

    load_bootstrap()
    load_css()
    render_header()

    inputs = render_input_form()
    student_id = st.session_state.user_id

    data_to_insert = {
    "stud_uuid": student_id,
    "hours_studied": inputs["Hours_Studied"],
    "attendance": inputs["Attendance"],
    "parental_involvement": inputs["Parental_Involvement"],
    "access_to_resources": inputs["Access_to_Resources"],
    "previous_scores": inputs["Previous_Scores"],
    "motivation_level": inputs["Motivation_Level"],
    "internet_access": inputs["Internet_Access"],
    "tutoring_sessions": inputs["Tutoring_Sessions"],
    "family_income": inputs["Family_Income"],
    "teacher_quality": inputs["Teacher_Quality"],
    "peer_influence": inputs["Peer_Influence"],
    "learning_disabilities": inputs["Learning_Disabilities"],
    "parental_education_level": inputs["Parental_Education_Level"],
    "distance_from_home": inputs["Distance_from_Home"],
    "extracurricular_activities": inputs["Extracurricular_Activities"],
    }


    st.markdown("---")
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("Predict My Grade", use_container_width=True):
            try:
                
                response = requests.post(API_URL, json=inputs)
                if response.status_code == 200:
                    result = response.json()
                    st.session_state["predicted_grade"] = result["predicted_score"]
                    st.session_state["inputs"] = inputs
                    data_to_insert["stud_score"] = result["predicted_score"]
                    supabase.table("student_features").upsert(data_to_insert,on_conflict="stud_uuid").execute()
                    st.switch_page("pages/prediction_page_app.py")
                else:
                    st.error("Prediction API failed")
            except requests.exceptions.RequestException:
                st.error("Could not connect to Prediction API")

    render_footer()

if __name__ == "__main__":
    render_student_performance()

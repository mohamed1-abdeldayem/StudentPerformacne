import pandas as pd
import streamlit as st
from components.metrics import render_metrics
from components.charts import render_grade_distribution
from components.tablesOfStudents import render_students_table
from components.footer import render_footer
from supabase import create_client, Client

# set page config
st.set_page_config(page_title="Instructor Dashboard", layout="wide")

# check if user is logged in
if "role" not in st.session_state:
    st.error("Please login first")
    st.stop()
# Check if user is instructor
if st.session_state["role"] != "instructor":
    st.error("Access Denied: Instructor only")
    st.stop()

# Initialize Supabase client
@st.cache_resource
def init_supabase() -> Client:
        """Initialize Supabase client"""
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_ANON_KEY"]
        return create_client(url, key)
# function to load css file 
def load_css():
    with open("styles/dashboard/dashboard.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

supabase= init_supabase()
# Function to get students data from Supabase
def get_students_data():
    response = supabase.table("student_account").select(
        """
        stud_uuid,
        full_name,
        email,
        student_features(
            hours_studied,
            attendance,
            previous_scores,
            stud_score
        )
        """
    ).execute()

    return response.data
# Function to map scores to grades
def get_grade(score):
    if score is None: return "F" 
    if score >= 85: return "A"
    elif score >= 75: return "B"
    elif score >= 65: return "C"
    elif score >= 50: return "D"
    else: return "F"
# Function to normalize students data into a DataFrame
def normalize_students_data(raw_data):
    rows = []
    
    for row in raw_data:
        features = row.get("student_features") or {}
        
        rows.append({
            "Student Name": row["full_name"],
            "Study Hours": features.get("hours_studied", 0), 
            "Attendance": features.get("attendance", 0),
            "Previous Score": features.get("previous_scores", 0),
            "Predicted Score": features.get("stud_score", 0),
            "Predicted Grade": get_grade(features.get("stud_score", 0))
        })

    return pd.DataFrame(rows)

# Function to calculate key metrics
def calculate_metrics(df):
    if df.empty:
        return {
            "avg_score": 0,
            "at_risk": 0,
            "total_students": 0,
            "highest_score": 0
        }

    avg_score = round(df["Predicted Score"].mean(), 1)

    at_risk = df[df["Predicted Score"] < 60].shape[0]

    total_students = len(df)

    highest_score = df["Predicted Score"].max()

    return {
        "avg_score": avg_score,
        "at_risk": at_risk,
        "total_students": total_students,
        "highest_score": highest_score
    }

load_css()

st.title("Instructor Dashboard")

# tabs = st.tabs(["All Students", "At Risk", "High Achievers", "New Enrollments"])

raw_data = get_students_data()
df = normalize_students_data(raw_data)
stats=calculate_metrics(df)
render_metrics(stats)

st.markdown("""<br><br>""", unsafe_allow_html=True)

render_students_table(df)
render_grade_distribution(df)
    


render_footer()

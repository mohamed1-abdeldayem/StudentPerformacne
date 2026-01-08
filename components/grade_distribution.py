import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def get_grade(score):
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"




def grade_distribution():
  # Simulated data
    np.random.seed(42)
    num_students = 100
    df = pd.DataFrame({
        "student_id": range(1, num_students + 1),
        "gender": np.random.choice(["Male", "Female"], num_students),
        "study_time": np.random.choice(["Low", "Medium", "High"], num_students),
        "absences": np.random.randint(0, 15, num_students),
        "prediction": np.random.randint(30, 100, num_students)
    })
    df["grade"] = df["prediction"].apply(get_grade)
    grade_counts = df["grade"].value_counts().sort_index()  # A, B, C, F
    grade_counts = grade_counts.reset_index()
    grade_counts.columns = ["Grade", "Count"]

    fig_grade = px.bar(
      grade_counts,
      x="Grade",
      y="Count",
      title="Grade Distribution",
      color="Grade",
      color_discrete_map={"A":"green", "B":"blue", "C":"orange", "F":"red"},
      text="Count"
    )

    st.plotly_chart(fig_grade)
    

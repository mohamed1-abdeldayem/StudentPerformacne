import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def score_distribution():
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
  #  Create histogram for score predictions 
    fig = px.histogram(
        df,
        x="prediction",
        nbins=8,
        title="Distribution of Student Prediction Scores",
        color_discrete_sequence=["#636EFA"]
    )
    fig.update_traces(
        marker=dict(
        line=dict(width=2, color="white")  
    )
)

    st.plotly_chart(fig, use_container_width=True)
    
    
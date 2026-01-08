import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
def performance_chart():
    np.random.seed(42)
    num_students = 100
    df = pd.DataFrame({
        "student_id": range(1, num_students + 1),
        "gender": np.random.choice(["Male", "Female"], num_students),
        "study_time": np.random.choice(["Low", "Medium", "High"], num_students),
        "absences": np.random.randint(0, 15, num_students),
        "prediction": np.random.randint(30, 100, num_students)
    })
    df["status"] = df["prediction"].apply(lambda x: "Pass" if x >= 50 else "Fail")
    colors = {
    "Pass": "green",
    "Fail": "red"
    }
    fig = px.pie(
        df,
        names="status",
        title="Pass vs Fail Ratio",
        color="status",  # ضروري علشان يأخذ الألوان من القاموس
        color_discrete_map=colors
    )
    st.plotly_chart(fig)
    
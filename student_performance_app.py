# app.py
import streamlit as st
import requests
from components.header import render_header
from components.input_form import render_input_form
from components.footer import render_footer

API_URL = "http://127.0.0.1:5000/predict"

st.set_page_config(
    page_title="Student Performance Predictor",
    layout="wide",
    page_icon="🎓"
)

def load_bootstrap():
    with open("styles/bootstrap.html", "r") as f:
        bootstrap_html = f.read()
    st.markdown(bootstrap_html, unsafe_allow_html=True)

def load_css():
    with open("styles/custom.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():

    load_bootstrap()
    load_css()
    render_header()

    inputs = render_input_form()

    st.markdown("---")
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

    with col_btn2:
        if st.button("Predict My Grade", use_container_width=True):
            try:
                # st.info(f" Sending data: {inputs}")
                response = requests.post(API_URL, json=inputs)
                # st.info(f" Response status: {response.status_code}")
                if response.status_code == 200:
                    result = response.json()
                    # st.info(f"Response data: {result}")
                    st.session_state["predicted_grade"] = result["predicted_score"]
                    st.session_state["inputs"] = inputs
                else:
                    st.error("Prediction API failed")

            except requests.exceptions.RequestException:
                st.error("Could not connect to Prediction API")

    if "predicted_grade" in st.session_state:
        st.markdown(f"""
        <div class="card shadow border-0 mt-4 text-center">
            <div class="card-header bg-primary text-white">
                <h4>Predicted Grade</h4>
            </div>
            <div class="card-body">
                <h1 class="display-3 text-primary">
                    {st.session_state["predicted_grade"]}
                </h1>
            </div>
        </div>
        """, unsafe_allow_html=True)

    render_footer()

if __name__ == "__main__":
    main()

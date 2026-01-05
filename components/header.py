
import streamlit as st

def render_header():
    st.markdown(""" 
                
    <div class="header p-2  mb-4 bg-primary text-white rounded-3">
        <div> 
            <div class="row align-items-center">
                <div class="col-md-10">
                    <h3 class="mb-0"><i class="bi bi-mortarboard-fill"></i> Student Performance Predictor</h3>
                    <p class="lead mb-0">Input your academic details below to get a personalized predicted grade and receive actionable recommendations to improve your performance.!</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
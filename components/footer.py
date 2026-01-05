# components/footer.py
import streamlit as st
from datetime import datetime

def render_footer():
    current_year = datetime.now().year
    
    st.markdown(f"""
    
        <div class="container position-relative bottom-0 w-100">
            <div class="row justify-content-center">
                <div class="col-12 m-auto text-center">
                    <p class="mb-0" style="
                        font-size: 14px;
                        color: #666;
                        margin: 0;
                        padding: 10px 0;">
                        © {current_year} Student Predictor. All rights reserved.
                    </p>
                </div>
            </div>
        </div>
            
    """, unsafe_allow_html=True)



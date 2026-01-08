import streamlit as st

def stat_card(title, value, positive=True):
  
    st.markdown(f"""
    <div class="card shadow-sm border-0 text-center">
      <div class="card-body">
        <h5 class="font-bold mb-1 text-primary">{title}</h5>
        <h3 class="fw-bold">{value}</h3>
      </div>
    </div>
    """, unsafe_allow_html=True)

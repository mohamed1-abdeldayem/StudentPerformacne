import streamlit as st
from pathlib import Path

Page_Ico = Path("../Styles/icons/lucide-GraduationCap-Outlined.svg")

st.set_page_config(
    page_title="Sign Up",
    page_icon=Page_Ico,
    layout="centered",
    initial_sidebar_state="collapsed"
)
def load_css(file_name):
    with open(file_name, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def load_html(file_name):
    with open(file_name, encoding="utf-8") as f:
        st.markdown(f.read(), unsafe_allow_html=True)
# ================= CSS =================
load_css("../Styles/Sign Up/Sign_Up.css")
load_html("../Styles/Sign Up/Sign_Up.html")
# ================= Form =================

with st.form("login_form"):

    Firstname=st.text_input("First Name", placeholder="john doe")
    email = st.text_input("Email", placeholder="john.doe@example.com")
    password = st.text_input("Password", type="password")
    Confirm_Password =st.text_input("Confirm Password", type="password")

    login_btn = st.form_submit_button("Sign Up", use_container_width=True , key="log_btn")




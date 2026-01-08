import streamlit as st
from pathlib import Path

Page_Ico = Path("../Styles/icons/lucide-GraduationCap-Outlined.svg")
st.set_page_config(
    page_title="Login",
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
load_css("../Styles/Login/Login_Block.css")
# ================= Session State =================
if "role" not in st.session_state:
    st.session_state.role = "student"

# ================= Form =================
with st.form("login_form"):
    load_html("../Styles/Login/Login_BLock.html")
    col1, col2 = st.columns(2)

    with col1:
        student_btn = st.form_submit_button(
            "Student",
            use_container_width=True,
            key="student_btn"
        )

    with col2:
        instructor_btn = st.form_submit_button(
            "Instructor",
            use_container_width=True,
            key="inst_btn"
        )

    email = st.text_input("Email", placeholder="john.doe@example.com")
    password = st.text_input("Password", type="password")

    login_btn = st.form_submit_button("Login", use_container_width=True , key="log_btn")
    load_html("../Styles/Login/Login_Sign_Up_Button.html")
# ================= Logic =================
if student_btn:
    st.session_state.role = "student"

if instructor_btn:
    st.session_state.role = "instructor"

# إعادة تلوين الزرار الصح
if st.session_state.role == "student":
    load_css("../Styles/Login/Login_Toggle_1.css")
else:
    load_css("../Styles/Login/Login_Toggle_2.css")
if login_btn:
    st.success(f"Login as {st.session_state.role}")

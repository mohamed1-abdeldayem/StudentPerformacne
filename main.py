import streamlit as st
from pages import Sign_Up, Login  # استدعاء ملفات الصفحات

# تهيئة صفحة افتراضية
if "page" not in st.session_state:
    st.session_state.page = "Sign_Up"  # الصفحة الافتراضية عند فتح التطبيق

# عرض الصفحة حسب session_state
if st.session_state.page == "Sign_Up":
    Sign_Up.sign_up_page()
elif st.session_state.page == "Login":
    Login.login_page()

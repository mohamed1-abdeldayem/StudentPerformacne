import streamlit as st
def render_logout_button():
    st.markdown("""
    <style>
    .logout-btn {
        position: fixed;
        top: 15px;
        right: 25px;
        z-index: 9999;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,1,6])
    with col1:
        if st.button("Logout"):
            st.session_state.clear()
            st.switch_page("pages/Login.py")

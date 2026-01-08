import streamlit as st
from pathlib import Path
from supabase import create_client, Client
import re
from datetime import datetime
import bcrypt
import streamlit.components.v1 as components
import streamlit as st
from streamlit.runtime.scriptrunner import RerunException
from streamlit.runtime.scriptrunner import add_script_run_ctx

def sign_up_page():
    Page_Ico = Path("Styles/icons/lucide-GraduationCap-Outlined.svg")

    st.set_page_config(
        page_title="Sign Up",
        page_icon=Page_Ico,
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    @st.cache_resource
    def init_supabase() -> Client:
        """Initialize Supabase client"""
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_ANON_KEY"]
        return create_client(url, key)

    supabase = init_supabase()

    def validate_email(email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def validate_password(password):
        """Validate password strength"""
        if len(password) < 6:
            return False, "Password must be at least 6 characters"
        return True, ""

    def check_email_exists(email):
        """Check if email already exists in database"""
        try:
            response = supabase.table("student_account").select("email").eq("email", email).execute()
            return len(response.data) > 0
        except Exception as e:
            return False

    def sign_up_user(full_name, email, password):
        """Sign up user and store in student_account table"""
        try:
            # Check if email already exists
            if check_email_exists(email):
                return False, "This email is already registered."
            
            # Hash the password
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            
            # Insert new student account
            new_student = {
                "full_name": full_name.strip(),
                "email": email.strip().lower(),
                "password": hashed_password.decode('utf-8'),
                "created_at": datetime.now().isoformat()
            }
            
            response = supabase.table("student_account").insert(new_student).execute()
            
            if response.data:
                return True, "Account created successfully! You can now login."
            else:
                return False, "Failed to create account. Please try again."
                
        except Exception as e:
            error_msg = str(e)
            return False, f"Error: {error_msg}"

    # ================= CSS HTML =================
    def load_css(file_name):
        with open(file_name, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def load_html(file_name):
        with open(file_name, encoding="utf-8") as f:
            st.markdown(f.read(), unsafe_allow_html=True)

    load_css("Styles/Sign Up/Sign_Up.css")
    load_html("Styles/Sign Up/Sign_Up.html")
    def rerun():
        raise RerunException(get_script_run_ctx())
    with st.container(key="Sign_In"):
        if st.button("Sign In"):
            st.session_state.page = "Login"
            st.rerun() 


    # ================= Form =================

    with st.form("login_form"):

        Firstname=st.text_input("Full Name", placeholder="john doe")
        email = st.text_input("Email", placeholder="john.doe@example.com")
        password = st.text_input("Password", type="password")
        Confirm_Password =st.text_input("Confirm Password", type="password")

        signup_btn = st.form_submit_button("Sign Up", use_container_width=True , key="log_btnsign")

        if signup_btn:
            # Validation
            if not Firstname.strip():
                st.error("Please enter your Full name")
            elif not email.strip():
                st.error("Please enter your email")
            elif not validate_email(email):
                st.error("Please enter a valid email address")
            elif not password:
                st.error("Please enter a password")
            else:
                is_valid, msg = validate_password(password)
                if not is_valid:
                    st.error(msg)
                elif password != Confirm_Password:
                    st.error("Passwords do not match")
                else:
                    # Sign up user
                    with st.spinner("Creating your account..."):
                        success, message = sign_up_user(Firstname, email, password)
                        
                    if success:
                        st.success(message)
                        st.balloons()
                        # st.switch_page("Login.py")
                        # st.info("You can now login with your credentials")
                    else:
                        st.error(message)




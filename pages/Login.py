import streamlit as st
from pathlib import Path
from supabase import create_client, Client
import bcrypt
def login_page():

    Page_Ico = Path("Styles/icons/lucide-GraduationCap-Outlined.svg")
    st.set_page_config(
        page_title="Login",
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

    # Instructor credentials (hardcoded)
    INSTRUCTOR_CREDENTIALS = {
        "instructor@edu.com": "instructor123"}

    # ================= CSS =================
    def load_css(file_name):
        with open(file_name, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def load_html(file_name):
        with open(file_name, encoding="utf-8") as f:
            st.markdown(f.read(), unsafe_allow_html=True)

    load_css("Styles/Login/Login_Block.css")

    # ================= Session State =================
    if "role" not in st.session_state:
        st.session_state.role = "student"
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user_data" not in st.session_state:
        st.session_state.user_data = None

    # ================= Authentication Functions =================
    def authenticate_student(email: str, password: str) -> dict:
        """Authenticate student from Supabase database with bcrypt"""
        try:
            # Get student record by email
            response = supabase.table("student_account")\
                .select("*")\
                .eq("email", email.strip().lower())\
                .execute()
            
            if response.data and len(response.data) > 0:
                student = response.data[0]
                stored_password = student['password']
                
                # Verify password using bcrypt
                if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                    return {"success": True, "data": student}
                else:
                    return {"success": False, "message": "Invalid email or password"}
            else:
                return {"success": False, "message": "Invalid email or password"}
        except Exception as e:
            return {"success": False, "message": f"Database error: {str(e)}"}

    def authenticate_instructor(email: str, password: str) -> dict:
        """Authenticate instructor from hardcoded credentials"""
        if email in INSTRUCTOR_CREDENTIALS and INSTRUCTOR_CREDENTIALS[email] == password:
            return {
                "success": True, 
                "data": {
                    "email": email,
                    "full_name": "Instructor",
                    "role": "instructor"
                }
            }
        else:
            return {"success": False, "message": "Invalid instructor credentials"}

    # ================= Form =================
    with st.form("login_form_login"):
        load_html("Styles/Login/Login_BLock.html")
        
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
        login_btn = st.form_submit_button("Login", use_container_width=True, key="log_btn_login")
        
        load_html("Styles/Login/Login_Sign_Up_Button.html")
        with st.container(key="Sign_Up"):
            if st.form_submit_button("Sign Up"):
                st.switch_page("pages/Sign_Up.py")
        # ================= Logic =================
        # Handle role selection
        if student_btn:
            st.session_state.role = "student"
            st.rerun()

        if instructor_btn:
            st.session_state.role = "instructor"
            st.rerun()

        # Apply correct styling based on role
        if st.session_state.role == "student":
            load_css("Styles/Login/Login_Toggle_1.css")
        else:
            load_css("Styles/Login/Login_Toggle_2.css")

        # Handle login
        if login_btn:
            if not email or not password:
                st.error("Please enter both email and password")
            else:
                with st.spinner("Authenticating..."):
                    if st.session_state.role == "student":
                        try:
                            auth_response = supabase.auth.sign_in_with_password({
                            "email": email,
                            "password": password
                            })
                            if auth_response.user:
                                # Save token and user_id in session_state
                                st.session_state.user_id = auth_response.user.id
                                st.session_state.token = auth_response.session.access_token
                                st.session_state.logged_in = True
                                st.session_state.user_role = "student"

                                # Fetch additional student data
                                user_data = supabase.table("student_account").select("*").eq("stud_uuid", auth_response.user.id).execute()
                                st.session_state.user_data = user_data.data[0] if user_data.data else None
                                
                                st.success(f"Welcome {st.session_state.user_data['full_name']}! 🎓")
                                st.balloons()
                                st.switch_page("pages/student_performance_app.py")
                            else:
                                st.error("Invalid email or password")
                        except Exception as e:
                            st.error(f"Auth error: {str(e)}")                    
                    else:  # instructor
                        # Authenticate instructor from hardcoded credentials
                        result = authenticate_instructor(email, password)
                        if result["success"]:
                            st.session_state.logged_in = True
                            st.session_state.user_data = result["data"]
                            st.session_state.user_role = "instructor"
                            st.balloons()
                            # Redirect to instructor dashboard
                            st.switch_page("pages/InstructorDashboard.py")
                        else:
                            st.error(f"❌ {result['message']}")

if __name__ == "__main__":
    login_page()
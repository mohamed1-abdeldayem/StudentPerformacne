
import streamlit as st

def render_input_form():
    """Render input form that matches API expectations"""
    
    st.markdown("""
    <div class="card border-0">
        <div>
            <h4 class="mb-0 text-black"><i class="bi bi-journal-text"></i> Enter Your Academic Details</h4>
        </div>
        <div class="card-body">
    """, unsafe_allow_html=True)
    
    with st.container():
        
        col1, col2 = st.columns(2)
        with col1:
            hours_studied = st.number_input(
                "Hours Studied",
                min_value=0,
                max_value=15,
                value=6,
                step=1,
                key="hours_studied"
            )
        
        with col2:
            attendance = st.number_input(
                "Attendance percentage (0-100)",
                min_value=0,
                max_value=100,
                value=85,
                step=1,
                key="attendance"
            )
        
        
        col3, col4 = st.columns(2)
        with col3:
            previous_scores = st.number_input(
                "Previous Scores (0-100)",
                min_value=0,
                max_value=100,
                value=78,
                step=1,
                key="previous_scores"
            )
        
        with col4:
            tutoring_sessions = st.number_input(
                "Number of Tutoring Sessions",
                min_value=0,
                max_value=8,
                value=2,
                step=1,
                key="tutoring_sessions"
            )
        
        
        col5, col6 = st.columns(2)
        with col5:
            extracurricular_activities = st.radio(
                "Participation in extracurricular activities",
                ["Yes", "No"],
                horizontal=True,
                index=0,  # Default to "Yes"
                key="extracurricular"
            )
        
        with col6:
            learning_disabilities = st.radio(
                "Presence of learning disabilities",
                ["Yes", "No"],
                horizontal=True,
                index=1,  # Default to "No"
                key="learning_disabilities"
            )
        
        
        col7, col8 = st.columns(2)
        with col7:
            parental_involvement = st.selectbox(
                "Level of parental involvement",
                ["Low", "Medium", "High"],
                index=1,  # Default to "Medium"
                key="parental_involvement"
            )
        
        with col8:
            access_to_resources = st.selectbox(
                "Student's access to educational resources",
                ["Low", "Medium", "High"],
                index=2,  # Default to "High"
                key="access_to_resources"
            )
        
        
        col9, col10 = st.columns(2)
        with col9:
            family_income = st.selectbox(
                "Family income level",
                ["Low", "Medium", "High"],
                index=1,  # Default to "Medium"
                key="family_income"
            )
        
        with col10:
            teacher_quality = st.selectbox(
                "Quality of teaching received",
                ["Low", "Medium", "High"],
                index=2,  # Default to "High"
                key="teacher_quality"
            )
        
        
        col11, col12 = st.columns(2)
        with col11:
            peer_influence = st.selectbox(
                "Type of peer influence",
                ["Positive", "Neutral", "Negative"],
                index=0,  
                key="peer_influence"
            )
        
        with col12:
            
            parental_education_level = st.selectbox(
                "Education level of parents",
                ["High School", "College", "Postgraduate"],
                index=1,  # Default to "College"
                key="parental_education"
            )
        
        
        col13, col14 = st.columns(2)
        with col13:
            distance_from_home = st.selectbox(
                "Distance from home to school",
                ["Near", "Moderate", "Far"],
                index=2,  # Default to "Far"
                key="distance_from_home"
            )
        
        with col14:
            internet_access = st.radio(
                "Internet Access at Home",
                ["Yes", "No"],
                horizontal=True,
                index=0,  
                key="internet_access"
            )
        
        
        motivation_level = st.selectbox(
            "Student Motivation Level",
            ["Low", "Medium", "High"],
            index=2,  
            key="motivation_level"
        )
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    
    return {
        "Hours_Studied": int(hours_studied),
        "Attendance": int(attendance),
        "Parental_Involvement": parental_involvement,
        "Access_to_Resources": access_to_resources,
        "Extracurricular_Activities": extracurricular_activities,
        "Previous_Scores": int(previous_scores),
        "Motivation_Level": motivation_level,
        "Internet_Access": internet_access,
        "Tutoring_Sessions": int(tutoring_sessions),
        "Family_Income": family_income,
        "Teacher_Quality": teacher_quality,
        "Peer_Influence": peer_influence,
        "Learning_Disabilities": learning_disabilities,
        "Parental_Education_Level": parental_education_level,
        "Distance_from_Home": distance_from_home
    }
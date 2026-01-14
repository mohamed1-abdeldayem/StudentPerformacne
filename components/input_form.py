
import streamlit as st

def render_input_form():
    saved_inputs = st.session_state.get("inputs", {})
    edit_mode = st.session_state.get("edit_mode", False)
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
                "Hours Studied per week",
                min_value=0,
                max_value=100,
                value=saved_inputs.get("Hours_Studied", 0) if edit_mode else 0,
                step=1,
                key="hours_studied"
                
            )
        
        with col2:
            attendance = st.number_input(
                "Attendance percentage (0-100)",
                min_value=0,
                max_value=100,
                value=saved_inputs.get("Attendance", 0) if edit_mode else 0,
                step=1,
                key="attendance"
            )
        
        
        col3, col4 = st.columns(2)
        with col3:
            previous_scores = st.number_input(
                "Previous Scores (0-100)",
                min_value=0,
                max_value=100,
                value=saved_inputs.get("Previous_Scores", 0) if edit_mode else 0,
                step=1,
                key="previous_scores"
            )
        
        with col4:
            tutoring_sessions = st.number_input(
                "Number of Tutoring Sessions",
                min_value=0,
                max_value=8,
                value=saved_inputs.get("Tutoring_Sessions", 0) if edit_mode else 0,
                step=1,
                key="tutoring_sessions"
            )
        
        
        col5, col6 = st.columns(2)
        
        with col5:
            index_value = 0  # default
            if edit_mode:
               if saved_inputs.get("Peer_Influence", "Positive") == "Neutral":
                  index_value = 1
               elif saved_inputs.get("Peer_Influence", "Positive") == "Negative":
                  index_value = 2
               else:
                 index_value = 0
            peer_influence = st.selectbox(
                "Type of peer influence",
                ["Positive", "Neutral", "Negative"],
                index=index_value,  
                key="peer_influence"
            )
            
        with col6:
            index_value = 0  
            if edit_mode:
               if saved_inputs.get("Learning_Disabilities", "Yes") == "Yes":
                  index_value = 0
               else:
                 index_value = 1    
                 
            learning_disabilities = st.radio(
                "Presence of learning disabilities",
                ["Yes", "No"],
                horizontal=True,
                index=index_value,
                key="learning_disabilities"
            )
        
        
        col7, col8 = st.columns(2)
        with col7:
            index_value = 1  # default
            if edit_mode:
               if saved_inputs.get("Parental_Involvement", "Medium") == "Low":
                  index_value = 0
               elif saved_inputs.get("Parental_Involvement", "Medium") == "High":
                  index_value = 2
               else:
                 index_value = 1
            parental_involvement = st.selectbox(
                "Level of parental involvement",
                ["Low", "Medium", "High"],
                index=index_value,  
                key="parental_involvement"
            )
        
        with col8:
            index_value = 2  # default
            if edit_mode:
               if saved_inputs.get("Access_to_Resources", "High") == "Low":
                  index_value = 0
               elif saved_inputs.get("Access_to_Resources", "High") == "Medium":
                  index_value = 1
               else:
                 index_value = 2
            access_to_resources = st.selectbox(
                "Student's access to educational resources",
                ["Low", "Medium", "High"],
                index=index_value,  
                key="access_to_resources"
            )


        col9, col10 = st.columns(2)
        with col9:
            index_value = 1  # default
            if edit_mode:
               if saved_inputs.get("Family_Income", "Medium") == "Low":
                  index_value = 0
               elif saved_inputs.get("Family_Income", "Medium") == "High":
                  index_value = 2
               else:
                 index_value = 1
            family_income = st.selectbox(
                "Family income level",
                ["Low", "Medium", "High"],
                index=index_value,  
                key="family_income"
            )
        with col10:
            index_value = 1  # default
            if edit_mode:
               if saved_inputs.get("Motivation_Level", "Medium") == "Low":
                  index_value = 0
               elif saved_inputs.get("Motivation_Level", "Medium") == "High":
                  index_value = 2
               else:
                 index_value = 1
            motivation_level = st.selectbox(
                "Student's motivation level",
                ["Low", "Medium", "High"],
                index=index_value,  
                key="Motivation_Level"
            )
            
            
            
        col11, col12 = st.columns(2)
        with col11:
            index_value = 0  # default
            if edit_mode:
               if saved_inputs.get("Internet_Access", "Yes") == "Yes":
                  index_value = 0
               else:
                 index_value = 1    
            internet_access = st.radio(
                "Internet access at home",
                ["Yes", "No"],
                horizontal=True,
                index=index_value,
                key="internet_access"
            )
        with col12:
            index_value = 1  # default
            if edit_mode:
               if saved_inputs.get("Distance_From_Home", "Near") == "Near":
                  index_value = 0
               elif saved_inputs.get("Distance_From_Home", "Far") == "Far":
                  index_value = 2
               else:
                 index_value = 1
            distance_from_home = st.selectbox(
                "Distance from home to school",
                ["Near","Moderate", "Far"],
                index=index_value,  
                key="distance_from_home"
            )
        
        
        
        
        
        col13, col14 = st.columns(2)
        with col13:
            index_value = 1  # default
            if edit_mode:
               if saved_inputs.get("Teacher_Quality", "Medium") == "Low":
                  index_value = 0
               elif saved_inputs.get("Teacher_Quality", "Medium") == "High":
                  index_value = 2
               else:
                 index_value = 1
            teacher_quality = st.selectbox(
                "Quality of teaching received",
                ["Low", "Medium", "High"],
                index=index_value,  
                key="teacher_quality"
            )
        with col14:
            index_value = 0  # default
            if edit_mode:
               if saved_inputs.get("Extracurricular_Activities", "Yes") == "Yes":
                  index_value = 0
               else:
                 index_value = 1    
            extracurricular_activities = st.radio(
                "Participation in extracurricular activities",
                ["Yes", "No"],
                horizontal=True,
                index=index_value,
                key="extracurricular_activities"
            )    
            
        
        
        
        
        col15 = st.columns(1)
        with col15[0]:
            
            index_value = 1  # default
            if edit_mode:
               if saved_inputs.get("Parental_Education_Level", "High School") == "High School":
                  index_value = 0
               elif saved_inputs.get("Parental_Education_Level", "College") == "College":
                  index_value = 1
               else:
                 index_value = 2
            parental_education_level = st.selectbox(
                "Parental education level",
                ["High School", "College", "Postgraduate"],
                index=index_value,  
                key="parental_education_level"
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
        "Distance_from_Home": distance_from_home,
        
    }
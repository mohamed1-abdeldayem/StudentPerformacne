
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
            st.empty()      
        
      
            
        
        
        
        
      
            
        
        
      
       
            
        
        
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    
    return {
        "Hours_Studied": int(hours_studied),
        "Attendance": int(attendance),
        "Parental_Involvement": parental_involvement,
        "Access_to_Resources": access_to_resources,
        "Previous_Scores": int(previous_scores),
        "Tutoring_Sessions": int(tutoring_sessions),
        "Family_Income": family_income,
        "Peer_Influence": peer_influence,
        "Learning_Disabilities": learning_disabilities,
        
    }
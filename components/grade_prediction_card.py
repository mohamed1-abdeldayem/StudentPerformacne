import streamlit as st
def render_grade_prediction_card(grade=90, show_buttons=True):
    radius = 60
    circumference = 2 * 3.1416 * radius
    dashoffset = circumference * (1 - grade / 100)

    
    grade_letter = ""
    if grade >= 90:
        grade_letter = "A+"
    elif grade >= 85:
        grade_letter = "A"    
    elif grade >= 80:
        grade_letter = "A-"
    elif grade >= 75:
        grade_letter = "B+"    
    elif grade >= 70:
        grade_letter = "B"
    elif grade >= 65:
        grade_letter = "C+"    
    elif grade >= 60:
        grade_letter = "C"
    else:
        grade_letter = "F"

    
    st.markdown(f"""
    <div class="card main-card p-4 p-md-5 mb-4">
      <div class="row align-items-center g-4">
        <div class="col-12 col-md-auto text-center">
          <div class="progress-circle mx-auto">
            <svg width="140" height="140" viewBox="0 0 140 140">
              <circle class="circle-bg" cx="70" cy="70" r="60"></circle>
              <circle class="circle-progress" cx="70" cy="70" r="60"
                      stroke-dasharray="{circumference}"
                      stroke-dashoffset="{dashoffset}"></circle>
            </svg>
            <div class="progress-text">
              <div class="percentage">{grade}%</div>
              <div class="label">Score</div>
            </div>
          </div>
        </div>
        <div class="col-12 col-md text-center text-md-start">
          <h1 class="grade-title fs-2 fs-md-1 mb-2 text-primary">
            Predicted Grade: <span class="grade-value text-primary">{grade_letter}</span>
          </h1>
          <p class="text-muted mb-4">
            This prediction is based on the information you provided and historical data patterns.
          </p>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    if show_buttons:
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Edit Inputs", use_container_width=True, key="edit_inputs"):
                st.session_state["edit_mode"] = True
                st.switch_page("pages/student_performance_app.py")
        with col2:
            if st.button("Re-Predict", use_container_width=True, key="re_predict"):
                st.session_state.pop("inputs", None)
                st.session_state.pop("predicted_grade", None)
                st.switch_page("pages/student_performance_app.py")

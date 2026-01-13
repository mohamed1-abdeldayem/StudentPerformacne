import streamlit as st

recommendations = [
    {
        "title": "Increase Study Hours",
        "desc": "Try to dedicate more hours to focused studying to strengthen understanding of key concepts.",
        "icon": "bi-book",
        "color": "blue",
        "condition": lambda data: data['Hours_Studied'] < 10
    },
    {
        "title": "Improve Attendance",
        "desc": "Regular attendance helps you stay on track with lessons and understand the material better.",
        "icon": "bi-person-check",
        "color": "yellow",
        "condition": lambda data: data['Attendance'] < 75
    },
    {
        "title": "Engage Parents",
        "desc": "Parental involvement can support your learning. Share progress and ask for guidance when needed.",
        "icon": "bi-people",
        "color": "green",
        "condition": lambda data: data['Parental_Involvement'] == "Low"
    },
    {
        "title": "Use Learning Resources",
        "desc": "Make use of available textbooks, videos, and online materials to enhance understanding.",
        "icon": "bi-globe",
        "color": "red",
        "condition": lambda data: data['Access_to_Resources'] == "Low"
    },
    {
        "title": "Participate in Activities",
        "desc": "Extracurricular activities improve teamwork, creativity, and time management skills.",
        "icon": "bi-star",
        "color": "purple",
        "condition": lambda data: data['Extracurricular_Activities'] == "No"
    },
    {
        "title": "Review Past Scores",
        "desc": "Analyze previous scores to identify strengths and areas that need improvement.",
        "icon": "bi-bar-chart",
        "color": "teal",
        "condition": lambda data: data['Previous_Scores'] < 60
    },
    {
        "title": "Increase Motivation",
        "desc": "Set goals and track progress to stay motivated and committed to your studies.",
        "icon": "bi-lightning",
        "color": "orange",
        "condition": lambda data: data['Motivation_Level'] == "Low"
    },
    {
        "title": "Improve Internet Access",
        "desc": "Reliable internet access allows you to use online learning platforms effectively.",
        "icon": "bi-wifi",
        "color": "cyan",
        "condition": lambda data: data['Internet_Access'] == "No"
    },
    {
        "title": "Attend Tutoring Sessions",
        "desc": "Extra tutoring can help clarify difficult concepts and boost understanding.",
        "icon": "bi-person-lines-fill",
        "color": "pink",
        "condition": lambda data: data['Tutoring_Sessions'] < 2
    },
    {
        "title": "Consider Family Support",
        "desc": "Family income and support can affect learning. Seek guidance on affordable resources if needed.",
        "icon": "bi-house",
        "color": "brown",
        "condition": lambda data: data['Family_Income'] == "Low"
    },
    
    {
        "title": "Address Learning Disabilities",
        "desc": "Identify and work on any learning difficulties with specialists for better performance.",
        "icon": "bi-heart-pulse",
        "color": "gray",
        "condition": lambda data: data['Learning_Disabilities'] == True
    },

    {
        "title": "Reduce Travel Fatigue",
        "desc": "Long distance from home can affect concentration. Plan study schedule accordingly.",
        "icon": "bi-car-front",
        "color": "silver",
        "condition": lambda data: data['Distance_from_Home'] == "Far"
    },
]

def render_recommendations_card(data):
    st.markdown('<h3 class="fw-bold mb-4">Recommendations</h3>', unsafe_allow_html=True)
    
    st.markdown("""
        <style>
        .simple-card {
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 15px;
            background: white;
            min-height: 150px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    filtered_recs = []
    for rec in recommendations:
        if rec["condition"](data):
            filtered_recs.append(rec)
            if len(filtered_recs) >= 4:
                break
            
    for i in range(0, len(filtered_recs), 2):
        cols = st.columns(2)
        
        
        if i < len(filtered_recs):
            rec = filtered_recs[i]
            with cols[0]:
                st.markdown(f"""
                    <div class="simple-card">
                        <div class="d-flex gap-3">
                            <div style="color: {rec['color']};">
                                <i class="bi {rec['icon']} fs-3"></i>
                            </div>
                            <div>
                                <h5>{rec['title']}</h5>
                                <p>{rec['desc']}</p>
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
        
        
        if i + 1 < len(filtered_recs):
            rec = filtered_recs[i + 1]
            with cols[1]:
                st.markdown(f"""
                    <div class="simple-card">
                        <div class="d-flex gap-3">
                            <div style="color: {rec['color']};">
                                <i class="bi {rec['icon']} fs-3"></i>
                            </div>
                            <div>
                                <h5>{rec['title']}</h5>
                                <p>{rec['desc']}</p>
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
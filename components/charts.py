import streamlit as st
import plotly.express as px
import pandas as pd
def render_grade_distribution(df):
    col1, col2 = st.columns([1, 1])

    with col1:
        st.caption("Grade Distribution")
        
        if "Predicted Grade" in df.columns:
            grade_counts = df["Predicted Grade"].value_counts().reset_index()
            grade_counts.columns = ["Grade", "Count"]
            
            
            color_map = {"A": "#2ecc71", "B": "#3498db", "C": "#f1c40f", "D": "#e67e22", "F": "#e74c3c"}
            
            fig = px.pie(
                grade_counts,
                names="Grade",
                values="Count",
                hole=0.45,
                color="Grade",
                color_discrete_map=color_map
            )
            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font_color="white"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Column 'Predicted Grade' not found.")

    with col2:
        st.caption("Avg Score by Attendance Range")
        
        if "Attendance" in df.columns and "Predicted Score" in df.columns:
            
            
            bins = [0, 20, 40, 60, 80, 100]
            labels = ['0-20%', '20-40%', '40-60%', '60-80%', '80-100%']
            
            
            df_chart = df.copy()
            df_chart['Range'] = pd.cut(df_chart['Attendance'], bins=bins, labels=labels)
            
            avg_scores = df_chart.groupby('Range', observed=False)['Predicted Score'].mean().reset_index()
            
            
            fig_bar = px.bar(
                avg_scores,
                x="Range",
                y="Predicted Score",
                text_auto='.1f', 
                color="Predicted Score", 
                color_continuous_scale="Blues", 
                labels={"Range": "Attendance Range", "Predicted Score": "Avg Score"}
            )
            
            fig_bar.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font_color="white",
                yaxis=dict(range=[0, 100]), 
                coloraxis_showscale=False 
            )
            
            st.plotly_chart(fig_bar, use_container_width=True)

        else:
            st.error("Missing Data")
            
    col3, col4 = st.columns(2)

   
    with col3:
        st.caption("Progress Tracking (First 10 Students)")
        
        
        sample_df = df.head(10) 
        
        if "Previous Score" in df.columns and "Predicted Score" in df.columns:
            
            comparison_df = sample_df.melt(
                id_vars=["Student Name"], 
                value_vars=["Previous Score", "Predicted Score"],
                var_name="Score Type", 
                value_name="Score"
            )
            
            fig_compare = px.bar(
                comparison_df,
                x="Student Name",
                y="Score",
                color="Score Type", 
                barmode="group",    
                color_discrete_map={"Previous Score": "#95a5a6", "Predicted Score": "#3498db"},
                height=400
            )
            
            fig_compare.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font_color="white",
                xaxis_title="",
                legend_title="",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig_compare, use_container_width=True)

    
    with col4:
        st.caption("Predicted Score Distribution")
        fig = px.histogram(
            df, 
            x="Predicted Score",
            nbins=20, 
            color_discrete_sequence=['#3498db'], 
            opacity=0.8, 
            labels={"Predicted Score": "Score Range"}
        )
        
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="white",
            xaxis_title="Score (0-100)",
            yaxis_title="Number of Students",
            bargap=0.1, 
            xaxis=dict(range=[0, 105]) 
        )

        st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import os

import datetime
import re

# Optimizing UI & Visual Theme
st.set_page_config(
    page_title = "Admission Helper | 2027 Admissions",
   # page_icon="🎓",
    layout = "centered"
)


# Save user input in session state
if "student_average" not in st.session_state:
    st.session_state.student_average = 0.0
if "course_summary_string" not in st.session_state:
    st.session_state.course_summary_string = "No courses evaluated yet."
if "course_grades" not in st.session_state:
    st.session_state.course_grades = {}
if "student_profile" not in st.session_state:
    st.session_state.student_profile = {
        "target_program": None,
        "target_stream": None,
        "average":0,
        "marks": {}
    }
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"role": "helper", "greeting": "Hello! Ask me anything about Ontario university prerequisite rules, OUAC deadlines, or competitive program averages."}
    ]

# ==========================================
#  STUDENT NAVIGATION
# ==========================================
with st.sidebar:
    st.image("data/images/school.jpeg", width=180)
    st.title("Admission Helper")
    st.caption(
        "Your guide to Ontario university admissions. "
        "Explore admission requirements, calculate your Top 6 average, "
        "track important deadlines, and prepare for supplemental applications." \
        "This project is an independent educational initiative and is not affiliated with OUAC"
        "or any Ontario university. Information is provided for demonstration purposes only."
    )
    st.divider()

    selected_page = st.selectbox(
        label = "Navigation Hotbar",
        options=[
            "Admission Helper",
            "Top 6 Average Course Calc",
            "Course Prerequisite Checker",
            "Deadlines & Resources",
            "Application Cost Planner"
        ]
    )
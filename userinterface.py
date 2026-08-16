
from asyncio import streams
import streamlit as st
import os
import pandas as pan
import datetime
import re
from program_database import ouac_deadlines, streams

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

def page_header(text, color = "red", size = 25):
    st.markdown(
        f"<h1 style = 'color: {color}; font-size: {size}px;'>{text}</h1>",
        unsafe_allow_html = True
    )

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

    st.divider()

    st.subheader(" Your Marks Profile ")
    if (
        "student_average" in st.session_state
        and "course_grade_matrix" in st.session_state
        and len(st.session_state.course_grade_matrix) > 0
    ):
        st.metric(
            label="Marks Summary (Top 6 Average)",
            value=f"{st.session_state.student_profile["average"]:.1f}%"
        )

       # Stored marks successfully to profile

    else:
        st.info(
            "Enter your courses and marks in the "
            "'Calculate My Top 6 Average' section to get started."
        )


    # DEADLINES & RESOURCES PAGE
if selected_page == "Deadlines & Resources":
   
    tab1, tab2 = st.tabs(
        [
            "Admission Deadlines",
            "Resources & Portals"
        ]
    )
    with tab1:
        
        st.write("Important Ontario university application deadlines.")
        df = pan.DataFrame(ouac_deadlines)
        st.dataframe(df, use_container_width = True, hide_index = True)

    with tab2: 
        st.write("Important Ontario Admission Portals")


# USER PROFILE

elif selected_page == "Course Prerequisite Checker":
    st.header("Course Prerequisite Checker")

    st.divider()

    page_header("Select Target Program", color = "red", size = 21)
# TOP 6 AVERAGE CALCULATOR PAGE

elif selected_page == "Top 6 Average Course Calc":

    # Header
    st.header("Top 6 Average Calculator")
    page_header("Calculate Top 6 courses average for Ontario university admissions", color = "red", size = 17)

    # Display different program streams for user to pick
    stream = st.selectbox(" Select your target program stream & enter your courses grades below", list(streams.keys()))

    st.divider()

    # store student stream and course info to profile
    st.session_state.student_profile["chosen_stream"] = stream
    st.divider()
    required_courses = streams[stream]["required"]
    
    # Location to store user input
    selected_courses = []
    student_grades = []
    course_grades = {}

    st.divider()

    # Required courses and marks display
    page_header("Required Courses", color = "green", size = 21)

# CHAT ASSISTANT PAGE

elif selected_page == "Admission Helper":
    st.header("Admission Helper Chat")
    st.caption("Ask me questions about Ontario university admissions, prerequisite rules, OUAC deadlines, or averages required for competitive programs.")

    # Prevent AI hallucinations
    system_prompt = (
            "You are a helpful Ontario University Admission Assistant.\n\n"

            "Your job is to help Grade 12 students understand:\n"
            "- Ontario university admission requirements\n"
            "- Required Grade 12 U/M prerequisite courses\n"
            "- Admission average ranges\n"
            "- OUAC application information and deadlines\n"
            "- Supplemental application requirements\n"
            "- Program eligibility based on a student's marks and courses\n\n"

            "Use only the information provided in the context documents when answering questions.\n"
            "Do not make up information.\n\n"

            "📋 Student Profile\n"




            "When a student asks if they are eligible for a university program:\n"
            "1. Check the admission average or admission range in the provided documents.\n"
            "2. Check the required Grade 12 U/M prerequisite courses.\n"
            "3. Compare the student's courses and average against those requirements.\n"
            "4. Explain your reasoning clearly.\n\n"

            "Important Rules:\n"
            "- Never guarantee admission.\n"
            "- Use phrases such as 'eligible to apply', "
            "'meets the published requirements', or "
            "'falls within the admission range'.\n"
            "- Admission decisions depend on many factors and can change each year.\n"
            "- If a required course is missing, clearly state which prerequisite is missing.\n"
            "- Only discuss Ontario university admissions and OUAC-related information.\n"
            "- Do not guess admission averages, prerequisite courses, deadlines, or requirements.\n"
            "- Do not provide information that is not supported by the context documents.\n\n"

            "If the answer cannot be found in the provided documents, respond with:\n"
            "'I couldn't find that information in the admission resources currently available. "
            "Please check the university's official admissions website for the most up-to-date information.'\n\n"

            "Keep your answers friendly, accurate, and easy for Grade 12 students to understand.\n\n"

            "Context:\n{context}"
        )

# OUAC COST PAGE
elif selected_page == "Application Cost Planner":
    st.header(" University Application Cost Planner via OUAC")

    # OUAC fees (3 choices )
    base_fee = 156.00
    # each additional program after 3
    additional_fee = 50.00

    page_header("Select Program", color = "red", size = 21)

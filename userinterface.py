
from asyncio import streams
import streamlit as st
import os
import pandas as pan
import datetime
import re
from program_database import program_database,universities,streams,course_names,ouac_deadlines

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

# GROQ API key









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
        
        portal_column1, portal_column2 = st.columns(2)
        
        with portal_column1:
            # link for OUAC
            st.markdown(
                """
                <div style="background-color:#F8FAFC; padding:12px; border-radius:8px; border-left:4px solid #3B82F6; margin-bottom:10px;">
                    <strong style="color:#1E293B;">OUAC Undergraduate Portal</strong><br>
                    <span style="font-size:0.85em; color:#64748B;">Apply to Ontario universities, manage your choices, and track your application status.</span><br>
                    <a href="https://ouac.on.ca" target="_blank" style="font-size:0.9em; color:#2563EB; font-weight:bold; text-decoration:none;">Launch OUAC Hub ↗</a>
                </div>
                """, unsafe_allow_html=True
            )
            # link for OUInfo
            st.markdown(
                """
                <div style="background-color:#F8FAFC; padding:12px; border-radius:8px; border-left:4px solid #10B981; margin-bottom:10px;">
                    <strong style="color:#1E293B;">Ontario Universities' Info (OUInfo)</strong><br>
                    <span style="font-size:0.85em; color:#64748B;">Explore Ontario university programs, admission averages, and program requirements.</span><br>
                    <a href="https://ouinfo.ca" target="_blank" style="font-size:0.9em; color:#059669; font-weight:bold; text-decoration:none;">Browse OUInfo Registry ↗</a>
                </div>
                """, unsafe_allow_html=True
            )

        with portal_column2:
            # link for ONTransfer
            st.markdown(
                """
                <div style="background-color:#F8FAFC; padding:12px; border-radius:8px; border-left:4px solid #F59E0B; margin-bottom:10px;">
                    <strong style="color:#1E293B;">ONTransfer Directory</strong><br>
                    <span style="font-size:0.85em; color:#64748B;">Learn how college courses and programs may transfer to universities in Ontario.</span><br>
                    <a href="https://ontransfer.ca" target="_blank" style="font-size:0.9em; color:#D97706; font-weight:bold; text-decoration:none;">Check Course Pathways ↗</a>
                </div>
                """, unsafe_allow_html=True
            )
            # link for OSAP page
            st.markdown(
                """
                <div style="background-color:#F8FAFC; padding:12px; border-radius:8px; border-left:4px solid #8B5CF6; margin-bottom:10px;">
                    <strong style="color:#1E293B;">OSAP Financial Aid Estimator</strong><br>
                    <span style="font-size:0.85em; color:#64748B;">Calculate provincial funding grants and loan configurations early.</span><br>
                    <a href="https://ontario.ca" target="_blank" style="font-size:0.9em; color:#7C3AED; font-weight:bold; text-decoration:none;">Open OSAP Portal ↗</a>
                </div>
                """, unsafe_allow_html=True
            )

# USER PROFILE

elif selected_page == "Course Prerequisite Checker":
    st.header("Course Prerequisite Checker")

    st.divider()

    # Verify if grades exist in the global calculator cache
    active_marks = st.session_state.get("course_grade_matrix", {})
    has_synced_data = bool(active_marks)

    if has_synced_data:

        #st.info(f"🔄 **Active Synced Profile:** `{st.session_state.course_summary_string}`")
        page_header("Selected Courses", color="Green", size=24)

        title_col, score_col = st.columns([3, 1])

        with title_col:
            st.markdown("**Course Name**")

        with score_col:
            st.markdown("**Mark**")

        for subject_code, percent_score in active_marks.items():

            title_col, score_col = st.columns([3, 1])

            with title_col:
                st.write(subject_code)

            with score_col:
                st.write(f"{percent_score}%")

        st.divider()

    else:
        st.info("No courses or marks found. Please calculate your average first to sync your profile.")

    # Provide feedback on average
    average = st.session_state.student_profile.get("average", 0)
    if average >= 90:
        st.success(
            "Great job! You have a competitive average for Ontario universities."
        )
        

    elif average >= 80:
        st.info(
            "Check Course Prerequisites Validator page for more information."
        )
        

    else:
        st.warning(
            "Please go over the admission requirements of your target universities."
        )

    page_header("Select Target Program", color = "red", size = 21)

    program_top_one = ""

    # user input takes raaw keys converts to clean names via lambda 
    select_program = st.selectbox(
        "", list(program_database.keys()),
        format_func = lambda x: program_database[x]["display_name"],
        key = "program_selector"
    )

    # update top one choice
    program_top_one = program_database[select_program]

    required_courses = program_top_one.get("required", [])
    vacant_courses = [
        course for course in required_courses
        if course not in active_marks or not active_marks[course]]

    st.session_state.student_profile["target_program"] = program_top_one
    st.divider()

    # make columns to display student average and required average
    col1, col2 = st.columns(2)

    # assign column roles
    with col1:
        if vacant_courses:
            st.error(f"You have not completed course selection. You need:  {", ".join(vacant_courses) }")
        else:
            if st.session_state.student_profile["average"] == 0:
                st.warning("You have not added your course marks in the system.")
            else:
                st.success("You have successfully recorded your course average.")

    # compare prerequistes to student marks
    with col2:
        if average >= program_top_one["target_avg"]:
            st.metric(
                label="Target Admission Match", 
                value=f"{st.session_state.student_profile['average']:.1f}%", 
                delta= f"+{(average - program_top_one['target_avg']):.1f}% over target")
        else:
            st.metric(label="Target Admission Match", 
                      value=f"{st.session_state.student_profile["average"]:.1f}%", 
                      delta=f"-{(program_top_one['target_avg'] - average):.1f}% below target", 
                      delta_color="inverse")
            
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

  
    required_courses = streams[stream]["required"]
    
    # Location to store user input
    selected_courses = []
    student_marks = []
    course_marks = {}



    # Required courses and marks display
    page_header("Required Courses", color = "green", size = 21)

    for course in required_courses:
        column1, column2 = st.columns([3, 1])

        with column1:
            st.write(f"**{course} - {course_names.get(course, course)}**")

        with column2:
            grade = st.text_input(
                "Mark",
                value = str(st.session_state.course_grades.get(course, 0)),
                key = f"grade_{course}",
                label_visibility = "collapsed"
            )

        try:
            mark = int(grade)
        except ValueError:
            mark = 0

        selected_courses.append(course)
        student_marks.append(grade)
        course_marks[course] = grade

    extra_courses = 6 - len(required_courses)

    st.divider()

    # picking electives
    page_header( f"Choose {extra_courses} Additional U/M Course", color= "Blue", size = 20)

    # list of available courses for user
    available_optional_courses = [
        course for course in course_names.keys()
        if course not in required_courses
    ]

    # Table of electives and marks
    column1, column2 = st.columns([3, 1])

    # elective course name column
    with column1:
        st.markdown("**Elective**")

    # elective course mark column
    with column2:
        st.markdown("**Mark**")
    
    # makes table depending on how many electives are needed by loop
    for i in range(extra_courses):

        column1, column2 = st.columns([3, 1])

        # display options for electives
        with column1:
            elective_course = st.selectbox(
            "", available_optional_courses,
            key = f"elective_course_{i}",
            label_visibility = "collapsed"
            )

        # marks user input for elective
        with column2:
            mark = st.text_input(
                "",
                value = str(st.session_state.course_grades.get(elective_course, 0)), 
                key = f"elective_mark_{i}",
                label_visibility = "collapsed"
            )

        # convert uer input to integer 
        try:
            mark = int(mark)
        except ValueError:
            mark = 0

        # add to selected courses profile , record marks
        selected_courses.append(elective_course)
        student_marks.append(mark)
        course_marks[elective_course] = mark

        # remove chosen electiive from available courses to avoid duplicates
        if elective_course in available_optional_courses:
                available_optional_courses.remove(elective_course)

    # CALCULATE TOP 6
    
    # AVERAGE CALCULATION

    # sum for all marks
    sum = 0
    for i in student_marks:
        sum += int(i)

    # calculate average
    student_course_average = sum / len(student_marks)

    # record to student profile in system
    st.session_state.course_grade_matrix = course_marks
    st.session_state.student_profile["average"] = student_course_average
    st.session_state.student_profile["marks"] = mark

    st.divider()

    # missing courses
    vacant_courses = [ course for course in required_courses if course not in course_marks or course_marks[course] == 0]

    # warning about missing courses
    if vacant_courses:
        st.warning("All information that is required has not been filled out")

    else:
        st.metric( "Top 6 Course Average",
                  f"{student_course_average:.2f}%")

        # Record user input to session 

        st.session_state.student_profile["marks"] = course_marks
        st.session_state.student_profile["average"] = student_course_average
        st.session_state.course_grades = course_marks
        st.rerun()




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
    st.header(" University Application Cost Planner via OUAC ")

    # OUAC fees (3 choices )
    base_fee = 156.00
    # each additional program after 3
    additional_fee = 50.00

    page_header("Select Program", color = "red", size = 21)
    
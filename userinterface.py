import streamlit as st
import os
import lancedb
import datetime
from operator import itemgetter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import LanceDB
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from program_database import program_database,universities,streams,course_names,admission_timelines,FIELD_OF_STUDY

st.set_page_config(
    page_title="Ontario University Admission Helper",
    page_icon="🏛️",
    layout="centered"
)

# Initialize Session State Variables to save user input across menu swaps
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
        "marks": {},
		"missing_courses": {},
    }

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"role": "assistant", "content": "Hello! Ask me anything about Ontario university prerequisite rules, OUAC deadlines, or competitive program averages."}
    ]

def page_header(text, color="blue", size=22):
    st.markdown(
        f"""
        <h3 style="color:{color}; font-size:{size}px; margin-bottom:-10px;">
            {text}
        </h3>
        """,
        unsafe_allow_html=True
    )

TOP_COURSES_REQUIRED = 6
def calculate_admission_average(
    course_grades,
    required_courses,
    top_n=TOP_COURSES_REQUIRED
):

    required_entries = []
    elective_entries = []

    for course, grade in course_grades.items():

        if course in required_courses:
            required_entries.append((course, grade))
        else:
            elective_entries.append((course, grade))

    elective_entries.sort(
        key=lambda x: x[1],
        reverse=True
    )

    remaining_slots = max(
        0,
        top_n - len(required_entries)
    )

    selected_electives = (
        elective_entries[:remaining_slots]
    )

    selected_courses = (
        required_entries +
        selected_electives
    )

    average = (
        sum(
            grade
            for _, grade in selected_courses
        ) / top_n
        if len(selected_courses) >= top_n
        else 0.0
    )

    return (
        average,
        selected_courses,
        len(course_grades)
    )

# Updates student profile, admission average,and course summary information.
def sync_student_profile(required_courses):

    if "course_grades" not in st.session_state:
        st.session_state.course_grades = {}

    # Keep only entered grades
    course_grades = {
        course: grade
        for course, grade in st.session_state.course_grades.items()
        if grade > 0
    }

    admission_average,top_courses,completed_courses = calculate_admission_average(
        course_grades=course_grades,
        required_courses=required_courses
    )

    # Session-level values
    st.session_state.student_average = admission_average
    st.session_state.course_grade_matrix = course_grades

    st.session_state.course_summary_string = (
        " | ".join(
            f"{course}: {grade:.1f}%"
            for course, grade in course_grades.items()
        )
        if course_grades
        else "No courses recorded yet."
    )

    # Student profile
    if "student_profile" not in st.session_state:
        st.session_state.student_profile = {}

    st.session_state.student_profile.update({
        "marks": course_grades,
        "average": admission_average,
        "top_courses": top_courses,
        "total_courses_entered": completed_courses
    })
#Clears all marks, averages, electives,and admission calculation data.
def clear_student_profile():
    # Reset grade data
    st.session_state.course_grades = {}
    st.session_state.course_grade_matrix = {}
    st.session_state.student_average = 0.0
    st.session_state.course_summary_string = (
        "No courses recorded yet."
    )

    # Reset profile values
    if "student_profile" in st.session_state:
        st.session_state.student_profile.update({
            "marks": {},
            "average": 0.0,
            "top_courses": [],
            "total_courses_entered": 0,
            "target_program": ""
        })

    # Remove widget state
    keys_to_delete = [
        key
        for key in st.session_state.keys()
        if (
            "_grade_" in key
            or "_elective_grade_" in key
            or "_elective_course_" in key
            or "_selected_electives" in key
            or "elective_slot_" in key
        )
    ]

    for key in keys_to_delete:
        del st.session_state[key]
        
def get_next_milestone():

    today = datetime.datetime.today().date()

    for milestone in admission_timelines:

        milestone_date = datetime.datetime.strptime(
            milestone["date"],
            "%Y-%m-%d"
        ).date()

        if milestone_date >= today:

            days_remaining = (
                milestone_date - today
            ).days

            return (
                milestone_date,
                milestone["title"],
                days_remaining
            )

    return None, None, None

# Left Menu Bar
with st.sidebar:
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(
            """
            <div style="
                text-align:center;
                color:#60A5FA;
                font-size:3rem;
                font-weight:600;
            ">
                🏛️
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """
            <div style="
                color:#4F8BF9;
                font-size:1.7rem;
                font-weight:700;
                line-height:1.2;
                margin-top:2px;
            ">
                Ontario University Admission Helper
            </div>
            """,
            unsafe_allow_html=True
        )
    st.divider()

    with st.container(border=True):

        st.markdown(
            """
            <div style='color:#7DD3FC;
                        font-size:1.05rem;
                        font-weight:600;
                        margin-bottom:8px;'>
                Student Snapshot
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("**Top 6 Average**")

        avg = st.session_state.student_profile.get(
            "average",
            0.0
        )

        if avg > 0:

            st.markdown(
                f"""
                <div style="
                    font-size:1.5rem;
                    font-weight:600;
                    margin-top:-8px;
                    margin-bottom:8px;
                ">
                    {avg:.1f}%
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.caption("Not Calculated")

        st.markdown("**Admission Goal**")

        target_stream = st.session_state.student_profile.get(
            "target_stream"
        )

        required_courses = (
            streams.get(target_stream, {})
            .get("required", [])
        )

        sync_student_profile(required_courses)
        
        st.session_state.required_courses = required_courses
        target_program = st.session_state.student_profile.get(
            "target_program",
            ""
        )

        if target_program:

            st.caption(target_program)

        else:

            target_stream = st.session_state.student_profile.get(
                "target_stream",
                ""
            )

            if target_stream:

                st.caption(f"{target_stream} Programs")

            else:

                st.caption("Not Selected")

    #CONTAINER FOR THE NAVIATION 
    with st.container(border=True):

        st.markdown("<div style='padding-top:5px'></div>",
                    unsafe_allow_html=True)

        st.markdown(
            "<div style='color:#7DD3FC;font-size:1.05rem;"
            "font-weight:600;'>Navigation</div>",
            unsafe_allow_html=True
        )

        selected_page = st.radio(
            "",
            [
                "Admission Helper Chat",
                "Top 6 Average Calculator",
                "Admission Requirements Checker",
                "Application Cost Planner",
                "Admissions Timeline & Resources"
            ],
            label_visibility="collapsed"
        )

    #st.divider()

    #CONTAINER for the NEXT MILESTONE
    next_date, next_title, days_remaining = (
        get_next_milestone()
    )

    if next_date:

        with st.container(border=True):

            st.markdown(
                """
                <div style='color:#7DD3FC;
                            font-size:1.05rem;
                            font-weight:600;
                            margin-bottom:8px;'>
                    Upcoming Deadline
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(f"**{next_title}**")

            st.caption(next_date.strftime("%B %d, %Y"))

            st.caption(f"{days_remaining} Days Remaining")

        st.caption(
            "Designed for Ontario Grade 12 students applying through OUAC."
        )

# Import GROQ_KEY from secrets into os environ
if "GROQ_API_KEY" in st.secrets:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]

else:
    st.error("Groq API key is not found.")
    st.stop()


# Load the admission knowledge base
@st.cache_resource
def load_admin_admission_knowledge():

    admission_db = lancedb.connect("vector_database")
    
    if "ontario_admissions" not in admission_db.table_names():
        st.error("The admissions database table 'ontario_admissions' was not found.")

    oauc_hugging_embed_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vectorstore = LanceDB(
        connection = admission_db,
        table_name ="ontario_admissions",
        embedding = oauc_hugging_embed_model,
    )
 

    # get the admission data
    # Used the nearest search alogirhtm..also try the neighbourhood algorithm and see the difference.
    admission_docs = vectorstore.as_retriever( search_kwargs = {"k" : 8 })
    
    # LLM model
    # Note: tried with different models, including google gemini, but this has daily quota more
    admission_model = ChatGroq(
        model_name = "openai/gpt-oss-20b", 
        temperature= 0.1,
        max_retries = 3,
        timeout = 60.0
    )    
    return admission_docs, admission_model
try:
    admission_docs, admission_model = ( load_admin_admission_knowledge())
except Exception as e:
    st.error(
        f"The admission database could not be loaded: {e}"
    )
    st.stop()


#Admission requirement checker

if selected_page == "Admission Requirements Checker":

    st.header("Admission Requirements Checker")

    st.caption(
        "Check whether you meet the Grade 12 course requirements for your chosen program."
    )

    st.divider()

    has_synced_grades = (
        "course_grade_matrix" in st.session_state
        and len(st.session_state.course_grade_matrix) > 0
    )

    if not has_synced_grades:

        st.warning(
            "Please enter your courses and marks in the Top 6 Average Calculator first."
        )

    else:

        saved_marks = st.session_state.course_grade_matrix

        #Select the Program
        left_col, right_col = st.columns([3, 2])

        with left_col:

            with st.container(border=True):

                page_header(
                    "Program Selection",
                    color="#60A5FA",
                    size=22
                )

                st.caption("Field of Study")

                stream_options = list(streams.keys())

                saved_stream = st.session_state.student_profile.get(
                    "target_stream",
                    "Engineering"
                )

                default_stream_index = (
                    stream_options.index(saved_stream)
                    if saved_stream in stream_options
                    else 0
                )

                stream = st.selectbox(
                    "Field of Study",
                    stream_options,
                    index=default_stream_index,
                    key="validator_stream"
                )

                program_keys = [
                    program
                    for program in program_database.keys()
                    if FIELD_OF_STUDY.get(program) == stream
                ]

                saved_program = st.session_state.student_profile.get(
                    "target_program",
                    ""
                )

                default_program_index = (
                    program_keys.index(saved_program)
                    if saved_program in program_keys
                    else 0
                )

                selected_program = st.selectbox(
                    "Target Program",
                    program_keys,
                    index=default_program_index,
                    format_func=lambda x: program_database[x]["display_name"],
                    key="validator_program"
                )

        #the required courses for the selected program
        required_courses = program_database[selected_program]["required"]

        # student marks
        all_marks = {
            course.split(" - ")[0].strip(): grade
            for course, grade in saved_marks.items()
            if grade > 0
        }

        #check the required courses
        met_courses = [
            course
            for course in required_courses
            if course in all_marks
        ]

        missing_courses = [
            course
            for course in required_courses
            if course not in all_marks
        ]

        met_count = len(met_courses)
        total_required = len(required_courses)
       
        top_courses = st.session_state.student_profile.get( "top_courses",  [] )

       # Academic snapshot of the student
        with right_col:

            with st.container(border=True):

                page_header(
                    "Academic Snapshot",
                    color="#60A5FA",
                    size=22
                )

                st.caption("Admission Average")

                st.markdown(f"## {st.session_state.student_average:.1f}%" )

                st.caption("Requirements Met")

                st.markdown( f"### {met_count} / {total_required}" )

        st.divider()

        # Courses used in the the admission average
        page_header(
            "Courses Used in Admission Average",
            color="#22C55E",
            size=22
        )

        with st.container(border=True):

            for course, grade in top_courses:

                is_required = course in required_courses

                icon = "✓" if is_required else "○"

                label = (
                    f"{icon} {course} - "
                    f"{course_names.get(course, course)} "
                    f"({grade:.0f}%)"
                )

                if is_required:
                    st.success(label)
                else:
                    st.info(label)


        st.caption(
            "✓ Required course for the selected program | ○ Additional course included in your Top 6 Average"
        )
        st.divider()

        # Missing courses details
        if missing_courses:

            page_header(
                "Missing Required Courses",
                color="#EF4444",
                size=22
            )

            with st.container(border=True):

                for course in missing_courses:

                    st.error(
                        f"✗ {course} - "
                        f"{course_names.get(course, course)}"
                    )

            st.divider()

            # ==========================================
            # NEXT STEPS
            # ==========================================

            page_header(
                "Next Steps",
                color="#60A5FA",
                size=22
            )

            with st.container(border=True):

                st.write(
                    f"To meet the prerequisite requirements for **{program_database[selected_program]['display_name']}**, consider completing:"
                )

                for course in missing_courses:

                    st.write(
                        f"• {course} - {course_names.get(course, course)}"
                    )

                st.caption(
                    "You can explore other programs or universities that match your current course profile using the Admission Helper."
                )

    #        st.divider()
        else:

            page_header(
                "Next Steps",
                color="#60A5FA",
                size=22
            )

            with st.container(border=True):

                st.success(
                    f"You currently meet the published prerequisite requirements for {program_database[selected_program]['display_name']}."
                )
    #        st.divider()    

# Admission timelines and  Resources page
elif selected_page == "Admissions Timeline & Resources":

    st.header("Admissions Timeline & Resources")

    st.caption(
        "Key admission dates, program requirements, and official Ontario university resources."
    )

    st.divider()

    timeline_col, reminder_col = st.columns([3, 2])

    #admission timelines
    with timeline_col:

        page_header(
            "Admissions Timeline",
            color="#60A5FA",
            size=22
        )

        general_deadlines = [
            item
            for item in admission_timelines
            if item["category"] == "General"
        ]

        for item in general_deadlines:

            with st.container(border=True):

                st.markdown(
                    f"#### {item['date']}"
                )

                st.markdown(
                    f"**{item['title']}**"
                )

                st.caption(
                    item["details"]
                )

    #Ontario admission dates
    with reminder_col:

        page_header(
            "Program Requirements",
            color="#22C55E",
            size=22
        )

        program_reminders = [
            item
            for item in admission_timelines
            if item["category"] == "Program"
        ]

        for item in program_reminders:

            with st.container(border=True):

                st.markdown(f"**{item['program']}**")

                st.caption(item["date"])

                st.write(item["title"])

    st.divider()


    # Official admission resources
    page_header(
        "Official Resources",
        color="#F59E0B",
        size=22
    )

    resource_col1, resource_col2, resource_col3 = st.columns(3)
    # link for OUAC
    with resource_col1:
        st.link_button(
            "OUAC Key Dates",
            "https://www.ouac.on.ca/guide/undergrad-dates/"
        )

    with resource_col2:
        st.link_button(
            "OUInfo Programs",
            "https://www.ouinfo.ca/"
        )

    with resource_col3:
        st.link_button(
            "OUAC Website",
            "https://www.ouac.on.ca/"
        )


# CHAT ASSISTANT PAGE
elif selected_page == "Admission Helper Chat":
    st.header("Ontario University Admission Helper")

    #Has the student entered at least 6 valid course marks
    valid_grades = [
        grade
        for grade in st.session_state.course_grades.values()
        if grade > 0
    ]
    has_calculation = len(valid_grades) >= 6

    if not has_calculation:
        st.markdown("""
        <div style="
            background-color:#1E293B;
            padding:20px;
            border-radius:12px;
            color:#F8FAFC;
        ">

        <h2 style="color:#60A5FA; margin-top:0;">Welcome</h2>

        <p>
        Ask questions about Ontario university programs, admission requirements,
        deadlines, and application costs.
        </p>

        <p>
        For more personalized guidance:
        </p>

        <ul>
        <li><strong>Calculate your Top 6 Average</strong></li>
        <li><strong>Check Program Prerequisites</strong></li>
        </ul>

        <p><em>No courses have been evaluated yet.</em></p>

        </div>
        """, unsafe_allow_html=True)

    else:
        avg = st.session_state.student_average

        stream = st.session_state.student_profile.get("target_stream", "")

        st.markdown(f"""
        <div style="
            background-color:#1E293B;
            padding:20px;
            border-radius:12px;
            color:#F8FAFC;
            border-left:5px solid #22C55E;
        ">
        <h2 style="color:#22C55E; margin-top:0;">Welcome Back</h2>
        <p>
        You're currently exploring <strong>{stream}</strong> programs.
        </p>
        <p>
        <strong>Top 6 Average:</strong>
        <span style="color:#60A5FA; font-size:18px;">
        {avg:.1f}%
        </span>
        </p>

        <p>
        Ask questions about programs, admission requirements,
        deadlines, application costs, and OUAC applications.
        </p>

        </div>
        """, unsafe_allow_html=True)

        
    # Combine search results into one text block
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
 

    system_prompt = f"""
        You are a helpful Ontario University Admission Assistant.

        Your purpose is to help Grade 12 students understand:

        • Ontario university admissions
        • OUAC applications and deadlines
        • Program prerequisites
        • Admission averages
        • Supplementary applications
        • University program information

        ==================================================
        STUDENT PROFILE
        ==================================================

        Current Area of Interest:
        {st.session_state.student_profile.get("target_stream", "Not Selected")}

        Top 6 Average:
        {st.session_state.student_profile.get("average", 0.0):.1f}%

        Courses and Marks:
        {st.session_state.course_summary_string}

        Admission target averages display:
        {chr(10).join([f"        - {info['display_name']}: {info['target_avg']:.1f}%" for info in program_database.values() if info.get('target_avg') is not None])}
        ==================================================
        ADMISSION RULES
        ==================================================

        When discussing university admissions:

        • Review prerequisite courses when relevant.
        • Use the student's courses and Top 6 Average when helpful.
        • Compare admission averages only when published information is available.
        • Identify missing prerequisite courses when applicable.
        • Never guarantee admission.
        • Never guess admission requirements, averages, deadlines, or policies.
        • Use only information found in the admission resources.
        • Consider both completed and in-progress Grade 12 U/M courses.

        Use phrases such as:

        • "Eligible to apply"
        • "Meets the published requirements"
        • "Appears competitive"
        • "Falls below the typical competitive average"
        • "Falls within the competitive range"

        Admission decisions vary from year to year.

        ==================================================
        STRICT PREREQUISITE VALIDATION
        ==================================================

        Match prerequisites only using exact Ontario course codes.

        Course Reference:

        ENG4U = English
        MHF4U = Advanced Functions
        MCV4U = Calculus & Vectors
        MDM4U = Data Management
        SBI4U = Biology
        SCH4U = Chemistry
        SPH4U = Physics
        ICS4U = Computer Science

        Validation Rules:

        • Never substitute one course for another.
        • Never guess course equivalencies.
        • Never assume one science course satisfies another science prerequisite.
        • Only mark a prerequisite as Met when the exact required course code is present.
        • If the required course is not present, mark it Missing.
        • If verification is not possible, mark it Unable to Verify.

        Examples:

        • Biology U = SBI4U only
        • Chemistry U = SCH4U only
        • Physics U = SPH4U only
        • Advanced Functions U = MHF4U only
        • Calculus & Vectors U = MCV4U only
        • English U = ENG4U only

        If SBI4U is missing, Biology U must be marked as Missing.

        ==================================================
        OUAC & ADMISSIONS
        ==================================================

        You may answer questions about:

        • Ontario university programs
        • Admission requirements
        • Prerequisite courses
        • OUAC applications
        • Admission timelines
        • Supplementary applications

        If information is unavailable in the admission resources, respond:

        "I couldn't find that information in the admission resources currently available. Please check the university's official admissions website for the most up-to-date information."

        ==================================================
        RESPONSE STYLE
        ==================================================

        • Answer the student's question directly.
        • Use simple and student-friendly language.
        • Reference the student's courses and Top 6 Average when relevant.
        • Explain admission requirements clearly.
        • When discussing prerequisites, explicitly identify:
        ✓ Met requirements
        ✗ Missing requirements
        • Recommend helpful next steps when appropriate.
        • Keep responses concise, accurate, and supportive.
        • Never present an admission prediction as a certainty.

        Context:
        {{context}}
        """
    #build Rag
    prompt_roles = ChatPromptTemplate.from_messages([
        ("system", system_prompt), ("human", "{input}")])

    # establish rag logic proccess
    rag_logic_chain = (RunnableParallel({"context": itemgetter("input") | admission_docs | format_docs, "input": itemgetter("input")})
        | prompt_roles
        | admission_model
        | StrOutputParser()
    )
    # Display conversation history
    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Process student question
    if user_query := st.chat_input("Ex: Am I eligible for Waterloo Software Engineering with my marks?"):
        
        st.session_state.chat_messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)
            
        with st.chat_message("assistant"):
            with st.spinner("Analyzing relevant info from official docs..."):
                try:
                    output = rag_logic_chain.invoke({"input": user_query})
                  
                    output = (output.replace("<br>", "\n").replace("<br/>", "\n").replace("<br />", "\n").replace("&lt;br&gt;", "\n"))

                     # gather source based on user query
                    source_documents = (
                        admission_docs.invoke(user_query)
                        or []
                    )

                    sources = {
                        os.path.basename(
                            doc.metadata.get(
                                "source",
                                "Unknown Guide"
                            )
                        )
                        for doc in source_documents
                        if doc is not None
                    }


                    # Display to user sources used to answer the student question
                    if sources:
                        output += f"\n **Sources Used:** _{', '.join(sources)}_"
                    
                    # display chatbot answer
                    st.markdown(output)

                    # record assistant output to session_state
                    st.session_state.chat_messages.append({"role": "assistant", "content": output})

                except Exception as e:
                    st.error(f"Unable to process the question: {e}")

elif selected_page == "Top 6 Average Calculator":

    MAX_TOTAL_COURSES = 10

    st.header("Top 6 Average Calculator")
    st.caption("Select a program area and enter your Grade 12 U/M course marks.")
    st.divider()

    if "course_grades" not in st.session_state:
        st.session_state.course_grades = {}

    selection_col, snapshot_col = st.columns([2.5, 2.5])

    with selection_col:

        with st.container(border=True):

            stream_options = list(streams.keys())
            saved_stream = st.session_state.student_profile.get("target_stream")
            default_index = stream_options.index(saved_stream) if saved_stream in stream_options else 0

            stream = st.selectbox(
                "Field of Study",
                stream_options,
                index=default_index
            )

            if stream != saved_stream:
                clear_student_profile()

            st.session_state.student_profile["target_stream"] = stream

    required_courses = streams[stream]["required"]

    with snapshot_col:

        with st.container(border=True):

            # CALCULATE TOP 6
            admission_average, admission_courses, completed_courses = calculate_admission_average(
                st.session_state.course_grades,
                required_courses
            )

            st.markdown(
                f"<h2 style='margin-bottom:0;'>{admission_average:.1f}%</h2>",
                unsafe_allow_html=True
            )

            st.caption("Selected Stream")
            st.markdown(f"**{stream}**")
            st.caption(f"{min(completed_courses, 6)} of 6 courses entered")

    st.divider()

    page_header("Required Courses", color="#60A5FA", size=22)

    for course in required_courses:

        col1, col2 = st.columns([3, 1])

        with col1:

            # elective course name column
            st.write(f"**{course} - {course_names.get(course, course)}**")

        with col2:

            grade = st.number_input(
                "Mark",
                min_value=0.0,
                max_value=100.0,
                value=float(st.session_state.course_grades.get(course, 0.0)),
                step=0.5,
                key=f"{stream}_grade_{course}",
                label_visibility="collapsed"
            )

            # add to selected courses profile , record marks
            if grade > 0:
                st.session_state.course_grades[course] = grade
                sync_student_profile(required_courses)

    st.divider()

    # picking electives
    page_header("Additional Grade 12 Courses", color="#60A5FA", size=22)

    def course_label(course):
        return f"{course} - {course_names.get(course, '')}"

    # Table of electives and marks

    # list of available courses for student
    available_electives = [
        course
        for course in course_names
        if course not in required_courses
    ]

    remaining_slots = MAX_TOTAL_COURSES - len(required_courses)

    state_key = f"{stream}_selected_electives"

    if state_key not in st.session_state:
        st.session_state[state_key] = [None] * remaining_slots

    # makes table depending on how many electives are needed by loop
    for i in range(remaining_slots):

        col1, col2 = st.columns([3, 1])

        with col1:

            # display options for electives
            choices = ["Choose Additional Course"] + [
                course_label(course)
                for course in available_electives
                if course_label(course) not in st.session_state[state_key]
                or st.session_state[state_key][i] == course_label(course)
            ]

            saved_selection = st.session_state[state_key][i]

            default_index = (
                choices.index(saved_selection)
                 if saved_selection in choices and saved_selection != ""
                else 0
            )

            elective = st.selectbox(
                "",
                choices,
                index=default_index,
                key=f"{stream}_elective_course_{i}",
                label_visibility="collapsed"
            )

            st.session_state[state_key][i] = elective

        with col2:

             if elective and elective != "Choose Additional Course":

                elective_code = elective.split(" - ")[0]

                # marks user input for elective
                grade = st.number_input(
                    "",
                    min_value=0.0,
                    max_value=100.0,
                    value=float(
                        st.session_state.course_grades.get(
                            elective_code,
                            0.0
                        )
                    ),
                    step=0.5,
                    key=f"{stream}_elective_grade_{i}",
                    label_visibility="collapsed"
                )

                # convert uer input to integer

                # add to selected courses profile , record marks
                if grade > 0:
                    st.session_state.course_grades[elective_code] = grade
                    sync_student_profile(required_courses)

        # remove chosen electiive from available courses to avoid duplicates
        if elective:
            chosen_code = elective.split(" - ")[0]

            if chosen_code in available_electives:
                available_electives.remove(chosen_code)

    # Record user input to session
    course_grades = {
        course: grade
        for course, grade in st.session_state.course_grades.items()
        if grade > 0
    }

    # CALCULATE TOP 6
    admission_average, admission_courses, completed_courses = calculate_admission_average(
        course_grades,
        required_courses
    )

    # calculate average
    progress_value = min(completed_courses / 6, 1.0)

    # record to student profile in system
    st.progress(progress_value)

    st.caption(
        f"{min(completed_courses, 6)} of 6 courses entered"
    )

    # missing courses
    if completed_courses < 6:

        # warning about missing courses
        st.info(
            "Enter at least 6 Grade 12 U/M course marks to calculate your admission average."
        )

    else:

        st.success(
            f"Admission Average: {admission_average:.1f}%"
        )

        with st.expander(
            "Courses Used in Admission Average",
            expanded=True
        ):
            for course, grade in admission_courses:
                st.write(f"✅ {course}: {grade:.1f}%")

        st.markdown(
            """
            <div style="
                background:#0F172A;
                padding:14px;
                border-radius:10px;
                border:1px solid #334155;
                margin-top:10px;
            ">
                <strong>Ready to Explore</strong><br>
                Use Admission Assistant to compare programs,
                admission averages, application deadlines,
                tuition costs, and career pathways.
            </div>
            """,
            unsafe_allow_html=True
        )
# OUAC COST PAGE
elif selected_page == "Application Cost Planner":

    st.header("Application Cost Planner")

    st.caption(
        "Estimate your OUAC application costs based on the programs you plan to apply to."
    )


    # Minimum ontario university fee - OUAC fees (3 choices )
    base_fee = 159.00
    # each additional program after 3
    additional_fees = 51.00

    cost_col1, cost_col2 = st.columns([2 , 3])

    # Select the program to calculate the cost

    with cost_col1:
        with st.container(border=True):
            page_header("Select Programs", color="#60A5FA", size=24 )

            if st.button("Clear Choices", type="secondary"):

                for university, programs in universities.items():

                    for display_name in programs.keys():

                        checkbox_key =  f"{university}_{display_name}" 

                        if checkbox_key in st.session_state:

                            st.session_state[ checkbox_key ] = False

                st.rerun()


            st.caption(
                "Select one or more programs to estimate your application costs."
            )
            chosen_programs = []
            chosen_universities = set()

            for university, programs in universities.items():

                with st.expander( university, expanded=False ):

                    for display_name, ( program_key, fee ) in programs.items():

                        selected = st.checkbox( display_name, key=f"{university}_{display_name}" )

                        if selected:

                            chosen_programs.append( program_key )

                            chosen_universities.add( university )

                            if fee > 0:

                                st.caption( f"Supplementary Fee: ${fee:.0f}" )

            
            # build fee dictionary for lookup
            university_supplemental_fees = {}

            for programs in universities.values():

                for _, ( program_key, fee ) in programs.items():

                    university_supplemental_fees[ program_key ] = fee

    with cost_col2:
        with st.container(border=True):

            page_header("Application Summary", color="#60A5FA", size=24)

            total_choices_count = len(chosen_programs)

            university_count = len(chosen_universities)

            if total_choices_count == 0:

                st.info("Select one or more university programs to view your estimated application costs.")

            else:
                # base cost calculation
                additional_choices_count = max(0, total_choices_count - 3)

                additional_choice_charge = additional_choices_count * additional_fees

                # Calculate supplementary fees
                total_supp_charge = sum(university_supplemental_fees.get(program, 0) for program in chosen_programs)

                total_cost = base_fee + additional_choice_charge + total_supp_charge


                # total fee calculation
                st.metric("Estimated Application Cost", f"${total_cost:.0f}")

                metric_col1, metric_col2 = st.columns(2)

                with metric_col1:
                    st.metric("Programs Selected", total_choices_count)

                with metric_col2:
                    st.metric("Universities", university_count)

                st.divider()
                
                # breakdown display
                st.markdown("### Cost Breakdown")

                st.write(
                    f"OUAC Application Fee  : **${base_fee + additional_choice_charge:.2f}**"
                )

                st.write(
                    f"Supplementary Fees    : **${total_supp_charge:.2f}**"
                )

                st.divider()

                st.markdown("### Fee Disclaimer")

                st.caption(
                    """
                    Estimated costs are intended for planning purposes only.
                    Actual fees may vary depending on program selection,
                    supplementary application requirements, and updates
                    from OUAC or individual universities.
                    """
                )
 
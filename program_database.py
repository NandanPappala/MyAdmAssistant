    # Authoritative Ontario Prerequisite Database Structure
program_database = {

        # =====================================================
        # UNIVERSITY OF WATERLOO
        # =====================================================

        "Waterloo Engineering": {
            "display_name": "Waterloo Engineering",
            "required": ["ENG4U", "MHF4U", "MCV4U", "SCH4U", "SPH4U"],
            "target_avg": 95.0,
            "note": "One of Canada's most competitive engineering programs. Strong AIF and extracurricular involvement are important."
        },

        "Waterloo Architecture": {
            "display_name": "Waterloo Architecture",
            "required": ["ENG4U", "MHF4U"],
            "target_avg": 85.0,
            "note": "Portfolio and interview components play an important role in admissions."
        },

        # =====================================================
        # MCMASTER UNIVERSITY
        # =====================================================

        "McMaster Engineering": {
            "display_name": "McMaster Engineering",
            "required": ["ENG4U", "MHF4U", "MCV4U", "SCH4U", "SPH4U"],
            "target_avg": 90.0,
            "note": "Competitive admission with mandatory supplementary application."
        },

        "McMaster Health Sciences": {
            "display_name": "McMaster Health Sciences (BHSc)",
            "required": ["ENG4U", "MHF4U", "SBI4U", "SCH4U"],
            "target_avg": 95.0,
            "note": "One of Canada's most competitive health science programs. Supplementary application is heavily weighted."
        },

        # =====================================================
        # UNIVERSITY OF TORONTO
        # =====================================================

        "U of T Computer Science": {
            "display_name": "U of T Computer Science (St. George)",
            "required": ["ENG4U", "MHF4U", "MCV4U"],
            "target_avg": 92.0,
            "note": "Calculus and Advanced Functions are heavily considered during admission review."
        },

        "U of T Rotman Commerce": {
            "display_name": "U of T Rotman Commerce",
            "required": ["ENG4U", "MHF4U", "MCV4U"],
            "target_avg": 90.0,
            "note": "Strong mathematics performance and supplementary application recommended."
        },

        "U of T Engineering": {
            "display_name": "U of T Engineering",
            "required": ["ENG4U", "MHF4U", "MCV4U", "SCH4U", "SPH4U"],
            "target_avg": 93.0,
            "note": "Competitive engineering admission requiring strong science and mathematics grades."
        },

        "U of T Architecture": {
            "display_name": "U of T Architecture",
            "required": ["ENG4U"],
            "target_avg": 85.0,
            "note": "Portfolio, design ability, and academics are considered."
        },

        "U of T Medical Radiation Sciences": {
            "display_name": "U of T Medical Radiation Sciences",
            "required": ["ENG4U", "MHF4U", "SBI4U", "SCH4U"],
            "target_avg": 88.0,
            "note": "Strong grades in biology, chemistry, and mathematics are recommended."
        },

        "U of T Music": {
            "display_name": "U of T Music",
            "required": ["ENG4U"],
            "target_avg": 80.0,
            "note": "Auditions may be required depending on the specialization."
        },

        "U of T Doctor of Pharmacy": {
            "display_name": "U of T Doctor of Pharmacy",
            "required": [],
            "target_avg": 0.0,
            "note": "Not a direct-entry Grade 12 program. Requires previous post-secondary study."
        },

        "U of T PharmD for Pharmacists": {
            "display_name": "U of T PharmD for Pharmacists",
            "required": [],
            "target_avg": 0.0,
            "note": "Professional upgrading program for licensed pharmacists. Not intended for Grade 12 applicants."
        },

        # =====================================================
        # QUEEN'S UNIVERSITY
        # =====================================================

        "Queens Commerce": {
            "display_name": "Queen's Commerce (Smith School of Business)",
            "required": ["ENG4U", "MHF4U", "MCV4U"],
            "target_avg": 88.0,
            "note": "Competitive supplementary application and leadership experience are beneficial."
        },

        "Queens Engineering": {
            "display_name": "Queen's Engineering",
            "required": ["ENG4U", "MHF4U", "MCV4U", "SCH4U", "SPH4U"],
            "target_avg": 87.0,
            "note": "Admission is primarily based on academic performance."
        },

        "Queens Health Sciences": {
            "display_name": "Queen's Health Sciences",
            "required": ["ENG4U", "MHF4U", "SBI4U", "SCH4U"],
            "target_avg": 92.0,
            "note": "Highly competitive health sciences program with strong emphasis on academics."
        },

        # =====================================================
        # WESTERN UNIVERSITY
        # =====================================================

        "Western Ivey AEO": {
            "display_name": "Western Ivey AEO",
            "required": ["ENG4U", "MHF4U"],
            "target_avg": 93.0,
            "note": "Leadership, extracurricular activities, and a strong supplementary application are important."
        },

        "Western Engineering": {
            "display_name": "Western Engineering",
            "required": ["ENG4U", "MHF4U", "MCV4U", "SCH4U", "SPH4U"],
            "target_avg": 87.0,
            "note": "Strong performance in Grade 12 Math, Physics, and Chemistry is recommended."
        },

        "Western Computer Science": {
            "display_name": "Western Computer Science",
            "required": ["ENG4U", "MHF4U", "MCV4U"],
            "target_avg": 85.0,
            "note": "Calculus and Advanced Functions are required. Competitive averages are typically in the mid-to-high 80s."
        },

        "Western Health Sciences": {
            "display_name": "Western Health Sciences",
            "required": ["ENG4U", "SBI4U"],
            "target_avg": 84.0,
            "note": "Biology is recommended. Popular pathway for healthcare-related careers."
        },

        "Western Medical Sciences": {
            "display_name": "Western Medical Sciences",
            "required": ["ENG4U", "MHF4U", "SBI4U", "SCH4U"],
            "target_avg": 90.0,
            "note": "One of Western's most competitive science programs. Strong preparation for medicine, dentistry, and research."
        },

        "Western Science": {
            "display_name": "Western Science",
            "required": ["ENG4U", "MHF4U"],
            "target_avg": 82.0,
            "note": "Gateway program leading to majors in Biology, Chemistry, Physics, Mathematics, and related fields."
        },

        "Western Nursing": {
            "display_name": "Western Nursing",
            "required": ["ENG4U", "SBI4U", "SCH4U"],
            "target_avg": 88.0,
            "note": "Competitive program requiring strong science grades and communication skills."
        },

        "Western BMOS": {
            "display_name": "Western BMOS (Management & Organizational Studies)",
            "required": ["ENG4U", "MHF4U"],
            "target_avg": 84.0,
            "note": "Popular business-focused program and a common pathway into Ivey HBA after second year."
        }
    }    

universities = {

        "University of Waterloo": {
            "Engineering": ("Waterloo Engineering", 60.00),
            "Architecture": ("Waterloo Architecture", 60.00)
        },

        "McMaster University": {
            "Engineering": ("McMaster Engineering", 50.00),
            "Health Sciences": ("McMaster Health Sciences", 30.00)
        },

        "University of Toronto": {
            "Architecture": ("U of T Architecture", 100.00),
            "Rotman Commerce": ("U of T Rotman Commerce", 51.00),
            "Computer Science": ("U of T Computer Science", 51.00),
            "Engineering": ("U of T Engineering", 43.86),
            "Medical Radiation Sciences": ("U of T Medical Radiation Sciences", 50.00),
            "Music": ("U of T Music", 70.00),
            "Doctor of Pharmacy": ("U of T Doctor of Pharmacy", 169.00),
            "PharmD for Pharmacists": ("U of T PharmD for Pharmacists", 54.00)
        },

        "University of Guelph": {
            "Landscape Architecture": (
                "Guelph Landscape Architecture",
                60.00
            )
        },

        "York University": {
            "Arts, Media, Performance & Design": (
                "York Arts, Media, Performance & Design",
                25.00
            )
        },

        # Universities/programs with no supplementary fee
        "Queen's University": {
            "Commerce": ("Queens Commerce", 0.00),
            "Engineering": ("Queens Engineering", 0.00),
            "Health Sciences": ("Queens Health Sciences", 0.00)
        },

        "Western University": {
            "Ivey AEO": ("Western Ivey AEO", 0.00),
            "Engineering": ("Western Engineering", 0.00),
            "Computer Science": ("Western Computer Science", 0.00),
            "Health Sciences": ("Western Health Sciences", 0.00)
        }
    }

ontario_grade12_courses = {
    # ==================================================
    # ENGLISH
    # ==================================================
    "ENG4U": "English",
    "EAE4U": "English (French-Language Schools)",
    "ETS4U": "Studies in Literature",
    "EWC4U": "The Writer's Craft",

    # ==================================================
    # MATHEMATICS
    # ==================================================
    "MHF4U": "Advanced Functions",
    "MCV4U": "Calculus and Vectors",
    "MDM4U": "Mathematics of Data Management",

    # ==================================================
    # SCIENCE
    # ==================================================
    "SBI4U": "Biology",
    "SCH4U": "Chemistry",
    "SPH4U": "Physics",

    # ==================================================
    # COMPUTER STUDIES
    # ==================================================
    "ICS4U": "Computer Science",

    # ==================================================
    # BUSINESS STUDIES
    # ==================================================
    "BAT4M": "Financial Accounting Principles",
    "BBB4M": "International Business Fundamentals",
    "BOH4M": "Business Leadership: Management Fundamentals",

    # ==================================================
    # CANADIAN & WORLD STUDIES
    # ==================================================
    "CIA4U": "Analysing Current Economic Issues",
    "CGW4U": "World Issues: A Geographic Analysis",
    "CLN4U": "Canadian and International Law",
    "CPW4U": "Canadian and World Politics",
    "CHY4U": "World History Since the Fifteenth Century",
    "CGR4M": "Environment and Resource Management",

    # ==================================================
    # SOCIAL SCIENCES & HUMANITIES
    # ==================================================
    "HHS4U": "Families in Canada",
    "HHG4M": "Human Development Throughout the Lifespan",
    "HSB4U": "Challenge and Change in Society",
    "HZT4U": "Philosophy: Questions and Theories",
    "HFA4U": "Nutrition and Health",

    # ==================================================
    # FRENCH
    # ==================================================
    "FSF4U": "Core French",

    # ==================================================
    # CLASSICAL & INTERNATIONAL LANGUAGES
    # ==================================================
    "LVV4U": "Classical Civilization",
    "LWSCU": "Spanish",
    "LWICU": "Italian",
    "LWSCU": "Spanish",
    "LWPCU": "Portuguese",
    "LWRCU": "Russian",
    "LWGCU": "German",

    # ==================================================
    # ARTS
    # ==================================================

    "ADA4M": "Drama",
    "AMU4M": "Music",
    "AVI4M": "Visual Arts",
    "ASM4M": "Media Arts",
    "ATC4M": "Dance",

    # Visual Arts focus courses
    "AWD4M": "Visual Arts - Drawing",
    "AWQ4M": "Photography, Digital Imaging and Media Arts",
    "AWP4M": "Visual Arts Portfolio",

    # Music focus courses
    "AMC4M": "Music and Computers",
    "AMI4M": "Instrumental Music",
    "AMV4M": "Vocal/Choral Music",

    # Drama focus courses
    "ADB4M": "Dramatic Arts Production",
    "ADW4M": "Playwriting",

    # Dance focus courses
    "ATU4M": "Urban Dance",
    "ATY4M": "Ballet / Specialized Dance",

    # ==================================================
    # SOCIAL SCIENCES & HUMANITIES
    # ==================================================

    "HFA4U": "Nutrition and Health",
    "HHS4U": "Families in Canada",
    "HHD4M": "Working with Infants and Young Children",
    "HHG4M": "Human Development Throughout the Lifespan",
    "HIP4O": "Personal Life Management",
    "HSB4U": "Challenge and Change in Society",
    "HZT4U": "Philosophy: Questions and Theories",

    # ==================================================
    # CLASSICAL STUDIES & INTERNATIONAL LANGUAGES
    # ==================================================

    "LVV4U": "Classical Civilization",

    # Language courses may vary by school board
    "LWBDU": "Arabic",
    "LWCDU": "Chinese",
    "LWGDU": "German",
    "LWIDU": "Italian",
    "LWJDU": "Japanese",
    "LWKDU": "Korean",
    "LWODU": "Spanish",
    "LWRDU": "Russian",
    "LWPDU": "Portuguese",
    "LWSDU": "Spanish",

    # ==================================================
    # HEALTH & PHYSICAL EDUCATION
    # ==================================================

    "PSK4U": "Introductory Kinesiology",
    "PLF4M": "Recreation and Healthy Active Living Leadership",

    # ==================================================
    # TECHNOLOGICAL EDUCATION
    # ==================================================

    "TEJ4M": "Computer Engineering Technology",
    "TGJ4M": "Communications Technology",
    "TDA4M": "Architectural Design",
    "TDJ4M": "Technological Design",
    "TFJ4M": "Hospitality and Tourism",
    "THJ4M": "Green Industries",
    "TMJ4M": "Manufacturing Engineering Technology",
    "TOJ4M": "Transportation Technology",
    "TPJ4M": "Health Care",
    "TXJ4M": "Construction Technology",

    # Additional focus courses sometimes offered
    "TTJ4M": "Transportation Technology - Automotive",
    "TGG4M": "Graphic Design",
    "TMV4E": "Custom Manufacturing Projects",

    # ==================================================
    # INTERDISCIPLINARY STUDIES
    # ==================================================

    "IDC4U": "Interdisciplinary Studies",

    # ==================================================
    # CO-OPERATIVE EDUCATION
    # ==================================================

    "COOP4U": "Co-operative Education",
    "COOP4M": "Co-operative Education"

}

streams = {
    "Engineering": {
        "required": [
            "ENG4U",
            "MHF4U",
            "MCV4U",
            "SCH4U",
            "SPH4U"
        ],
        "electives": [
            "SBI4U",
            "ICS4U",
            "MDM4U",
            "BOH4M",
            "BBB4M",
            "BAT4M",
            "FSF4U"
        ]
    },

    "Health Sciences": {
        "required": [
            "ENG4U",
            "MHF4U",
            "SBI4U",
            "SCH4U"
        ],
        "electives": [
            "MCV4U",
            "SPH4U",
            "MDM4U",
            "PSK4U",
            "HFA4U",
            "HHG4M",
            "HHS4U"
        ]
    },

    "Computer Science": {
        "required": [
            "ENG4U",
            "MHF4U",
            "MCV4U"
        ],
        "electives": [
            "ICS4U",
            "SPH4U",
            "SCH4U",
            "MDM4U",
            "BOH4M",
            "BBB4M"
        ]
    },

    "Business & Commerce": {
        "required": [
            "ENG4U",
            "MHF4U"
        ],
        "electives": [
            "MCV4U",
            "MDM4U",
            "BOH4M",
            "BBB4M",
            "BAT4M",
            "CIA4U",
            "CPW4U",
            "FSF4U"
        ]
    },

    "Arts & Humanities": {
        "required": [
            "ENG4U"
        ],
        "electives": [
            "HHS4U",
            "HSB4U",
            "HZT4U",
            "ADA4M",
            "AVI4M",
            "AMU4M",
            "FSF4U",
            "CHY4U"
        ]
    }
}
course_names = {

    "ENG4U": "English",
    "MHF4U": "Advanced Functions",
    "MCV4U": "Calculus and Vectors",
    "MDM4U": "Mathematics of Data Management",

    "SBI4U": "Biology",
    "SCH4U": "Chemistry",
    "SPH4U": "Physics",
    "ICS4U": "Computer Science",

    "BOH4M": "Business Leadership",
    "BBB4M": "International Business",
    "BAT4M": "Financial Accounting",

    "HFA4U": "Nutrition and Health",
    "HHG4M": "Human Development",
    "HHS4U": "Families in Canada",
    "HSB4U": "Challenge and Change in Society",
    "HZT4U": "Philosophy",

    "PSK4U": "Introductory Kinesiology",

    "ADA4M": "Drama",
    "AVI4M": "Visual Arts",
    "AMU4M": "Music",

    "CPW4U": "Canadian and World Politics",
    "CIA4U": "Economic Issues",
    "CHY4U": "World History",
    "FSF4U": "Core French"
}

ouac_deadlines = [
    {
        "deadline_date": "5-Nov-26",
        "description": "Deadline for the OUAC to receive all electronic student data files from Ontario high schools."
    },
    {
        "deadline_date": "19-Nov-26",
        "description": "Deadline for the OUAC to receive all midterm or final grades available for 4U/M courses from Ontario high schools. Schools may report in-progress grades for full-year courses as soon as they are available."
    },
    {
        "deadline_date": "26-Nov-26",
        "description": "Target date for Ontario universities to receive all midterm or final grades available for 4U/M courses from the OUAC."
    },
    {
        "deadline_date": "15-Jan-27",
        "description": "Deadline for Ontario high school students to submit their completed applications to the OUAC. The initial application includes all final grades from completed Grade 11 and 12 courses and a list of all current-year courses in progress."
    },
    {
        "deadline_date": "21-Jan-27",
        "description": "Target date for Ontario universities to receive all application data and grades from the OUAC for applications submitted by January 15, 2027."
    },
    {
        "deadline_date": "15-Jan-27",
        "description": "Target date for Ontario universities to receive all application data and grades from the OUAC for applications submitted by."
    },
    {
        "deadline_date": "11-Feb-27",
        "description": "Deadline for the OUAC to receive all final grades available for 4U/M courses and current full-year grades for 4U/M courses from Ontario high schools."
    },
    {
        "deadline_date": "18-Feb-27",
        "description": "Target date for Ontario universities to receive all final grades available for 4U/M courses and current full-year grades for 4U/M courses from the OUAC."
    },
    {
        "deadline_date": "22-Apr-27",
        "description": "Deadline for Ontario high schools to report all midterm or final grades available for 4U/M courses and interim grades for full-year courses to the OUAC."
    },
    {
        "deadline_date": "3-May-27",
        "description": "Target date for Ontario universities to receive all midterm or final grades available for 4U/M courses and interim grades for full-year courses from the OUAC."
    },
    {
        "deadline_date": "28-May-27",
        "description": "Latest date all high school applicants who submitted their application by the January application deadline can expect a response from an Ontario university, including an offer of admission, a refusal, or a deferral."
    },
    {
        "deadline_date": "1-Jun-27",
        "description": "Earliest date an Ontario high school student may be required to respond to an Ontario university offer of admission and/or provide a financial commitment (e.g., registration deposit, residence deposit)."
    },
    {
        "deadline_date": "1-Jun-27",
        "description": "All other admission-related elements, including scholarships, financial incentives, and residence offers, are considered part of the offer of admission. Universities will not compel a student to make a decision before this date."
    },
    {
        "deadline_date": "8-Jul-27",
        "description": "Deadline for the OUAC to receive all final grades for 4U/M courses from Ontario high schools."
    },
    {
        "deadline_date": "15-Jul-27",
        "description": "Target date for the OUAC to send all remaining final grades to Ontario universities."
    },
    {
        "deadline_date": "August 2 to 31, 2027",
        "description": "The OUAC collects summer school grades from Ontario high schools and school boards."
    }
]
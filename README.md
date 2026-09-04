# Ontario Admission Assitant 


## Project Overview

 

Applying to university can be stressful and confusing. Students often need to visit multiple university websites to find information about admission requirements, prerequisites, deadlines, application costs, and program details.

 

I built Ontario Admission Assistant to make this process easier. It is an AI-powered platform that helps Ontario high school students explore university options, calculate admission averages, check prerequisites, track deadlines, estimate costs, and ask admission-related questions.

 

One of the main features is an AI Admission Assistant that uses a Retrieval-Augmented Generation (RAG) system to search official university and OUAC documents before generating answers.

 

This project allowed me to learn about artificial intelligence, databases, document retrieval, and web application development while solving a real-world problem that affects students like me.

 

---

 

## Features

 

- Top 6 Average Calculator

- Prerequisite Checker

- Deadline Tracker

- Cost Calculator

- AI Admission Assistant

- Official University and OUAC Document Search

- Personalized Admission Guidance

 

---

 

## Why I Built This Project

 

As a high school student, I noticed that many students spend hours researching university admission requirements across different websites.

 

Students often ask questions such as:

 

- What average do I need?

- Do I have the required courses?

- Which programs am I eligible for?

- When are applications due?

- How much will it cost?

 

I wanted to create a single platform that could answer these questions and help students make more informed decisions about their future.

 

---

 

## Problem Statement

 

University admission information is often spread across university websites, OUAC resources, admission handbooks, and PDF documents.

 

This can make the process confusing and time-consuming for students.

 

My goal was to build a platform that combines admission tools and AI-powered guidance into one place, making it easier for students to access reliable information.

 

---

 

## How the System Works

 

[INSERT ARCHITECTURE DIAGRAM]

 

---

 

## Technologies Used

 

| Technology | Purpose |
| :--- | :--- |
| **GROQ** | AI response generation |
| **LanceDB** | Vector database |
| **LangChain** | RAG workflow and document handling |
| **OUAC Documents** | Admission information |
| **Python** | Main programming language |
| **Sentence Transformers** | Embedding generation |
| **Streamlit** | Web application interface |
| **University PDFs** | Knowledge source |
 

---



## Data Sources

 

The system uses:

 

- Official university admission documents

- Program requirement documents

- OUAC resources

- Admission requirement PDFs

- Application deadline information

 

All of these resources are PDF documents that are processed and stored in the system.

 

---

 

## AI Admission Assistant

 

The AI Admission Assistant helps students ask questions such as:

 

- What courses do I need for Engineering?

- What average is needed for Computer Science?

- What are the prerequisites for Business programs?

- What are the important application deadlines?

- Which programs match my grades?

 

The assistant retrieves relevant information from official admission documents before generating an answer.

 

---

 

## Example Use Case

 

Imagine a student named Sarah:

 

- Interested in Computer Science

- Has an 88% average

- Wants to understand admission requirements

 

Instead of visiting multiple university websites, Sarah can:

 

- Calculate her Top 6 average

- Verify prerequisites

- Review important deadlines

- Ask the AI assistant admission questions

- Receive personalized guidance

 

This helps Sarah make better admission decisions more quickly.

 

---

 

## Getting Started

 

### Requirements

 

- Python

- Streamlit

- LangChain

- LanceDB

- GROQ API Key

 

### Setup

 

1. Clone the repository.

2. Install the required dependencies.

3. Add your GROQ API key.

4. Load university and OUAC documents.

5. Run the Streamlit application.

6. Start exploring admission information.

 

---

 

## Results

 

The project successfully:

 

- Organized admission information in one platform

- Processed university and OUAC documents

- Implemented a RAG-based AI assistant

- Generated source-based admission answers

- Helped students quickly find admission information

- Demonstrated a practical educational use of AI

 

---

 

## Challenges I Faced

 

### Learning RAG

 

Understanding how document retrieval and AI generation work together was one of the most challenging parts of the project.

 

### Choosing an AI Model

 

Since this was a student project, I needed a solution that was both affordable and effective. After experimenting with different options, I chose GROQ because of its speed and free access.

 

### Improving Response Quality

 

Initially, the AI responses were not always accurate.

 

To improve this, I:

 

- Adjusted retrieval settings

- Experimented with different K values

- Refined prompts

- Tested many admission-related questions

 

### Processing Large PDF Documents

 

University admission information is usually found in large PDF files. I had to process and organize those documents so the system could quickly find relevant information when answering questions.

 

---

 

## What I Learned

 

Through this project, I learned about:

 

- Artificial Intelligence

- Retrieval-Augmented Generation (RAG)

- Vector Databases

- Document Processing

- Prompt Engineering

- Web Application Development

- Software Design

- Problem Solving

 

Most importantly, I learned that building a successful AI application involves much more than simply connecting an AI model.

 

---

 

## Future Improvements

 

If I continue developing this project, I would like to add:

 

- Scholarship recommendations

- Admission chance predictions

- More universities across Canada

- Student accounts

- Personalized dashboards

- Program recommendation features

 

---

 

## Project Demonstration

 

The demonstration shows:

 

1. Calculating a Top 6 average

2. Checking prerequisites

3. Asking questions through the AI assistant

4. RAG-powered document retrieval

5. AI-generated admission guidance

 

Video Link:

 

[INSERT YOUTUBE LINK]

 

---

 

## Final Reflection

 

This project started as an idea to make the university application process easier for students.

 

Along the way, I learned how AI systems, databases, document retrieval, and web applications work together to solve real problems.

 

The most rewarding part was building a tool that combines my interest in technology with something that could genuinely help students make important decisions about their future.

 

---

 

## Disclaimer

 

This project was developed as a Grade 12 passion project for learning purposes.

 

While the system uses official university and OUAC documents, students should always verify admission information directly with universities and OUAC before making application decisions.

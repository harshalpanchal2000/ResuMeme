import os
import streamlit as st
from crewai import Agent, Task, Crew, Process
from PyPDF2 import PdfReader
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "Your OpenAI API Key"

# Define agent roles
data_scientist = Agent(
    role='Data Scientist',
    goal='Provide personalized resume feedback for data science roles',
    backstory="You're an industry expert in data science with years of experience in resume evaluation."
)

# Define tasks
resume_feedback_task = Task(
    description='Provide personalized resume feedback',
    agent=data_scientist
)

# Define crew
resume_crew = Crew(
    agents=[data_scientist],
    tasks=[resume_feedback_task],
    process=Process.sequential
)

def get_resume_feedback(resume_path):
    # Read resume PDF
    with open(resume_path, "rb") as f:
        reader = PdfReader(f)
        resume_text = ""
        for page in reader.pages:
            resume_text += page.extract_text()
    
    # Simulate uploading resume and getting feedback
    feedback = resume_crew.kickoff(inputs={'resume_text': resume_text})
    return feedback

# Streamlit UI
st.title('ResuMeme - Attract Employers, Not Glitches!')

uploaded_file = st.file_uploader("Upload your resume (PDF format)", type="pdf")

if uploaded_file is not None:
    st.write("Resume Uploaded Successfully!")

    # Display uploaded resume
    st.subheader("Uploaded Resume")
    st.write(uploaded_file)

    # Get resume feedback
    feedback = get_resume_feedback(uploaded_file.name)

    # Display resume feedback
    st.subheader("Resume Feedback")
    st.write(feedback)

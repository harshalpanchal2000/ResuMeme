import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="ResuMeme",
    page_icon=":clipboard:",
    initial_sidebar_state="expanded"
)

# Streamlit UI
st.title('ResuMeme - Attract Employers, Not Glitches!')
st.subheader('Welcome to ResuMeme, where data meets dream jobs! ResuMeme is a unique app designed to provide personalized feedback on your current resume, specifically tailored for data science roles.')

uploaded_file = st.file_uploader("Upload your resume (PDF format)", type="pdf")

if uploaded_file is not None:
    st.write("Resume Uploaded Successfully!")

    # Display uploaded resume
    st.subheader("Uploaded Resume")
    st.write(uploaded_file)

    # Read PDF content
    resume_text = ""
    with uploaded_file:
        resume_text = uploaded_file.read().decode("utf-8")

    # Display resume content
    st.subheader("Resume Content")
    st.write(resume_text)

# Add attribution with left padding
st.markdown(
    """<div style="position: fixed; bottom: 10px; width: 100%; text-align: center;">
    <span style="padding-left: 20px;">Built by <a href="https://www.linkedin.com/in/harshal-panchal/" target="_blank">Harshal Panchal</a></span>
    </div>""",
    unsafe_allow_html=True
)

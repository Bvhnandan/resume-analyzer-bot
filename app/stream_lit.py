# app/streamlit_app.py

import os
import streamlit as st
from dotenv import load_dotenv
from utils.pdf_loader import load_resume_text
from graphs.resume_flow import build_resume_flow

# Load environment variables (.env with GROQ_API_KEY)
load_dotenv()

# Page title
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("📄 AI Resume Analyzer (Groq + LangChain + LangGraph)")

# Upload PDF
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Reading resume..."):
        # Save uploaded file temporarily
        temp_path = os.path.join("temp_resume.pdf")
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        resume_text = load_resume_text(temp_path)

    st.subheader("✅ Extracted Resume Text")
    with st.expander("View Resume Content"):
        st.write(resume_text)

    # Run LangGraph flow
    if st.button("Analyze Resume"):
        with st.spinner("Analyzing with Groq LLM..."):
            flow = build_resume_flow()
            result = flow.invoke({"resume_text": resume_text})

        # Display results
        st.success("Analysis Complete!")

        st.subheader("🔍 Extracted Information")
        st.write(result.get("parsed", "No result"))

        st.subheader("📊 Resume Score")
        st.write(result.get("score", "No result"))

        st.subheader("🛠️ Suggestions to Improve")
        st.write(result.get("suggestion", "No result"))

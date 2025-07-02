AI-Powered Resume Analyzer Bot

Hi there! 
This is a personal project I built to explore how we can use LLMs like LLaMA (via Groq) along with LangChain and LangGraph to analyze resumes smartly and provide feedback, all through a simple Streamlit interface.

What It Does

This app lets you:
- Upload your resume (PDF)
- Automatically extract important info like name, skills, education, etc.
- Score your resume’s technical strength
- Get 3 suggestions to improve your resume

All of this is powered by a multi-step LangGraph pipeline and an LLM from **Groq**, using the blazing-fast **Mixtral** model.



Tech Stack                          
 
Python - Core programming language        
Groq - LLM backend (Mixtral)            
LangChain - Prompt management              
LangGraph - To build a logical multi-step flow 
Streamlit - Simple and interactive UI       
PyPDF2 - To extract text from resume PDFs               



How to Run It Locally

1. Clone the repo
bash
git clone https://github.com/your-username/resume-analyzer-bot.git
cd resume-analyzer-bot

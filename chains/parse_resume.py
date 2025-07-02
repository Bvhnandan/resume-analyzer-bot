from base.groq_client import GroqLLM

llm = GroqLLM()

def extract_resume_info(resume_text):
    prompt = f"""
You are a resume analyzer. Extract the following:
- Name
- Email
- Education
- Skills
- Work Experience
From this resume text:\n{resume_text}
"""
    return llm.complete(prompt)

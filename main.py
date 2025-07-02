# main.py

import os
from dotenv import load_dotenv
from utils.pdf_loader import load_resume_text
from graphs.resume_flow import build_resume_flow

# Load .env variables (GROQ_API_KEY)
load_dotenv()

def main():
    # Step 1: Load resume text from PDF
    file_path = "C://COUSRE RA//Harshanandan_Resume.pdf"  # change if needed
    resume_text = load_resume_text(file_path)

    # Step 2: Run through LangGraph flow
    flow = build_resume_flow()
    result = flow.invoke({"resume_text": resume_text})

    # Step 3: Display results
    print("\n🔍 Extracted Resume Info:\n")
    print(result["parsed"])
    
    print("\n📊 Resume Score:\n")
    print(result["score"])

    print("\n🛠️ Suggestions for Improvement:\n")
    print(result["suggestion"])

if __name__ == "__main__":
    main()

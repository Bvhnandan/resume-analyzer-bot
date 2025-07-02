# graphs/resume_flow.py
from langgraph.graph import StateGraph
from base.groq_client import GroqLLM

# State = dict with keys like 'resume_text', 'parsed', 'score', 'suggestion'
def parse_resume_node(state):
    llm = GroqLLM()
    prompt = f"""
From the resume text below, extract:
- Name
- Email
- Education
- Top 5 Technical Skills
- Work Summary (2 lines)

Resume:
{state['resume_text']}
"""
    state["parsed"] = llm.complete(prompt)
    return state

def score_resume_node(state):
    llm = GroqLLM()
    prompt = f"""
Given this extracted resume info, score the technical strength from 1 to 10 and justify briefly.

Resume Info:
{state['parsed']}
"""
    state["score"] = llm.complete(prompt)
    return state

def suggest_improvements_node(state):
    llm = GroqLLM()
    prompt = f"""
Given this resume info and score, suggest 3 improvements to strengthen the candidate’s profile.

Resume Info:
{state['parsed']}
Score: {state['score']}
"""
    state["suggestion"] = llm.complete(prompt)
    return state

def build_resume_flow():
    builder = StateGraph()
    
    # Add nodes
    builder.add_node("parse_resume", parse_resume_node)
    builder.add_node("score_resume", score_resume_node)
    builder.add_node("suggest_improvements", suggest_improvements_node)

    # Connect nodes in sequence
    builder.set_entry_point("parse_resume")
    builder.add_edge("parse_resume", "score_resume")
    builder.add_edge("score_resume", "suggest_improvements")

    # Final output
    builder.set_finish_point("suggest_improvements")

    return builder.compile()

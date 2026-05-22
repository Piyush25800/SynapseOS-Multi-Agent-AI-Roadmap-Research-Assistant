# agents/planner_agent.py

from langchain_ollama import OllamaLLM


# ============================================
# LLM
# ============================================

llm = OllamaLLM(
    model="phi3",
    temperature=0.1
)


# ============================================
# CLEAN RESPONSE
# ============================================

def clean_response(text):

    # REMOVE UNWANTED WORDS
    text = text.replace("markdown", "")

    text = text.replace("```", "")

    text = text.replace("<NAME>", "")

    # REMOVE EXTRA SPACES
    text = text.replace("  ", " ")

    # REMOVE EXTRA NEWLINES
    text = text.replace("\n\n\n", "\n\n")

    return text.strip()


# ============================================
# PLANNER AGENT
# ============================================

def planner_agent(query):

    prompt = f"""
You are a professional AI Roadmap Planner Agent.

Your task:
- Create a practical roadmap
- Create month-wise learning plan
- Keep roadmap beginner friendly
- Use clear formatting
- Keep roadmap concise
- Keep roadmap realistic

STRICT RULES:
- Use markdown formatting
- Use bullet points only
- Avoid long paragraphs
- Do NOT hallucinate
- Do NOT generate fake books
- Do NOT generate fake resources
- Do NOT generate fake links
- Do NOT generate fake author names
- Use only popular trusted resources
- Keep roadmap practical
- Keep roadmap structured

Topic:
{query}

Return EXACTLY in this format:

# Month 1 — Basics

## Topics
- 
- 

## Practice
- 
- 

## Resources
- 
- 


# Month 2 — Intermediate

## Topics
- 
- 

## Practice
- 
- 

## Resources
- 
- 


# Month 3 — Advanced

## Topics
- 
- 

## Practice
- 
- 

## Resources
- 
- 


# Final Projects
- 
- 
"""


    # ============================================
    # GENERATE RESPONSE
    # ============================================

    response = llm.invoke(prompt)

    response = clean_response(response)


    # ============================================
    # STRUCTURED OUTPUT
    # ============================================

    return {
        "agent": "planner_agent",
        "status": "success",
        "query": query,
        "response": response
    }
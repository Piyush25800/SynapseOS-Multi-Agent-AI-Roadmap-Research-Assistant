# agents/research_agent.py

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

    text = text.replace("occurrth", "occurring")

    # REMOVE EXTRA SPACES
    text = text.replace("  ", " ")

    # REMOVE EXTRA NEWLINES
    text = text.replace("\n\n\n", "\n\n")

    return text.strip()


# ============================================
# RESEARCH AGENT
# ============================================

def research_agent(query):

    prompt = f"""
You are a professional AI Research Agent.

Your task:
- Explain the topic clearly
- Keep answers concise
- Use structured formatting
- Avoid long paragraphs
- Keep responses beginner friendly

STRICT RULES:
- Use markdown headings
- Use bullet points
- Do NOT hallucinate
- Do NOT generate fake information
- Do NOT generate fake books
- Do NOT generate fake citations
- Do NOT generate fake links
- Do NOT generate fake author names
- Use only well-known concepts
- Keep output clean and professional
- Keep explanations short and direct

Topic:
{query}

Return EXACTLY in this format:

# Definition
- Short clear definition

# Key Concepts
- Point 1
- Point 2
- Point 3

# Applications
- Application 1
- Application 2
- Application 3

# Important Notes
- Note 1
- Note 2
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
        "agent": "research_agent",
        "status": "success",
        "query": query,
        "response": response
    }
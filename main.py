from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="phi3")

response = llm.invoke("Explain AI agents in simple words")

print(response)
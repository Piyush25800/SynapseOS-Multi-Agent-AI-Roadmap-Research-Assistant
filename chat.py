from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

while True:

    user = input("You: ")

    response = llm.invoke(user)

    print("AI:", response)
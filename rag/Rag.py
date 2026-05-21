# rag/Rag.py

import os
import sys

# ============================================
# PROJECT PATH
# ============================================

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

# ============================================
# MEMORY
# ============================================

from memory.memory import save_memory, get_memory

# ============================================
# LANGCHAIN IMPORTS
# ============================================

from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma

from langchain_ollama import OllamaLLM


# ============================================
# LOAD PDF
# ============================================

PDF_PATH = "sample.pdf"

loader = PyPDFLoader(PDF_PATH)

docs = loader.load()


# ============================================
# TEXT SPLITTING
# ============================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

chunks = splitter.split_documents(docs)


# ============================================
# EMBEDDINGS
# ============================================

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# ============================================
# VECTOR DATABASE
# ============================================

DB_PATH = "db"

if not os.path.exists(f"{DB_PATH}/chroma.sqlite3"):

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=DB_PATH
    )

    print("\n===================================")
    print("NEW VECTOR DB CREATED")
    print("===================================\n")

else:

    vectorstore = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding
    )

    print("\n===================================")
    print("EXISTING VECTOR DB LOADED")
    print("===================================\n")


# ============================================
# LLM
# ============================================

llm = OllamaLLM(
    model="phi3"
)


# ============================================
# CLEAN RESPONSE
# ============================================

def clean_response(text):

    text = text.replace("<NAME>", "")

    text = text.replace("  ", " ")

    return text.strip()


# ============================================
# READY MESSAGE
# ============================================

print("===================================")
print("RAG SYSTEM READY")
print("Type 'exit' to stop")
print("===================================\n")


# ============================================
# MAIN LOOP
# ============================================

while True:

    query = input("Ask Question: ")

    # EXIT
    if query.lower() == "exit":
        break


    # ============================================
    # RETRIEVER
    # ============================================

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 2}
    )

    results = retriever.invoke(query)


    # ============================================
    # CONTEXT
    # ============================================

    context = "\n\n".join(
        [doc.page_content for doc in results]
    )

    # LIMIT CONTEXT
    context = context[:3000]


    # ============================================
    # DEBUG CONTEXT
    # ============================================

    print("\n===================================")
    print("RETRIEVED CONTEXT")
    print("===================================\n")

    print(context)


    # ============================================
    # PROMPT
    # ============================================

    prompt = f"""
You are a professional RAG AI Assistant.

Answer the question ONLY using the provided context.

Rules:
- Keep answers concise
- Use simple language
- Use markdown formatting
- Use bullet points
- Do NOT use outside knowledge
- Do NOT hallucinate
- Answer directly from context

Context:
{context}

Question:
{query}

Return format:

# Answer
## Definition
## Key Points
## Applications
"""


    # ============================================
    # GENERATE RESPONSE
    # ============================================

    response = llm.invoke(prompt)

    response = clean_response(response)


    # ============================================
    # PRINT RESPONSE
    # ============================================

    print("\n===================================")
    print("AI ANSWER")
    print("===================================\n")

    print(response)


    # ============================================
    # SAVE MEMORY
    # ============================================

    save_memory(query, response)


    # ============================================
    # SHOW MEMORY
    # ============================================

    print("\n===================================")
    print("MEMORY")
    print("===================================\n")

    print(get_memory())
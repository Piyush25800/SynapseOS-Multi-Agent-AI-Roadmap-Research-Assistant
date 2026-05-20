# SynapseOS — Multi-Agent AI Roadmap & Research Assistant

SynapseOS is a modular Multi-Agent AI System built using FastAPI, Ollama, LangChain, Phi-3, ChromaDB, and n8n.

The project is designed to simulate a modern AI orchestration architecture where multiple intelligent agents collaborate to generate learning roadmaps, perform contextual research, answer user queries, and automate AI-driven workflows.

Unlike traditional chatbot projects, SynapseOS focuses on:
- Multi-agent collaboration
- AI planning systems
- Workflow orchestration
- Local LLM execution
- Modular backend architecture
- Vector memory foundations
- Scalable AI infrastructure

---

## 🚀 Features

### Planner Agent
- Generates structured learning roadmaps
- Breaks goals into actionable steps
- Creates execution strategies

### Research Agent
- Answers user queries
- Performs contextual research
- Provides technical explanations

### Core System
- Multi-Agent Architecture
- FastAPI Backend APIs
- Local LLM execution using Ollama + Phi-3
- Workflow orchestration using n8n
- Modular project structure
- ChromaDB vector memory foundation
- RAG-ready architecture
- Structured API responses

---

## 🧠 Architecture

```text
User Query
    ↓
n8n Workflow
    ↓
FastAPI Backend
    ↓
Decision Routing
    ↓
┌───────────────────────────┐
│     Multi-Agent System    │
├─────────────┬─────────────┤
│ Planner     │ Research    │
│ Agent       │ Agent       │
└─────────────┴─────────────┘
    ↓
Memory + Vector Database
    ↓
Structured AI Response
```

---

## ⚙️ Tech Stack

| Component | Technology |
|---|---|
| Backend | FastAPI |
| AI Framework | LangChain |
| LLM Runtime | Ollama |
| Language Model | Phi-3 |
| Workflow Automation | n8n |
| Vector Database | ChromaDB |
| Programming Language | Python |
| Embeddings | Sentence Transformers |

---

## 📂 Project Structure

```text
SynapseOS/
│
├── agents/
│   ├── planner_agent.py
│   ├── research_agent.py
│
├── api/
│   └── server.py
│
├── memory/
│
├── rag/
│
├── db/
│
├── graph/
│
├── workflows/
│
├── requirements.txt
│
├── README.md
│
└── main.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/synapseos-multi-agent-ai.git
cd synapseos-multi-agent-ai
```

---

### Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Install Ollama

Download and install Ollama:

https://ollama.com

---

### Pull Phi-3 Model

```bash
ollama pull phi3
```

---

### Run FastAPI Server

```bash
uvicorn api.server:app --reload
```

---

### Run n8n

```bash
npx n8n
```

---

## 🔌 API Endpoints

| Endpoint | Description |
|---|---|
| `/planner` | Roadmap & planning generation |
| `/research` | Research & question answering |

---

## 💡 Example Queries

### Planner Agent

```text
Create a roadmap to learn Data Science in 6 months
```

### Research Agent

```text
Explain how Retrieval-Augmented Generation works
```

---

## 🔮 Future Improvements

- Coding Agent
- Tool calling system
- Web search integration
- Autonomous workflows
- Long-term memory
- Docker deployment
- Streaming responses
- Multi-modal support
- Parallel agent execution

---

## 📚 Learning Outcomes

This project demonstrates practical implementation of:
- Multi-Agent AI Architectures
- AI Workflow Orchestration
- Local LLM Deployment
- FastAPI Backend Engineering
- RAG Pipelines
- Vector Databases
- AI Systems Engineering

---

## 🚧 Status

Currently under active development with continuous improvements in:
- Workflow orchestration
- Memory systems
- Agent collaboration
- AI infrastructure scalability

---

## 👨‍💻 Author

Developed by Piyush Bhajikhaye

---

## 📄 License

This project is licensed under the MIT License.

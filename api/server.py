from fastapi import FastAPI

from agents.research_agent import research_agent
from agents.planner_agent import planner_agent

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "AI Research Agent Running"
    }


@app.post("/research")
def research(data: dict):

    query = data["query"]

    result = research_agent(query)

    return {
        "response": result
    }


@app.post("/planner")
def planner(data: dict):

    query = data["query"]

    result = planner_agent(query)

    return {
        "response": result
    }
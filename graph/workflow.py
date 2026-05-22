import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from typing import TypedDict

from langgraph.graph import StateGraph

from agents.research_agent import research_agent

from agents.planner_agent import planner_agent

class AgentState(TypedDict):

    input: str

    research: str

    roadmap: str

def research_node(state):

    result = research_agent(
        state["input"]
    )

    return {
        "research": result
    }

def planner_node(state):

    result = planner_agent(
        state["input"]
    )

    return {
        "roadmap": result
    }

graph = StateGraph(AgentState)

graph.add_node(
    "research",
    research_node
)

graph.add_node(
    "planner",
    planner_node
)

graph.set_entry_point(
    "research"
)

graph.add_edge(
    "research",
    "planner"
)

graph.set_finish_point(
    "planner"
)

app = graph.compile()

result = app.invoke({
    "input": "AI Engineer"
})

print(result)
from agents.research_agent import research_agent

from agents.planner_agent import planner_agent

query = input("Enter Topic: ")

print("\nRESEARCH AGENT:\n")

research = research_agent(query)

print(research)

print("\nPLANNER AGENT:\n")

plan = planner_agent(query)

print(plan)
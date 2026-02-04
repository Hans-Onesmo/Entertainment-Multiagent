from crewai import Task
from agents.preference_agent import preference_agent

preference_task = Task(
    description="Analyze the user request and extract preferences",
    agent=preference_agent,
    expected_output="Structured user preferences"
)

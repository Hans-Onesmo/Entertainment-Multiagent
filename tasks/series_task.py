from crewai import Task
from agents.series_agent import series_agent

series_task = Task(
    description="Recommend series based on extracted preferences",
    agent=series_agent,
    expected_output="Series recommendations"
)

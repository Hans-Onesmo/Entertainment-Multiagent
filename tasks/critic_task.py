from crewai import Task
from agents.critic_agent import critic_agent

critic_task = Task(
    description="Review final recommendations",
    agent=critic_agent,
    expected_output="Approved recommendations"
)

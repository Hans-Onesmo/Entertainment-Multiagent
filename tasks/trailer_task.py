from crewai import Task
from agents.trailer_agent import trailer_agent

trailer_task = Task(
    description="Provide trailers for recommended content",
    agent=trailer_agent,
    expected_output="Trailer links"
)

from crewai import Task
from agents.movie_agent import movie_agent

movie_task = Task(
    description="Recommend movies based on extracted preferences",
    agent=movie_agent,
    expected_output="Movie recommendations"
)

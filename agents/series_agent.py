from crewai import Agent

series_agent = Agent(
    role="Series Recommendation Agent",
    goal="Recommend series based on user preferences",
    backstory="TV series expert",
    verbose=True
)
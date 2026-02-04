from crewai import Agent

preference_agent = Agent(
    role="Preference Profiler",
    goal="Extract user preferences for movies and series",
    backstory="Expert in understanding entertainment taste",
    verbose=True
)
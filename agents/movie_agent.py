from crewai import Agent

movie_agent = Agent(
    role="Movie Recommendation Agent",
    goal="Recommend movies based on user preferences",
    backstory="Professional movie curator",
    verbose=True
)

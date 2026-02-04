from crewai import Agent

trailer_agent = Agent(
    role="Trailer Agent",
    goal="Find trailers for recommended content",
    backstory="Finds official trailers",
    verbose=True
)

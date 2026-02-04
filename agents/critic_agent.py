from crewai import Agent

critic_agent = Agent(
    role="Quality Reviewer",
    goal="Review recommendations for quality and diversity",
    backstory="Strict entertainment critic",
    verbose=True
)

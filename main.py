import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from crewai import Crew
from tasks.preference_task import preference_task
from tasks.movie_task import movie_task
from tasks.series_task import series_task
from tasks.trailer_task import trailer_task
from tasks.critic_task import critic_task


crew = Crew(
    tasks=[
        preference_task,
        movie_task,
        series_task,
        trailer_task,
        critic_task
    ],
    verbose=True
)

user_input = input("What do you want to watch? ")

result = crew.kickoff(
    inputs={"user_request": user_input}
)

print("\nFINAL RECOMMENDATIONS:\n")
print(result)

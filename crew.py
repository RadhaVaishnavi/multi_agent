from crewai import Crew,Process
from tools import tool_1, tool_2
from agents import research_agent, resource_agent,usecase_agent
from tasks import research_task, resource_task, usecase_task

crew= Crew(
    agents=[research_agent, resource_agent,usecase_agent],
    tasks=[research_task, resource_task, usecase_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)


result=crew.kickoff()

print("Market Research")
print("Enter company:")
inputs = {"company": input()}  # Collect company name as input
print(result)
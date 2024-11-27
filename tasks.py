from crewai import Task
from tools import tool_1,tool_2
from agents import research_agent, resource_agent,usecase_agent

research_task=Task(
    description= ("identify the industry {company} and gather relevant product information."),
    expected_output="Industry classification and product details.",
    agent=research_agent,
    tools=[tool_1,tool_2]
)

usecase_task=Task(
    description= ("Analyze industry trends and propose AI/ML use cases."),
    expected_output="ist of proposed AI/ML use cases.",
    agent=usecase_agent,
    tools=[tool_1]
)

resource_task=Task(
    description= ("Find datasets related to usecases from Kaggle or GitHub."),
    expected_output="Links to relevant datasets and GitHub resources.",
    agent=usecase_agent,
    tools=[tool_1,tool_2]
)




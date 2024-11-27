from crewai import Agent
from tools import tool_1
from tools import tool_2
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"

research_agent=Agent(
    role='Researcher',
    goal='Identify the industry of the company{company} and gather relevant information.',
    verbose=True,
    memory=True,
    backstory=("You are a research expert who can analyze web data to determine industry classification."),
    tools=[tool_1,tool_2],
    allow_delegation=True,
    llm=llm
)

usecase_agent=Agent(
    role='usecase generator',
    goal='Analyze industry trends and propose relevant AI/ML use cases for the company{company}.',
    verbose=True,
    memory=True,
    backstory=("You are an analyst skilled in identifying usecases for AI and ML applications in various industries"),
    tools=[tool_1],
    allow_delegation=True,
    llm=llm
)

resource_agent=Agent(
    role='resource generator',
    goal='Search and provide relevant datasets, github links, and resources to support the proposed use cases for the{company}.',
    verbose=True,
    memory=True,
    backstory=("You are an expert in curating datasets and finding online resources that help in executing AI and ML solutions."),
    tools=[tool_1, tool_2],
    allow_delegation=True,
    llm=llm
)

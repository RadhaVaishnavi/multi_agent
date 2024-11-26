from crewai import Agent
from langchain_openai import ChatOpenAI
import os

class MarketResearchAgents:

    def __init__(self):
        # OpenAI Models
        self.gpt4 = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.7)

    def research_agent(self):
        return Agent(
            role='Research Agent',
            goal='Identify the industry of the company and gather relevant product information.',
            backstory="You are a research expert who can analyze web data to determine industry classification.",
            verbose=True,
            allow_delegation=False,
            llm=self.gpt4,
            max_iter=3,
        )

    def use_case_agent(self):
        return Agent(
            role='Use Case Agent',
            goal='Analyze industry trends and propose relevant AI/ML use cases for the company.',
            backstory="You are an analyst skilled in identifying opportunities for AI and ML applications in various industries.",
            verbose=True,
            allow_delegation=False,
            llm=self.gpt4,
            max_iter=3,
        )

    def resource_agent(self):
        return Agent(
            role='Resource Agent',
            goal='Collect datasets related to proposed use cases from various platforms.',
            backstory="You are a resource expert who can find and summarize relevant datasets for AI applications.",
            verbose=True,
            allow_delegation=False,
            llm=self.gpt4,
            max_iter=3,
        )

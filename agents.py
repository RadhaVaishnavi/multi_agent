from crewai import Agent
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import os
from crewai_tools import SerperDevTool, WebsiteSearchTool, ScrapeWebsiteTool

class MarketResearchAgents:

    def __init__(self):
        # Initialize tools if needed
        self.serper = SerperDevTool()
        self.web = WebsiteSearchTool()
        self.web_scrape = ScrapeWebsiteTool()

        # OpenAI Models
        self.gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.gpt4 = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.7)

        # Select the model to use
        self.selected_llm = self.gpt4

    def research_agent(self):
        return Agent(
            role='Research Agent',
            goal='Identify the industry of the company and gather relevant product information.',
            backstory="You are a research expert who can analyze web data to determine industry classification.",
            verbose=True,
            allow_delegation=False,
            llm=self.selected_llm,
            tools=[self.serper, self.web, self.web_scrape],
            max_iter=3,
        )

    def use_case_agent(self):
        return Agent(
            role='Use Case Agent',
            goal='Analyze industry trends and propose relevant AI/ML use cases for the company.',
            backstory="You are an analyst skilled in identifying opportunities for AI and ML applications in various industries.",
            verbose=True,
            allow_delegation=False,
            llm=self.selected_llm,
            max_iter=3,
        )

    def resource_agent(self):
        return Agent(
            role='Resource Agent',
            goal='Collect datasets related to proposed use cases from various platforms.',
            backstory="You are a resource expert who can find and summarize relevant datasets for AI applications.",
            verbose=True,
            allow_delegation=False,
            llm=self.selected_llm,
            tools=[self.serper, self.web],
            max_iter=3,
        )

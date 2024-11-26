from crewai import Agent
from langchain_openai import ChatOpenAI  # Using GPT-4 model from OpenAI
from crewai_tools import SerperDevTool, WebsiteSearchTool, ScrapeWebsiteTool
import os


class MarketResearchCrewAgents:

    def __init__(self):
        # Initialize tools
        self.serper = SerperDevTool()
        self.web = WebsiteSearchTool()
        self.web_scrape = ScrapeWebsiteTool()

        # OpenAI Models
        self.gpt4 = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.7)

        # Set the selected model for the agent
        self.selected_llm = self.gpt4

    def researcher(self):
        # Researcher agent for gathering company and industry-related insights
        return Agent(
            role='Researcher',
            goal='Identify the industry of the company and gather relevant product and vision information for the sector.',
            backstory="You are a highly skilled researcher who can break down company information and relate it to industry trends.",
            verbose=True,
            allow_delegation=False,
            llm=self.selected_llm,
            max_iter=3,
            tools=[self.serper, self.web, self.web_scrape]
        )

    def use_case_expert(self):
        # Use case agent for analyzing AI, ML, and automation trends and proposing relevant use cases
        return Agent(
            role='Use Case Expert',
            goal='Analyze the industry trends and propose AI/ML use cases that can improve the company’s processes.',
            backstory="You are an AI and ML expert, skilled in identifying cutting-edge solutions for improving business operations.",
            verbose=True,
            allow_delegation=False,
            llm=self.selected_llm,
            max_iter=3
        )

    def resource_expert(self):
        # Resource agent for finding relevant datasets and resources
        return Agent(
            role='Resource Expert',
            goal='Search and provide relevant datasets, articles, and resources to support the proposed use cases.',
            backstory="You are an expert in curating datasets and finding online resources that help in executing AI and ML solutions.",
            verbose=True,
            allow_delegation=False,
            llm=self.selected_llm,
            max_iter=3,
            tools=[self.serper, self.web, self.web_scrape]
        )

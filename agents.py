from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool,WebsiteSearchTool, ScrapeWebsiteTool 
class MarketResearchAgents:

    def __init__(self):
        # OpenAI Models
        self.gpt4 = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.7)
        self.serper = SerperDevTool()
        self.web = WebsiteSearchTool()
        self.web_scrape=ScrapeWebsiteTool()
        
    def research_agent(self):
        return Agent(
            role='Research Agent',
            goal='Identify the industry of the company and gather relevant product information.',
            backstory="You are a research expert who can analyze web data to determine industry classification.",
            verbose=True,
            allow_delegation=False,
            llm=self.gpt4,
            max_iter=3,
            tools=[self.serper, self.web, self.web_scrape],
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
            tools=[self.serper, self.web, self.web_scrape],
        )
        
    def resource_agent(self):
        return Agent(
            role='resource agent',
            goal='Search and provide relevant datasets, github links, and resources to support the proposed use cases.',
            backstory="You are an expert in curating datasets and finding online resources that help in executing AI and ML solutions.",
            verbose=True,
            allow_delegation=False,
            llm=self.gpt4,
            max_iter=3,
            tools=[self.serper, self.web, self.web_scrape]
        )

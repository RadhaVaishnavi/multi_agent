from crewai import Crew, Process
from tasks import MarketResearchTasks
from agents import MarketResearchAgents

from decouple import config
from textwrap import dedent
import os

class MarketResearchApplication:
    def __init__(self, inputs):
        self.inputs = inputs
        self.tasks = MarketResearchTasks()
        self.agents = MarketResearchAgents()

    def run(self):
        # Define agents
        research_agent = self.agents.research_agent()
        use_case_agent = self.agents.use_case_agent()
        resource_agent = self.agents.resource_agent()


        # Create tasks
        research_task = self.tasks.research_task(research_agent, self.inputs)
        use_case_task = self.tasks.use_case_task(use_case_agent, [research_task])
        resource_task = self.tasks.resource_task(resource_agent, [use_case_task], self.inputs)

        # Form the crew
        crew = Crew(
            agents=[research_agent, use_case_agent, resource_agent],
            tasks=[research_task, use_case_task, resource_task],
            process=Process.sequential,
        )

        # Execute and return results
        result = crew.kickoff()

        # Map results for structured output
        return {
            "Industry": result[research_task],
            "Suggested Use Cases": result[use_case_task],
            "Suggested Resources": result[resource_task],
        }

if __name__ == "__main__":
    print("Welcome to the Market Research Assistant!")
    company_name = input("Enter the company's name: ")

    inputs = {"company_name": company_name}
    market_research_agent = MarketResearchAgents(inputs)
    result = market_research_agent.run()

    print("\n## Results:")
    print(f"Industry: {result['Industry']}")
    print("Suggested Use Cases:")
    for use_case in result["Suggested Use Cases"]:
        print(f"- {use_case}")
    print("Suggested Resources:")
    for resource in result["Suggested Resources"]:
        print(f"- {resource}")

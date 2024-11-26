import os
from crewai import Crew, Process
from agents import MarketResearchCrewAgents
from tasks import MarketResearchCrewTasks

class MarketResearchCrew:
    def __init__(self, inputs):
        self.inputs = inputs
        self.agents = MarketResearchCrewAgents()
        self.tasks = MarketResearchCrewTasks()

    def run(self):
        # Initialize agents
        researcher = self.agents.researcher()
        use_case_expert = self.agents.use_case_expert()
        resource_expert = self.agents.resource_expert()

        # Initialize tasks with respective agents
        research_task = self.tasks.research_task(researcher, self.inputs)
        use_case_task = self.tasks.use_case_task(use_case_expert, [research_task])
        resource_task = self.tasks.resource_task(resource_expert, [use_case_task])

        # Form the crew with defined agents and tasks
        crew = Crew(
            agents=[researcher, use_case_expert, resource_expert],
            tasks=[research_task, use_case_task, resource_task],
            process=Process.sequential
        )

        # Execute the crew to carry out the market research project
        return crew.kickoff()

if __name__ == "__main__":
    print("Welcome to the Market Research Crew Setup")
    print("-------------------------------------------")
    company_name = input("Please enter the company's name: ")
    industry_name = input("Optional: Enter the industry name (or leave blank): ")

    inputs = f"Company Name: {company_name}\nIndustry Name: {industry_name if industry_name else 'Unknown'}"
    research_crew = MarketResearchCrew(inputs)
    result = research_crew.run()

    print("\n\n##############################")
    print("## Here are the results of your market research project:")
    print("##############################\n")
    print(result)

import os
from crewai import Crew, Process
from agents import MarketResearchAgents
from tasks import MarketResearchTasks

class MarketResearchCrew:
    def __init__(self, inputs):
        self.inputs = inputs
        self.agents = MarketResearchAgents()
        self.tasks = MarketResearchTasks()

    def run(self):
        # Initialize agents
        research_agent = self.agents.research_agent()
        use_case_agent = self.agents.use_case_agent()
        resource_agent = self.agents.resource_agent()

        # Initialize tasks with respective agents
        research_task = self.tasks.research_task(research_agent, self.inputs)
        analysis_task = self.tasks.analysis_task(use_case_agent, [research_task])
        writing_task = self.tasks.writing_task(resource_agent, [analysis_task], self.inputs)

        # Form the crew with defined agents and tasks
        crew = Crew(
            agents=[research_agent, use_case_agent, resource_agent],
            tasks=[research_task, analysis_task, writing_task],
            process=Process.sequential
        )

        # Execute the crew to carry out the research project
        return crew.kickoff()

if __name__ == "__main__":
    print("Welcome to the Market Research Crew Setup")
    print("---------------------------------------")
    company_name = input("Please enter the company's name: ")
    
    inputs = f"Company Name: {company_name}"
    market_research_crew = MarketResearchCrew(inputs)
    result = market_research_crew.run()

    print("\n\n##############################")
    print("## Here are the results of your market research:")
    print("##############################\n")
    print(result)

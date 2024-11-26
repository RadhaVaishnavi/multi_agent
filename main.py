from crewai import Crew, Process
from textwrap import dedent

from agents import MarketResearchAgents
from tasks import MarketResearchTasks

class MarketResearchAgents:
    def __init__(self, inputs):
        self.inputs = inputs
        self.agents = MarketResearchAgents()
        self.tasks = MarketResearchTasks()

    def run(self):
        research_agent = self.agents.research_agent()
        use_case_agent = self.agents.use_case_agent()
        resource_agent = self.agents.resource_agent()

 # Initialize tasks with respective agents
        research_task = self.tasks.research_task(researcher, self.inputs)
        use_case_task = self.tasks.use_case_task(analyst, [research_task])
        resource_task = self.tasks.resource_task(writer, [analysis_task],self.inputs)

# Form the crew with defined agents and tasks
        crew = Crew(
            agents=[research_agent, use_case_agent, resource_agent],
            tasks=[research_task, use_case_task, resource_task],
            process=Process.sequential
        )

        # Execute the crew to carry out the research project
        return crew.kickoff()

if __name__ == "__main__":
    print("Welcome to the Market Research ")
    company_name = input("Please enter the company's name: ")
    
    inputs = f"Company Name: {company_name}"
    market_research_agent = MarketResearchAgents(inputs)
    result = market_research_agent.run()
    print("## Here are the results of your market research:")
    print(result)

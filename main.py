from crewai import Crew, Process
from textwrap import dedent

from agents import MarketResearchCrew
from tasks import MarketResearchTasks

class MarketResearchCrew:
    def __init__(self, inputs):
        self.inputs = inputs
        self.agents = MarketResearchAgents()

    def run(self):
        # Simulating results without database interaction
        industry = "Technology" if "tech" in self.inputs.lower() else "General"
        use_cases = ["AI-driven customer support", "Predictive maintenance", "Data analytics"]

        return {
            "Industry": industry,
            "Suggested Use Cases": use_cases
        }

if __name__ == "__main__":
    print("Welcome to the Market Research Crew Setup")
    company_name = input("Please enter the company's name: ")
    
    inputs = f"Company Name: {company_name}"
    market_research_crew = MarketResearchCrew(inputs)
    result = market_research_crew.run()

    print("\n\n##############################")
    print("## Here are the results of your market research:")
    print("##############################\n")
    print(result)

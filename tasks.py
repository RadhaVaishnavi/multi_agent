from crewai import Task

class MarketResearchTasks:

    def research_task(self, agent, inputs):
      return Task(
          agent=agent,
          description=f"Identify the industry of {inputs} and gather relevant product information.",
          expected_output=f"Industry classification and product information."
      )

    def analysis_task(self, agent, context):
      return Task(
          agent=agent,
          context=context,
          description="Analyze industry trends and propose relevant AI/ML use cases.",
          expected_output=f"List of proposed AI/ML use cases based on industry trends."
      )

    def writing_task(self, agent, context, inputs):
      return Task(
          agent=agent,
          context=context,
          description=f"Find datasets related to proposed use cases from platforms like Kaggle or GitHub.",
          expected_output=f"Links to relevant datasets and github."
      )

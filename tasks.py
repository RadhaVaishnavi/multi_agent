from crewai import Task

class MarketResearchTasks:
    def research_task(self, agent, inputs):
        return Task(
            agent=agent,
            description=f"Identify the industry for {inputs['company_name']} and gather relevant product information.",
            expected_output="Industry classification and product details.",
        )

    def use_case_task(self, agent, context):
        return Task(
            agent=agent,
            context=context,
            description="Analyze industry trends and propose AI/ML use cases.",
            expected_output="List of proposed AI/ML use cases.",
        )

    def resource_task(self, agent, context, inputs):
        return Task(
            agent=agent,
            context=context,
            description=f"Find datasets related to {inputs['company_name']} from Kaggle or GitHub.",
            expected_output="Links to relevant datasets and GitHub resources.",
        )

from crewai import Task

class MarketResearchCrewTasks:

    def research_task(self, agent, inputs):
        return Task(
            agent=agent,
            description=f"Using the company information {inputs}, figure out the industry the company belongs to and gather vision and product information for the sector.",
            expected_output="A detailed report that includes the company's industry, vision, and product information."
        )

    def use_case_task(self, agent, context):
        return Task(
            agent=agent,
            context=context,
            description=f"Based on the research report {context}, analyze industry trends, and propose AI, ML, or automation use cases that the company could adopt.",
            expected_output="A list of relevant use cases where AI, ML, and automation could be applied to improve business operations."
        )

    def resource_task(self, agent, context):
        return Task(
            agent=agent,
            context=context,
            description=f"Given the proposed use cases {context}, search for relevant datasets, articles, and other resources to support the implementation of these use cases.",
            expected_output="A curated list of datasets, articles, and resources with links that can be used to implement the proposed AI/ML use cases."
        )

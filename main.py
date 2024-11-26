from agents import ResearchAgent, UseCaseAgent, ResourceAgent

def run_research(company_name):
    research_agent = ResearchAgent(company_name)
    research_result = research_agent.run()

    use_case_agent = UseCaseAgent(research_result)
    use_case_result = use_case_agent.run()

    resource_agent = ResourceAgent(use_case_result)
    resource_result = resource_agent.run()

    return research_result, use_case_result, resource_result

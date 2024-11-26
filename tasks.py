# tasks.py
from agents import ResearchAgent, UseCaseAgent, ResourceAgent

def perform_research(company_name):
    research_agent = ResearchAgent()
    industry, vision, product_info = research_agent.get_industry_info(company_name)
    
    use_case_agent = UseCaseAgent()
    use_cases = use_case_agent.generate_use_cases(industry)
    
    resource_agent = ResourceAgent()
    resources = []
    for use_case in use_cases:
        resources.append({
            "use_case": use_case,
            "datasets": resource_agent.fetch_datasets(use_case)
        })
    
    return {
        "industry": industry,
        "vision": vision,
        "product_info": product_info,
        "use_cases": use_cases,
        "resources": resources
    }

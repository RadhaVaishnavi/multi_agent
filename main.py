from agents import ResearchAgent, UseCaseAgent, ResourceAgent

def main(company_name):
    research_agent = ResearchAgent(company_name)
    industry = research_agent.scrape_industry_info()
    
    use_case_agent = UseCaseAgent()
    use_cases = use_case_agent.analyze_trends(industry)
    
    resource_agent = ResourceAgent()
    datasets = resource_agent.find_datasets(use_cases)
    
    print(f"Industry: {industry}")
    print(f"Use Cases: {use_cases}")
    print("Datasets:")
    for dataset in datasets:
        print(dataset)

if __name__ == "__main__":
    company_name = input("Enter the company's name: ")
    main(company_name)

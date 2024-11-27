class UseCaseAgent:
    def __init__(self, company_name, industry):
        self.company_name = company_name
        self.industry = industry
        self.use_cases = {
            "healthcare": ["Disease Prediction", "Medical Image Analysis", "Patient Monitoring"],
            "finance": ["Fraud Detection", "Risk Assessment", "Algorithmic Trading"],
            "retail": ["Inventory Management", "Personalized Recommendations", "Customer Sentiment Analysis"]
        }

    def suggest_use_cases(self):
        # Suggest use cases based on the industry
        return self.use_cases.get(self.industry, ["General Business Automation"])

# Example usage:
company_name = "Tesla"
industry = "automotive"
use_case_agent = UseCaseAgent(company_name, industry)
use_cases = use_case_agent.suggest_use_cases()
print("Suggested Use Cases:", use_cases)

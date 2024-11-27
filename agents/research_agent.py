import requests

class ResearchAgent:
    def __init__(self, company_name):
        self.company_name = company_name
        self.api_url = f"https://en.wikipedia.org/w/api.php"
    
    def get_company_info(self):
        params = {
            "action": "query",
            "format": "json",
            "titles": self.company_name,
            "prop": "extracts",
            "exintro": True,
            "explaintext": True
        }

        try:
            response = requests.get(self.api_url, params=params)
            data = response.json()
            pages = data['query']['pages']
            page_id = list(pages.keys())[0]
            extract = pages[page_id].get('extract', 'No information available')
            return extract
        except Exception as e:
            return f"Error fetching company info: {e}"

# Example usage:
company = "Tesla"
research_agent = ResearchAgent(company)
company_info = research_agent.get_company_info()
print(company_info)

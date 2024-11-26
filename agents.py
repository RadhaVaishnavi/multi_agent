from crewai import Agent
import requests
from bs4 import BeautifulSoup
import openai

class ResearchAgent(Agent):
    def __init__(self, inputs):
        self.inputs = inputs

    def run(self):
        # Extract company name
        company_name = self.inputs
        industry = self.get_industry_from_web(company_name)
        vision_and_product = self.get_industry_vision_and_products(industry)

        return {"industry": industry, "vision_and_product": vision_and_product}

    def get_industry_from_web(self, company_name):
        # Example of scraping logic to find the company's industry
        search_query = f"{company_name} industry"
        response = requests.get(f"https://www.google.com/search?q={search_query}")
        soup = BeautifulSoup(response.text, 'html.parser')

        # Simplified scraping - Ideally, this should be more complex
        industry = soup.find('div', {'class': 'BNeawe iBp4i AP7Wnd'}).text
        return industry

    def get_industry_vision_and_products(self, industry):
        # Example for providing vision and products based on industry
        industry_vision = {
            "Automotive": "Innovative vehicles with AI-based safety features.",
            "Healthcare": "Improving patient care with AI-powered diagnostics.",
        }
        return industry_vision.get(industry, "No vision found for this industry.")


class UseCaseAgent(Agent):
    def __init__(self, inputs):
        self.inputs = inputs

    def run(self):
        industry = self.inputs["industry"]
        use_cases = self.generate_use_cases_for_industry(industry)
        return {"use_cases": use_cases}

    def generate_use_cases_for_industry(self, industry):
        # Use GPT-4 to generate use cases based on industry
        prompt = f"Generate AI, ML, and automation use cases for the {industry} industry."
        response = openai.Completion.create(
            model="gpt-4",
            prompt=prompt,
            max_tokens=300,
            temperature=0.7
        )
        return response.choices[0].text.strip()


class ResourceAgent(Agent):
    def __init__(self, inputs):
        self.inputs = inputs

    def run(self):
        use_cases = self.inputs["use_cases"]
        resource_links = self.find_relevant_resources(use_cases)
        return {"resource_links": resource_links}

    def find_relevant_resources(self, use_cases):
        # Search for relevant datasets related to use cases on Kaggle, HuggingFace, GitHub
        # In practice, we would use APIs for these platforms. Below is a simplified example
        links = {
            "Kaggle": f"https://www.kaggle.com/search?q={use_cases.replace(' ', '+')}",
            "HuggingFace": f"https://huggingface.co/datasets?search={use_cases.replace(' ', '+')}",
            "GitHub": f"https://github.com/search?q={use_cases.replace(' ', '+')}"
        }
        return links

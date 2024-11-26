import requests
from bs4 import BeautifulSoup

def fetch_industry_info(company_name):
    """Fetch the industry and vision/product information for the company."""
    industry = None
    industry_url = f"https://www.google.com/search?q={company_name}+industry"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(industry_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        industry_results = soup.find_all('h3')  # Find the industry-related info
        if industry_results:
            industry = industry_results[0].text  # Assuming first result mentions industry

    if not industry:
        return {"error": "Industry info not found."}

    # Now, fetch vision and product information
    vision_url = f"https://www.google.com/search?q={company_name}+vision+product"
    response = requests.get(vision_url, headers=headers)
    vision_and_product = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        vision_results = soup.find_all('h3')  # Find the vision and product-related info
        vision_and_product = [result.text for result in vision_results[:5]]  # Top 5 vision/product descriptions

    return {"industry": industry, "vision_and_product": vision_and_product}


import requests
from bs4 import BeautifulSoup

def fetch_company_info(company_name):
    """
    Scrape the web to determine the industry and focus areas of the given company.
    """
    search_url = f"https://www.google.com/search?q={company_name}+industry"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the most relevant snippet for industry (improve logic as needed)
    snippets = soup.find_all("span")
    industry = "Not Found"
    for snippet in snippets:
        text = snippet.get_text().lower()
        if "industry" in text or "sector" in text:
            industry = text
            break

    return industry

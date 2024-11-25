# agents/research_agent.py

import requests
from bs4 import BeautifulSoup

def fetch_industry_and_offerings(company_name):
    """
    Fetch industry and strategic focus areas of a company via web scraping.
    """
    search_query = f"{company_name} industry and key offerings"
    url = f"https://www.google.com/search?q={search_query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None, None  # Handle failed requests
    
    soup = BeautifulSoup(response.text, "html.parser")
    snippets = soup.find_all("span", class_="BNeawe")
    
    industry, offerings = None, None
    for snippet in snippets:
        text = snippet.get_text()
        if "industry" in text.lower():
            industry = text
        if "key offerings" in text.lower() or "focus areas" in text.lower():
            offerings = text
        if industry and offerings:
            break
    
    return industry, offerings

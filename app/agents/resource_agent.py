# agents/resource_agent.py

import requests
from bs4 import BeautifulSoup

def find_relevant_resources(use_case):
    """
    Search for relevant datasets or pre-trained models for a given use case.
    """
    search_query = f"Kaggle dataset or HuggingFace model for {use_case}"
    url = f"https://www.google.com/search?q={search_query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    links = [a["href"] for a in soup.find_all("a", href=True) if "kaggle.com" in a["href"] or "huggingface.co" in a["href"]]

    return links

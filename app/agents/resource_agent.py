import requests
from bs4 import BeautifulSoup

def search_datasets(use_case):
    """Search for relevant datasets on Kaggle, HuggingFace, and GitHub."""
    
    # Search query to find pharmaceutical/healthcare-related resources
    query = use_case.replace(" ", "+")
    
    # Scraping Kaggle datasets (using a Google search workaround)
    kaggle_search_url = f"https://www.kaggle.com/search?q={query}"
    kaggle_page = requests.get(kaggle_search_url)
    kaggle_soup = BeautifulSoup(kaggle_page.text, 'html.parser')
    
    kaggle_links = []
    for link in kaggle_soup.find_all('a', {'class': 'sc-fzqImN iWLkxf'}):
        kaggle_links.append("https://www.kaggle.com" + link.get('href'))

    # Scraping HuggingFace datasets (direct search page)
    huggingface_search_url = f"https://huggingface.co/datasets?search={query}"
    huggingface_page = requests.get(huggingface_search_url)
    huggingface_soup = BeautifulSoup(huggingface_page.text, 'html.parser')

    huggingface_links = []
    for link in huggingface_soup.find_all('a', {'class': 'sc-hGpYNS jzMsmO'}):
        huggingface_links.append("https://huggingface.co" + link.get('href'))

    # Scraping GitHub repositories (direct search)
    github_search_url = f"https://github.com/search?q={query}"
    github_page = requests.get(github_search_url)
    github_soup = BeautifulSoup(github_page.text, 'html.parser')

    github_links = []
    for link in github_soup.find_all('a', {'class': 'v-align-middle'}):
        github_links.append("https://github.com" + link.get('href'))

    # Return the gathered links
    return {
        "Kaggle": kaggle_links[:5],  # Limit to 5 results
        "HuggingFace": huggingface_links[:5],  # Limit to 5 results
        "GitHub": github_links[:5]  # Limit to 5 results
    }

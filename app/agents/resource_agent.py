import requests
from bs4 import BeautifulSoup

def search_datasets(use_case):
    """Search for datasets on Kaggle, HuggingFace, and GitHub based on the use case."""
    
    search_urls = {
        "Kaggle": f"https://www.kaggle.com/search?q={use_case.replace(' ', '+')}",
        "HuggingFace": f"https://huggingface.co/datasets?search={use_case.replace(' ', '+')}",
        "GitHub": f"https://github.com/search?q={use_case.replace(' ', '+')}"
    }
    
    dataset_links = {
        "Kaggle": [],
        "HuggingFace": [],
        "GitHub": []
    }

    # Fetch Kaggle datasets
    response_kaggle = requests.get(search_urls["Kaggle"])
    if response_kaggle.status_code == 200:
        soup_kaggle = BeautifulSoup(response_kaggle.text, 'html.parser')
        kaggle_results = soup_kaggle.find_all('a', {'class': 'sc-kAzzGY'})
        dataset_links["Kaggle"] = [f"https://www.kaggle.com{result['href']}" for result in kaggle_results[:5]]

    # Fetch HuggingFace datasets
    response_huggingface = requests.get(search_urls["HuggingFace"])
    if response_huggingface.status_code == 200:
        soup_huggingface = BeautifulSoup(response_huggingface.text, 'html.parser')
        huggingface_results = soup_huggingface.find_all('a', {'class': 'dataset-link'})
        dataset_links["HuggingFace"] = [f"https://huggingface.co{result['href']}" for result in huggingface_results[:5]]

    # Fetch GitHub repositories
    response_github = requests.get(search_urls["GitHub"])
    if response_github.status_code == 200:
        soup_github = BeautifulSoup(response_github.text, 'html.parser')
        github_results = soup_github.find_all('a', {'class': 'v-align-middle'})
        dataset_links["GitHub"] = [f"https://github.com{result['href']}" for result in github_results[:5]]

    return dataset_links

def collect_resources(use_cases):
    """Collect resource links for each use case."""
    resources = {}
    for use_case in use_cases:
        resources[use_case] = search_datasets(use_case)
    return resources

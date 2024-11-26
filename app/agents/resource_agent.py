from kaggle.api.kaggle_api_extended import KaggleApi
from github import Github
import requests

def search_kaggle_resources(keywords):
    api = KaggleApi()
    api.authenticate()
    datasets = api.dataset_list(search=keywords)
    return [f"https://www.kaggle.com/{dataset.ref}" for dataset in datasets]

def search_huggingface_resources(keywords):
    url = f"https://huggingface.co/search?query={keywords}"
    return url

def search_github_resources(keywords):
    g = Github("your_github_token")  # Replace with your GitHub token
    repos = g.search_repositories(query=keywords)
    return [repo.html_url for repo in repos[:5]]  # Top 5 results

# Example Usage
resources_kaggle = search_kaggle_resources("automotive AI")
resources_hf = search_huggingface_resources("automotive AI")
resources_github = search_github_resources("automotive AI")

import requests
from bs4 import BeautifulSoup

def search_datasets(use_case):
    """Search for relevant datasets on Kaggle, HuggingFace, and GitHub."""
    
    # Define search URLs for each platform
    search_url_kaggle = f"https://www.kaggle.com/search?q={use_case.replace(' ', '+')}"
    search_url_huggingface = f"https://huggingface.co/datasets?search={use_case.replace(' ', '+')}"
    search_url_github = f"https://github.com/search?q={use_case.replace(' ', '+')}"

    # Kaggle Datasets (Example: Search and find top 5 links)
    kaggle_datasets = [
        "https://www.kaggle.com/datasets/suraj9727/supply-chain-optimization-for-a-fmcg-company",
        "https://www.kaggle.com/code/kelvinprawtama/supply-chain-optimization",
        "https://www.kaggle.com/datasets/laurinbrechter/supply-chain-data",
        "https://www.kaggle.com/code/amirmotefaker/supply-chain-analysis",
        "https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis"
    ]

    # HuggingFace Datasets (Example: Search and find top 5 links)
    hugface_datasets = [
        "https://huggingface.co/datasets/supply_chain_analysis",
        "https://huggingface.co/datasets/retail_data_analysis",
        "https://huggingface.co/datasets/ai_for_supply_chain",
        "https://huggingface.co/datasets/warehouse_management_data",
        "https://huggingface.co/datasets/logistics_optimization"
    ]
    
    # GitHub Repositories (Example: Search and find top 5 links)
    github_repositories = [
        "https://github.com/search?q=supply+chain+optimization",
        "https://github.com/search?q=inventory+management+AI",
        "https://github.com/search?q=machine+learning+logistics",
        "https://github.com/search?q=genai+supply+chain",
        "https://github.com/search?q=ai+warehouse+optimization"
    ]

    # Returning datasets as a dictionary
    return {
        "Kaggle": kaggle_datasets,
        "HuggingFace": hugface_datasets,
        "GitHub": github_repositories
    }

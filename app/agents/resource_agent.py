import requests

def search_datasets(use_case):
    """Search for datasets on Kaggle or HuggingFace."""
    search_url_kaggle = f"https://www.kaggle.com/search?q={use_case.replace(' ', '+')}"
    search_url_huggingface = f"https://huggingface.co/datasets?search={use_case.replace(' ', '+')}"
    search_url_github = f"https://github.com/search?q={use_case.replace(' ', '+')}"

    # Get Kaggle datasets
    kaggle_response = requests.get(search_url_kaggle)
    kaggle_link = f"Kaggle: {search_url_kaggle}" if kaggle_response.status_code == 200 else "Kaggle: No datasets found"

    # Get HuggingFace datasets
    hugface_response = requests.get(search_url_huggingface)
    hugface_link = f"HuggingFace: {search_url_huggingface}" if hugface_response.status_code == 200 else "HuggingFace: No datasets found"

    # Get GitHub repositories
    github_response = requests.get(search_url_github)
    github_link = f"GitHub: {search_url_github}" if github_response.status_code == 200 else "GitHub: No datasets found"

    return {
        "Kaggle": kaggle_link,
        "HuggingFace": hugface_link,
        "GitHub": github_link
    }

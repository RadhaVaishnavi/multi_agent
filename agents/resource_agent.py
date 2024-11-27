import requests

def search_datasets(use_case):
    search_url_kaggle = f"https://www.kaggle.com/datasets?search={use_case}"
    search_url_huggingface = f"https://huggingface.co/datasets?search={use_case}"
    search_url_github = f"https://github.com/search?q={use_case}+dataset"

    datasets = []
    
    # Search on Kaggle
    response_kaggle = requests.get(search_url_kaggle)
    if response_kaggle.status_code == 200:
        datasets.append({"platform": "Kaggle", "link": search_url_kaggle})

    # Search on HuggingFace
    response_huggingface = requests.get(search_url_huggingface)
    if response_huggingface.status_code == 200:
        datasets.append({"platform": "HuggingFace", "link": search_url_huggingface})

    # Search on GitHub
    response_github = requests.get(search_url_github)
    if response_github.status_code == 200:
        datasets.append({"platform": "GitHub", "link": search_url_github})
    
    return datasets

def save_datasets_to_file(datasets, filename="datasets.md"):
    with open(filename, "w") as file:
        for dataset in datasets:
            file.write(f"**{dataset['platform']}**: [Dataset Link]({dataset['link']})\n")

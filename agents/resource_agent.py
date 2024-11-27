import requests

def search_datasets(use_case):
    search_url = f"https://huggingface.co/datasets?search={use_case}"
    response = requests.get(search_url)
    # Logic to parse response and extract clickable dataset links
    datasets = parse_datasets(response.text)
    return datasets

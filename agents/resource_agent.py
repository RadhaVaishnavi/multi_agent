import requests

def search_datasets(use_cases):
    # Search for datasets based on use cases (this is a simplified example)
    search_query = '+'.join(use_cases.split())
    datasets = {
        "Kaggle": f"https://www.kaggle.com/datasets?search={search_query}",
        "HuggingFace": f"https://huggingface.co/datasets?search={search_query}",
        "GitHub": f"https://github.com/search?q={search_query}+dataset"
    }
    return datasets

def save_datasets_to_file(datasets):
    # Save datasets to a markdown file
    with open('datasets.md', 'w') as file:
        file.write("# Relevant Datasets\n\n")
        for platform, link in datasets.items():
            file.write(f"- [{platform}]({link})\n")

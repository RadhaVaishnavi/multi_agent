import requests
from bs4 import BeautifulSoup

def search_datasets(use_case):
    """
    Search for relevant datasets related to the given use case on platforms like Kaggle, Hugging Face, and GitHub.
    """
    datasets = []

    # Search on Kaggle
    kaggle_search_url = f"https://www.kaggle.com/search?q={use_case.replace(' ', '+')}"
    response = requests.get(kaggle_search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    kaggle_links = soup.find_all('a', {'class': 'sc-ifAKCX jIjCOJ'})  # Update with actual class for Kaggle links
    for link in kaggle_links:
        datasets.append(f"- [Kaggle]({link.get('href')})")

    # Search on Hugging Face
    huggingface_search_url = f"https://huggingface.co/datasets?search={use_case.replace(' ', '+')}"
    response = requests.get(huggingface_search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    huggingface_links = soup.find_all('a', {'class': 'link link-primary'})  # Update with actual class for Hugging Face links
    for link in huggingface_links:
        datasets.append(f"- [Hugging Face]({link.get('href')})")

    # Search on GitHub
    github_search_url = f"https://github.com/search?q={use_case.replace(' ', '+')}+dataset"
    response = requests.get(github_search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    github_links = soup.find_all('a', {'class': 'v-align-middle'})  # Update with actual class for GitHub links
    for link in github_links:
        datasets.append(f"- [GitHub]({link.get('href')})")

    return datasets

def format_output(company_name, industry, use_cases, datasets):
    """
    Format the output with company info, use cases, and clickable dataset links.
    """
    # Create formatted output
    formatted_output = f"Company Name: {company_name}\n"
    formatted_output += f"Industry Overview: {industry}\n\n"
    
    # Add Use Cases
    for idx, use_case in enumerate(use_cases, 1):
        formatted_output += f"Use Case {idx}: {use_case['title']}\n"
        formatted_output += f"AI Application: {use_case['application']}\n"
        formatted_output += "Cross-Functional Benefits:\n"
        for benefit in use_case['benefits']:
            formatted_output += f"- {benefit['team']}: {benefit['description']}\n"
        formatted_output += "\n"

    # Add Dataset Links
    formatted_output += "Dataset Links:\n"
    for dataset in datasets:
        formatted_output += f"{dataset}\n"
    
    return formatted_output

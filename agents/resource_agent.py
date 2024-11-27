import requests

class ResourceAgent:
    def __init__(self):
        self.kaggle_url = "https://www.kaggle.com/datasets"
        self.huggingface_url = "https://huggingface.co/datasets"
        self.github_url = "https://github.com/search?q=dataset"
    
    def get_kaggle_datasets(self, search_term):
        return f"{self.kaggle_url}?search={search_term}"
    
    def get_huggingface_datasets(self, search_term):
        return f"{self.huggingface_url}?search={search_term}"
    
    def get_github_datasets(self, search_term):
        return f"{self.github_url}+dataset"

    def collect_relevant_datasets(self, search_term):
        datasets = {
            "Kaggle": self.get_kaggle_datasets(search_term),
            "HuggingFace": self.get_huggingface_datasets(search_term),
            "GitHub": self.get_github_datasets(search_term)
        }
        return datasets

# Example usage:
resource_agent = ResourceAgent()
search_term = "AI healthcare"
datasets = resource_agent.collect_relevant_datasets(search_term)
print("Relevant Datasets:", datasets)

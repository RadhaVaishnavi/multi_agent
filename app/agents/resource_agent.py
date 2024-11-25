import requests

def collect_resources(keywords):
    """
    Search for relevant datasets on platforms like Kaggle and Hugging Face.
    """
    kaggle_url = f"https://www.kaggle.com/search?q={keywords}"
    huggingface_url = f"https://huggingface.co/datasets?q={keywords}"

    resources = {
        "Kaggle": kaggle_url,
        "Hugging Face": huggingface_url,
    }
    return resources

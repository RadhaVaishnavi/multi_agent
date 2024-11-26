import requests
from bs4 import BeautifulSoup
from transformers import pipeline

def classify_industry(company_name):
    # Scrape data (example: LinkedIn or Crunchbase)
    query = f"{company_name} industry"
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example classification (improve with ML model later)
    if "automobile" in soup.text.lower():
        industry = "Automotive"
    else:
        industry = "Unknown"
    
    return industry

def fetch_vision_and_product_info(company_name):
    # Use web scraping or GPT-based API to summarize information
    url = f"https://www.example.com/{company_name}"  # Replace with actual logic
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    text = soup.text[:5000]  # Extract main content



summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(input_text):
    # Dynamically adjust max_length based on the input length
    input_length = len(input_text.split())
    max_length = min(100, input_length)  # Set max_length based on input size
    min_length = max(25, input_length // 2)  # Ensure summary is at least half the input size

    # Generate summary with adjusted max_length
    summary = summarizer(input_text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary

# Example usage
input_text = "Your input text goes here."
summary = summarize_text(input_text)

# Display the result
print(summary)



# Example Usage
industry = classify_industry("Tesla")
vision_info = fetch_vision_and_product_info("Tesla")

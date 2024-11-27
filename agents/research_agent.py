import wikipediaapi
import requests
from bs4 import BeautifulSoup

def get_company_info(company_name):
    # Using Wikipedia API for company information
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(company_name)
    
    if not page.exists():
        return "Industry and Product Info Not Found"
    
    text = page.text
    
    # Extract industry and key offerings from the text (you can refine this with regex)
    industry = "Not found"
    product_info = "Not found"
    
    if "industry" in text.lower():
        industry_start = text.lower().find("industry")
        industry_end = text[industry_start:].find(".")
        industry = text[industry_start:industry_start + industry_end].strip()
    
    if "product" in text.lower():
        product_start = text.lower().find("product")
        product_end = text[product_start:].find(".")
        product_info = text[product_start:product_start + product_end].strip()
    
    return industry, product_info

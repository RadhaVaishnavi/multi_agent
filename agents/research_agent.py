import requests
from bs4 import BeautifulSoup

def get_industry_and_product(company_name):
    url = f"https://www.google.com/search?q={company_name}+industry"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None, None

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Modify these selectors based on the actual HTML structure
    industry_element = soup.find('div', {'class': 'industry-class'})
    product_info_element = soup.find('div', {'class': 'product-class'})
    
    industry = industry_element.text if industry_element else 'Industry not found'
    product_info = product_info_element.text if product_info_element else 'Product info not found'
    
    return industry, product_info

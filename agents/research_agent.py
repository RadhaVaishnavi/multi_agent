import wikipediaapi

def get_company_info(company_name):
    # Set up Wikipedia API with a user-agent string
    wiki_wiki = wikipediaapi.Wikipedia(
        'en',
        user_agent="YourAppName/1.0 (your_email@example.com)"  # Replace with your app name and contact info
    )
    
    page = wiki_wiki.page(company_name)
    
    if not page.exists():
        return "Industry not found", "Product info not found"
    
    industry = "Industry info not found"  # Default value if industry isn't found
    product_info = "Product info not found"  # Default value if product info isn't found
    
    # Try extracting the information
    if 'industry' in page.text.lower():
        industry = "Extracted industry info here"  # Add your extraction logic or scrape for industry data
    if 'product' in page.text.lower():
        product_info = "Extracted product info here"  # Add your extraction logic or scrape for product data
    
    return industry, product_info

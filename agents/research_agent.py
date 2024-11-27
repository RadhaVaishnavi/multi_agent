import requests
from bs4 import BeautifulSoup

def get_company_info(company_name):
    # Create a search query for Google to find the company info
    search_url = f"https://www.google.com/search?q={company_name}+industry+and+product+info"
    
    # Send GET request to Google search
    response = requests.get(search_url, headers={"User-Agent": "Mozilla/5.0"})
    
    # If the request is successful
    if response.status_code == 200:
        # Parse the HTML response using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Try to extract some useful info from the Google search results
        try:
            # Extract first search result snippet for industry info (simple fallback approach)
            snippet = soup.find('div', class_='BNeawe iBp4i AP7Wnd')
            industry_info = snippet.text if snippet else "Industry info not found"
            
            # You can further refine this logic to extract product information
            product_info = "Product info not found"  # Placeholder, add your custom logic
            
            return industry_info, product_info
        except Exception as e:
            print(f"Error extracting data: {e}")
            return "Industry not found", "Product info not found"
    else:
        return "Error during web scraping", "Error during web scraping"

# Example usage
company_name = "Tesla"
industry, product_info = get_company_info(company_name)
print(f"Industry: {industry}")
print(f"Product Info: {product_info}")

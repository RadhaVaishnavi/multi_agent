import wikipediaapi

def get_company_info(company_name):
    try:
        # Set up Wikipedia API with a user-agent string
        wiki_wiki = wikipediaapi.Wikipedia(
            'en',  # Language code
            user_agent="YourAppName/1.0 (your_email@example.com)"  # Replace with your app details
        )
        
        # Fetch page from Wikipedia
        page = wiki_wiki.page(company_name)
        
        # Check if the page exists
        if not page.exists():
            return "Industry info not found", "Product info not found"
        
        # Extract summary and return as product info
        summary = page.summary.split('\n')[0]  # Only the first paragraph
        industry = "Industry info not found"  # This is a placeholder for now
        product_info = summary
        return industry, product_info
    except Exception as e:
        return f"Error fetching company info: {e}", f"Error: {e}"

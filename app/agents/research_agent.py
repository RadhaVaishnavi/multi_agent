import requests
from bs4 import BeautifulSoup

def get_company_industry(company_name):
    """
    Scrapes Wikipedia to fetch the industry/sector of a company based on its name.
    """
    # Replace spaces in the company name with underscores for Wikipedia URL format
    company_name_wiki = company_name.replace(" ", "_")
    
    # Wikipedia URL for the company
    url = f"https://en.wikipedia.org/wiki/{company_name_wiki}"
    
    # Send a GET request to the Wikipedia page
    response = requests.get(url)
    
    if response.status_code != 200:
        return "Industry information not found on Wikipedia."
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Search for the infobox table that contains company details
    infobox = soup.find('table', {'class': 'infobox'})

    if infobox:
        # Try to find the "Industry" field in the infobox
        rows = infobox.find_all('tr')
        for row in rows:
            th = row.find('th')
            td = row.find('td')

            if th and td:
                if 'Industry' in th.text:
                    # Extract the industry/sector value
                    industry = td.text.strip()
                    return industry
    return "Industry information not found."

from research_agent import get_company_industry
from use_case_agent import generate_use_cases
from resource_agent import search_datasets, format_output

def fetch_industry_and_use_cases(company_name):
    """
    Fetch the industry and generate use cases for the given company name.
    """
    # Scrape the industry for the company
    industry = get_company_industry(company_name)

    # Generate use cases based on the industry
    use_cases = generate_use_cases(industry)

    return industry, use_cases

def generate_use_case(company_name):
    """
    Generate use cases and dataset links for the company based on the company name.
    """
    # Fetch industry and use cases
    industry, use_cases = fetch_industry_and_use_cases(company_name)

    # Search for relevant datasets based on use cases
    datasets = []
    for use_case in use_cases:
        datasets.extend(search_datasets(use_case["title"]))

    # Format the final output
    final_output = format_output(company_name, industry, use_cases, datasets)

    return final_output


# Example usage
company_name = input("Enter the company name: ")

# Generate use cases and dataset links for the given company
output = generate_use_case(company_name)

# Print the final formatted output
print(output)

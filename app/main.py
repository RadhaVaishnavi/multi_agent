import streamlit as st
from agents.research_agent import fetch_industry_info, fetch_company_info
from agents.use_case_agent import generate_use_cases
from agents.resource_agent import collect_resources

st.title("AI/GenAI Market Research & Use Case Generator")

# Input fields
company_name = st.text_input("Enter the Company Name (Required):")
industry_name = st.text_input("Enter the Industry Name (Optional):")

if st.button("Generate Insights"):
    if company_name:
        # Fetch company data
        company_info = fetch_company_info(company_name)
        st.subheader(f"{company_name} Company Offerings")
        st.write(company_info)
        
        # If industry name is not provided, fetch industry info based on company
        if not industry_name:
            industry_info = fetch_industry_info(company_name)  # Update to search industry based on company name
            st.subheader("Industry Insights")
            st.write(industry_info)
        else:
            # If industry name is provided, fetch info for the specified industry
            industry_info = fetch_industry_info(industry_name)
            st.subheader(f"Insights for {industry_name} Industry")
            st.write(industry_info)
        
        # Generate AI/GenAI Use Cases
        use_cases = generate_use_cases(industry_name or company_name, industry_info['insights'])
        st.subheader("AI/GenAI Use Cases")
        for use_case in use_cases:
            st.write(f"- {use_case}")
        
        # Collect resources
        st.subheader("Relevant Datasets & Tools")
        resources = collect_resources(use_cases)
        for use_case, link in resources.items():
            st.write(f"{use_case}: [Dataset Link]({link})")
    else:
        st.error("Company Name is required!")

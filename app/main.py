import sys
import os

print("Python Paths:", sys.path)  # Debugging: Check available paths
print("Current Directory:", os.getcwd())  # Debugging: Check where the app runs from
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from agents.research_agent import fetch_industry_info, fetch_company_info
from agents.use_case_agent import generate_use_cases
from agents.resource_agent import collect_resources

st.title("AI/GenAI Market Research & Use Case Generator")

# Input fields
industry_name = st.text_input("Enter the Industry Name (e.g., Retail, Healthcare):")
company_name = st.text_input("Enter the Company Name (optional):")

if st.button("Generate Insights"):
    # Fetch industry and company data
    industry_info = fetch_industry_info(industry_name)
    st.subheader("Industry Insights")
    if "error" in industry_info:
        st.error(industry_info["error"])
    else:
        st.write(industry_info)

    if company_name:
        company_info = fetch_company_info(company_name)
        st.subheader("Company Offerings")
        if "error" in company_info:
            st.error(company_info["error"])
        else:
            st.write(company_info)

    # Generate AI use cases
    if "insights" in industry_info:
        use_cases = generate_use_cases(industry_name, industry_info['insights'])
        st.subheader("AI/GenAI Use Cases")
        st.write(use_cases)

        # Collect resources
        st.subheader("Relevant Datasets & Tools")
        resources = collect_resources([use_cases])
        for use_case, link in resources.items():
            st.write(f"{use_case}: {link}")

import streamlit as st
from agents.research_agent import fetch_company_info
from agents.use_case_agent import generate_use_cases
from agents.resource_agent import collect_resources

# Streamlit UI
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
        
        # Generate AI/GenAI Use Cases
        use_cases = generate_use_cases(company_info)
        st.subheader("AI/GenAI Use Cases")
        for use_case in use_cases:
            st.write(f"- {use_case}")
        
        # Collect resources
        st.subheader("Relevant Datasets & Tools")
        resources = collect_resources(use_cases)
        for resource in resources:
            st.write(f"- {resource}")
    else:
        st.error("Company Name is required!")

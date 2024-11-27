import streamlit as st
from agents.research_agent import get_company_info
from agents.use_case_agent import generate_use_cases
from agents.resource_agent import search_datasets, save_datasets_to_file

# Streamlit input for company name
company_name = st.text_input("Enter Company Name:")

if company_name:
    # Research Agent
    industry, product_info = get_company_info(company_name)
    st.write(f"Industry: {industry}")
    st.write(f"Product Info: {product_info}")
    
    # Use Case Agent
    use_cases = generate_use_cases(industry)
    st.write("Proposed Use Cases:")
    st.write(use_cases)
    
    # Resource Agent
    datasets = search_datasets(use_cases)
    st.write("Relevant Datasets:")
    st.write(datasets)
    
    # Saving datasets to markdown file
    save_datasets_to_file(datasets)

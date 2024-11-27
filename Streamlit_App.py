import streamlit as st
from agents.research_agent import get_industry_and_product
from agents.use_case_agent import analyze_use_cases
from agents.resource_agent import search_datasets

st.title("Market Research AI Model")

company_name = st.text_input("Enter Company Name:")

if company_name:
    # Research Agent
    industry, product_info = get_industry_and_product(company_name)
    st.write(f"Industry: {industry}")
    st.write(f"Product Info: {product_info}")
    
    # Use Case Agent
    if industry != 'Industry not found':
        use_cases = analyze_use_cases(industry)
        st.write(f"Suggested Use Cases: {use_cases}")
    
        # Resource Agent
        datasets = search_datasets(use_cases)
        st.write("Relevant Datasets:")
        for dataset in datasets:
            st.markdown(f"[{dataset['name']}]({dataset['link']})")
    else:
        st.write("Could not determine the industry or product info for this company.")

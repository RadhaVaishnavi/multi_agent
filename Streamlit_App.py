import streamlit as st
from agents.research_agent import get_industry_and_product
from agents.use_case_agent import analyze_use_cases
from agents.resource_agent import search_datasets

st.title("Market Research AI Model")

company_name = st.text_input("Enter Company Name:")
if company_name:
    industry, product_info = get_industry_and_product(company_name)
    use_cases = analyze_use_cases(industry)
    datasets = search_datasets(use_cases)
    
    st.write(f"Industry: {industry}")
    st.write(f"Product Info: {product_info}")
    st.write(f"Suggested Use Cases: {use_cases}")
    for dataset in datasets:
        st.markdown(f"[{dataset['name']}]({dataset['link']})")

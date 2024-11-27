import streamlit as st
from agents.research_agent import get_company_info
from agents.use_case_agent import generate_use_cases
from agents.resource_agent import search_datasets, save_datasets_to_file

st.title("AI & GenAI Use Case Generation for Companies")

company_name = st.text_input("Enter Company Name:")

if company_name:
    # Research Agent
    industry, product_info = get_company_info(company_name)
    st.write(f"Industry: {industry}")
    st.write(f"Product Info: {product_info}")
    
    if industry != 'Industry and Product Info Not Found':
        # Market Standards & Use Case Generation Agent
        use_cases = generate_use_cases(industry)
        st.write(f"Proposed Use Cases: {use_cases}")
    
        # Resource Asset Collection Agent
        datasets = search_datasets(use_cases)
        st.write("Relevant Datasets:")
        for dataset in datasets:
            st.markdown(f"[{dataset['platform']}]({dataset['link']})")
        
        # Optional: Save the dataset links to a file
        save_datasets_to_file(datasets)
        st.write("Dataset links have been saved to a markdown file.")
    else:
        st.write("Could not determine the industry or product info for this company.")

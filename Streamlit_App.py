import streamlit as st
from research_agent import ResearchAgent
from usecase_agent import UseCaseAgent
from resource_agent import ResourceAgent

# Title for the Streamlit app
st.title("Market Research Agent")

# Inputs
company_name = st.text_input("Enter company name:")
industry = st.selectbox("Select Industry", ["healthcare", "finance", "retail", "automotive"])

# Create the agents
research_agent = ResearchAgent(company_name)
use_case_agent = UseCaseAgent(company_name, industry)
resource_agent = ResourceAgent()

# Get and display company information
if company_name:
    company_info = research_agent.get_company_info()
    st.subheader("Company Analysis")
    st.write(company_info)

    # Get and display use cases
    use_cases = use_case_agent.suggest_use_cases()
    st.subheader("Proposed Use Cases")
    st.write(use_cases)

    # Get and display relevant datasets
    search_term = industry  # You can refine this based on the use case
    datasets = resource_agent.collect_relevant_datasets(search_term)
    st.subheader("Relevant Datasets")
    st.write(datasets)


import streamlit as st
from agents.research_agent import fetch_company_info
from agents.use_case_agent import generate_use_cases
from agents.resource_agent import collect_resources

st.title("AI/GenAI Market Research & Use Case Generator")

# Input: Company name
company_name = st.text_input("Enter the company name:")

if st.button("Generate"):
    if company_name:
        # Fetch company info and industry
        industry = fetch_company_info(company_name)
        focus_areas = "Customer Experience, Operations, Supply Chain"  # Example placeholder

        st.write(f"**Company Name:** {company_name}")
        st.write(f"**Industry:** {industry}")

        # Generate use cases
        use_cases = generate_use_cases(industry, focus_areas)
        st.write("### AI/GenAI Use Cases")
        st.write(use_cases)

        # Collect resource links
        resources = collect_resources(f"{industry} AI datasets")
        st.write("### Relevant Datasets")
        for platform, link in resources.items():
            st.markdown(f"- [{platform}]({link})")
    else:
        st.error("Please enter a company name!")

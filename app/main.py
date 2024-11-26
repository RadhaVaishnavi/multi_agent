import streamlit as st
from agents.research_agent import fetch_industry_info
from agents.use_case_agent import generate_use_cases
from agents.resource_agent import search_datasets

# Streamlit app setup
st.title("AI/GenAI Use Cases for Hetero Healthcare")

# Input fields
company_name = st.text_input("Enter Company Name:")
industry_name = st.text_input("Enter Industry Name (optional):")

if st.button("Generate Insights"):
    if company_name:
        # Fetch industry and company data
        industry_info = fetch_industry_info(company_name)
        st.subheader("Industry Insights")
        st.write(industry_info)

        # Generate AI use cases based on industry info
        use_cases = generate_use_cases(industry_info["industry"], industry_info["vision_and_product"])
        st.subheader("AI/GenAI Use Cases")
        st.write(use_cases)

        # Collect resource links for the generated use cases
        st.subheader("Relevant Datasets & Tools")
        resources = search_datasets(use_cases)
        for resource_platform, resource_links in resources.items():
            st.write(f"{resource_platform} Datasets:")
            for link in resource_links:
                st.write(f"[{link}]({link})")
    else:
        st.warning("Please enter a company name to generate insights.")

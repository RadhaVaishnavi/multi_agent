import streamlit as st
from agents.research_agent import classify_industry, fetch_vision_and_product_info
from agents.use_case_agent import generate_use_cases
from agents.resource_agent import search_kaggle_resources, search_huggingface_resources, search_github_resources

# Streamlit App
st.title("Market Research Model")
st.write("Enter a company's name to analyze its industry, generate AI/ML use cases, and find relevant resources.")

# Input Form
company_name = st.text_input("Company Name", placeholder="e.g., Tesla")

if st.button("Analyze"):
    if not company_name.strip():
        st.error("Please enter a valid company name.")
    else:
        # Research Agent
        try:
            st.subheader("Step 1: Industry Classification")
            industry = classify_industry(company_name)
            st.write(f"**Identified Industry:** {industry}")

            st.subheader("Step 2: Vision and Product Information")
            vision_info = fetch_vision_and_product_info(company_name)
            st.write(f"**Vision & Product Information:** {vision_info}")
        except Exception as e:
            st.error(f"Error in Research Agent: {e}")

        # Use Case Agent
        try:
            st.subheader("Step 3: Proposed AI/ML Use Cases")
            use_cases = generate_use_cases(industry)
            for idx, use_case in enumerate(use_cases, start=1):
                st.write(f"{idx}. {use_case}")
        except Exception as e:
            st.error(f"Error in Use Case Agent: {e}")

        # Resource Agent
        try:
            st.subheader("Step 4: Relevant Resources")
            st.write("### Kaggle Resources:")
            kaggle_links = search_kaggle_resources(industry)
            for link in kaggle_links:
                st.write(f"- [Dataset Link]({link})")

            st.write("### Hugging Face Resources:")
            hf_link = search_huggingface_resources(industry)
            st.write(f"- [Search Results]({hf_link})")

            st.write("### GitHub Resources:")
            github_links = search_github_resources(industry)
            for link in github_links:
                st.write(f"- [Repository Link]({link})")
        except Exception as e:
            st.error(f"Error in Resource Agent: {e}")

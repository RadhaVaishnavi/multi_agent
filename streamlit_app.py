import streamlit as st
from main import run_research

st.title('Market Research Assistant')

company_name = st.text_input("Enter Company Name")

if st.button('Run Research'):
    if company_name:
        # Run the research process
        research_result, use_case_result, resource_result = run_research(company_name)

        # Display the results
        st.subheader("Industry & Vision Info")
        st.write(research_result)

        st.subheader("Proposed Use Cases")
        st.write(use_case_result["use_cases"])

        st.subheader("Relevant Resources")
        st.write("Kaggle: ", resource_result["resource_links"]["Kaggle"])
        st.write("HuggingFace: ", resource_result["resource_links"]["HuggingFace"])
        st.write("GitHub: ", resource_result["resource_links"]["GitHub"])
    else:
        st.error("Please enter a company name.")

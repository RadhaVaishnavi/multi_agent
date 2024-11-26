# main.py
import streamlit as st
from tasks import perform_research

def main():
    st.title("Market Research Model")

    # Input section
    company_name = st.text_input("Enter Company Name:")

    if company_name:
        st.write(f"Performing research for: {company_name}")
        
        # Call the task to perform research
        results = perform_research(company_name)

        # Display the results
        st.header(f"Industry: {results['industry']}")
        st.subheader("Vision and Product Info:")
        st.write(f"Vision: {results['vision']}")
        st.write(f"Product Info: {results['product_info']}")

        st.header("Proposed Use Cases")
        for use_case in results['use_cases']:
            st.write(f"- {use_case}")

        st.header("Relevant Datasets")
        for resource in results['resources']:
            st.write(f"Use Case: {resource['use_case']}")
            for dataset in resource['datasets']:
                st.markdown(f"- [{dataset}]({dataset})")

if __name__ == "__main__":
    main()

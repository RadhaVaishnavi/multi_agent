# app/main.py

import streamlit as st
from agents.research_agent import fetch_industry_and_offerings
from agents.use_case_agent import generate_use_cases
from agents.resource_agent import find_relevant_resources

st.title("Market Research & Use Case Generator")

company_name = st.text_input("Enter Company Name", "Google")
industry, offerings = fetch_industry_and_offerings(company_name)

if not industry:
    st.warning("Industry could not be fetched. Please enter manually.")
    industry = st.text_input("Industry", "")
else:
    st.success(f"Identified Industry: {industry}")

insights = st.text_area("Enter Insights about the Industry", "AI is transforming industries globally.")

if st.button("Generate Use Cases"):
    if industry:
        use_cases = generate_use_cases(industry, insights)
        st.text_area("Generated Use Cases", value=use_cases, height=400)
    else:
        st.error("Industry information is required.")

if st.button("Find Resources"):
    for use_case in use_cases.split("\n\n"):
        resources = find_relevant_resources(use_case)
        st.write(f"Resources for '{use_case}':")
        for resource in resources:
            st.markdown(f"- [{resource}]({resource})")

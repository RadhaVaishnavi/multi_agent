import streamlit as st
from main import main

st.title("Market Research Model")
company_name = st.text_input("Enter the company's name:")

if st.button("Analyze"):
    if company_name:
        results = main(company_name)
        st.write(results)
    else:
        st.error("Please enter a company name.")

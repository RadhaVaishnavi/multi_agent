import streamlit as st
from main import MarketResearchCrew  # Import the MarketResearchCrew class from main.py

st.title('Market Research Assistant')

with st.sidebar:
    st.header('Enter Company Details')
    company_name = st.text_input("Company Name:")

if st.button('Run Research'):
    if not company_name:
        st.error("Please enter a company name.")
    else:
        inputs = f"Company Name: {company_name}"
        market_research_crew = MarketResearchCrew(inputs)
        result = market_research_crew.run()
        
        st.subheader("Results of your market research:")
        st.write(result)

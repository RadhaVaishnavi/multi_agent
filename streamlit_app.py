import streamlit as st
from main import MarketResearchAgents

st.title("Market Research Assistant")

company_name = st.text_input("Enter the company's name:")
if st.button("Analyze"):
    if company_name:
        inputs = f"Company Name: {company_name}"
        market_research_agent = MarketResearchAgents(inputs)
        result = market_research_agent.run()
        
        st.subheader("Results:")
        st.write(f"**Industry:** {result['Industry']}")
        st.write("**Suggested Use Cases:**")
        for use_case in result["Suggested Use Cases"]:
            st.write(f"- {use_case}")
    else:
        st.error("Please enter a company name.")

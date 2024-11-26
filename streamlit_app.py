import streamlit as st
from main import MarketResearchAgents
import os

st.title("Market Research agent")

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
os.environ["SERPER_API_KEY"] = st.secrets["SERPER_API_KEY"]


# Get company name input
company_name = st.text_input("Enter the company's name:")

if st.button("Analyze"):
    if company_name:
        # Prepare inputs
        inputs = {"company_name": company_name}
        
        # Run the Market Research Agents
        market_research_agent = MarketResearchAgents(inputs)
        result = market_research_agent.run()

        # Display results
        st.subheader("Results:")
        st.write(f"**Industry:** {result['Industry']}")
        
        st.write("**Suggested Use Cases:**")
        for use_case in result["Suggested Use Cases"]:
            st.write(f"- {use_case}")
        
        st.write("**Suggested Resources:**")
        for resource in result["Suggested Resources"]:
            st.write(f"- {resource}")
    else:
        st.error("Please enter a company name.")

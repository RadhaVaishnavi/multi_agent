from langchain.agents import initialize_agent
from langchain.tools import DuckDuckGoSearchResults
from langchain.agents import Tool
from langchain.agents import AgentExecutor

# Define tools
search = DuckDuckGoSearchResults()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Search the web for relevant information"
    ),
]

# Initialize agent
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description")

def fetch_company_info(company_name):
    result = agent.run(company_name)
    return result

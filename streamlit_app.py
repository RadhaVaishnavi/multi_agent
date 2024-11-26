import streamlit as st
from main import ResearchCrew, UseCaseAgent, ResourceAgent  # Import agents from main.py
from transformers import GPT4LMHeadModel, GPT4Tokenizer
import torch

# Load the GPT-4 model and tokenizer (ensure this is locally available)
model_name = "gpt-4"  # Replace with the exact model name
tokenizer = GPT4Tokenizer.from_pretrained(model_name)
model = GPT4LMHeadModel.from_pretrained(model_name)

# Set Streamlit UI
st.title('Your Research Assistant')

# Collect user inputs for research
with st.sidebar:
    st.header('Enter Research Details')
    topic = st.text_input("Main topic of your research:")
    detailed_questions = st.text_area("Specific questions or subtopics you are interested in exploring:")

# Function to use GPT-4 for generating responses
def generate_response(inputs: str) -> str:
    input_ids = tokenizer.encode(inputs, return_tensors="pt")
    
    with torch.no_grad():
        output = model.generate(input_ids, max_length=500, num_return_sequences=1)
    
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# Run the research
if st.button('Run Research'):
    if not topic or not detailed_questions:
        st.error("Please fill all the fields.")
    else:
        inputs = f"Research Topic: {topic}\nDetailed Questions: {detailed_questions}"
        
        # Now integrate your agents into the app
        research_agent = ResearchCrew(inputs)
        research_results = research_agent.run()

        # Use the UseCaseAgent to analyze potential use cases (example)
        use_case_agent = UseCaseAgent(inputs)
        use_case_results = use_case_agent.analyze_use_cases()

        # Use the ResourceAgent to find relevant resources
        resource_agent = ResourceAgent(use_case_results)
        resource_results = resource_agent.find_resources()

        # Combine all results and use GPT-4 for a final response
        gpt_input = f"Research Results: {research_results}\nUse Case Analysis: {use_case_results}\nResources Found: {resource_results}"
        final_response = generate_response(gpt_input)

        # Display the results
        st.subheader("Results of your research project:")
        st.write(final_response)

import streamlit as st
from agents.research_agent import classify_industry, fetch_vision_and_product_info
from agents.use_case_agent import generate_use_cases
from agents.resource_agent import search_kaggle_resources, search_huggingface_resources, search_github_resources


# Load the model and tokenizer once to save time
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2-large")
    model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2-large")
    return tokenizer, model

# Generate use cases for a given industry
@st.cache_data
def generate_industry_use_cases(industry, tokenizer, model):
    prompt = f"Propose AI/ML use cases for a company in the {industry} industry."
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(inputs["input_ids"], max_length=150, num_return_sequences=1)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Main app
def main():
    st.title("Market Research AI Tool")

    # Input field for company name
    company_name = st.text_input("Enter the company name:")

    if st.button("Analyze"):
        if not company_name.strip():
            st.error("Please enter a valid company name.")
            return

        try:
            # Step 1: Research Agent
            st.subheader("Step 1: Industry Classification")
            industry = classify_industry(company_name)
            st.write(f"**Identified Industry:** {industry}")

            st.subheader("Step 2: Vision and Product Information")
            vision_info = fetch_vision_and_product_info(company_name)
            st.write(f"**Vision & Product Information:** {vision_info}")

        except Exception as e:
            st.error(f"Error in Research Agent: {e}")
            return

        # Step 2: Use Case Agent (only proceed if industry is classified)
        if industry:
            tokenizer, model = load_model()
            try:
                st.subheader("Step 3: Proposed AI/ML Use Cases")
                use_cases = generate_industry_use_cases(industry, tokenizer, model)
                st.write(f"**Proposed Use Cases for {industry}:**\n{use_cases}")
            except Exception as e:
                st.error(f"Error in Use Case Agent: {e}")

        # Step 3: Resource Agent (only proceed if industry is classified)
        if industry:
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

if __name__ == "__main__":
    main()

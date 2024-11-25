from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the GPT-Neo model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")
model.config.pad_token_id = tokenizer.eos_token_id  # Set pad token if not already set

def generate_use_cases(company_name):
    """
    Generate AI/GenAI use cases for a given company using GPT-Neo.
    """
    # Web-scraped or pre-determined industry overview
    industry_overview = f"The company {company_name} operates in the cutting-edge industry of technology and innovation. They are a leader in electric vehicles, autonomous driving, renewable energy, and AI advancements."

    # Prompt definition
    prompt = (
        f"Company Name: {company_name}\n"
        f"Industry Overview: {industry_overview}\n\n"
        "Generate AI/GenAI use cases for this company. Each use case should be structured as follows:\n"
        "Use Case: [Title]\n"
        "AI Application: [Detailed description]\n"
        "Cross-Functional Benefit: [List benefits across teams/functions]\n\n"
        "Provide clear and structured output."
    )

    # Tokenize the prompt
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
    
    # Generate response
    outputs = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=500,
        num_return_sequences=1,
        do_sample=True,
        top_k=50,
        top_p=0.9,
        temperature=0.7
    )

    # Decode and clean up the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response_cleaned = ' '.join(response.split()).replace(prompt, "").strip()  # Remove excess spaces and keep only the generated content
    return response_cleaned

# Example usage
company_name = "Tesla"
use_cases = generate_use_cases(company_name)
print(use_cases)

from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st

# Load Hugging Face model (GPT-2 for simplicity)
tokenizer = AutoTokenizer.from_pretrained("gpt2")  
model = AutoModelForCausalLM.from_pretrained("gpt2")

def generate_use_cases(industry_name, insights):
    """
    Generate AI/GenAI use cases using GPT-2 model and ensure proper formatting.
    The use case will include AI application and cross-functional benefits.
    """
    prompt = (
        f"Generate structured AI/GenAI use cases for the {industry_name} industry based on the following insights:\n"
        f"{insights}\n\n"
        "Each use case should follow this format:\n"
        "Use Case: [Title]\n"
        "Objective/Use Case: [Detailed description of the use case objective]\n"
        "AI Application: [Detailed description of AI application]\n"
        "Cross-Functional Benefit:\n"
        "- [List benefits for each department/team within the company]\n\n"
        "Please ensure proper formatting without any extra spaces or new lines."
    )

    # Tokenize the prompt
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generate response
    outputs = model.generate(
        inputs["input_ids"],
        max_length=500,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        do_sample=True,
        top_k=50,
        top_p=0.9,
        temperature=0.7
    )

    # Decode the model output
    raw_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Post-process to ensure clean output
    formatted_text = raw_text.replace("\n", " ").replace("\r", "").strip()  # Remove newlines and extra spaces
    formatted_text = ' '.join(formatted_text.split())  # Normalize spaces
    
    return formatted_text

from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st

# Load Hugging Face model
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-1B")

def generate_use_cases(industry_name, insights):
    """
    Generate AI/GenAI use cases using a Hugging Face model and ensure proper formatting.
    """
    # Create a structured prompt
    prompt = (
        f"Generate structured AI/GenAI use cases for the {industry_name} industry based on the following insights:\n"
        f"{insights}\n\n"
        "Each use case should follow this format:\n"
        "Use Case: [Title]\n"
        "Objective/Use Case: [Detailed description of the use case objective]\n"
        "AI Application: [Detailed description of AI application]\n"
        "Cross-Functional Benefit: [List benefits for each department/team within the company]\n\n"
        "Please ensure there are no extra spaces or formatting issues."
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

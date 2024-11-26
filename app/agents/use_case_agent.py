from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st

# Load Hugging Face model
tokenizer = AutoTokenizer.from_pretrained("gpt2")  # Using GPT-2 for simplicity
model = AutoModelForCausalLM.from_pretrained("gpt2")

def generate_use_cases(industry_name, insights):
    """
    Generate AI/GenAI use cases using GPT-2 model and ensure proper formatting.
    """
    prompt = (
        f"Generate AI/GenAI use cases for the {industry_name} industry based on the following insights:\n"
        f"{insights}\n\n"
        "Each use case should follow this format:\n"
        "Use Case: [Title]\n"
        "AI Application: [Detailed description]\n"
        "Cross-Functional Benefit: [List benefits across teams/functions]\n\n"
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

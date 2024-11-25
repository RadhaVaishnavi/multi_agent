# agents/use_case_agent.py
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("nvidia/Llama-3.1-Nemotron-70B-Instruct-HF")
model = AutoModelForCausalLM.from_pretrained("nvidia/Llama-3.1-Nemotron-70B-Instruct-HF")

def generate_use_cases(industry_name, insights):
    """
    Generate AI/GenAI use cases using a language model.
    """
    prompt = (
        f"Generate structured AI/GenAI use cases for the {industry_name} industry based on the following insights:\n"
        f"{insights}\n\n"
        "Each use case should follow this format:\n"
        "Use Case: [Title]\n"
        "AI Application: [Detailed description]\n"
        "Cross-Functional Benefit: [List benefits across teams/functions]\n\n"
        "Ensure proper formatting and relevance."
    )

    inputs = tokenizer(prompt, return_tensors="pt")
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

    raw_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    formatted_text = raw_text.replace("\n", " ").strip()
    return formatted_text

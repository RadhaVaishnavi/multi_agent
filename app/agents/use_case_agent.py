# agents/use_case_agent.py
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")

def generate_use_cases(industry_name, focus_areas):
    """
    Generate AI/GenAI use cases for a given industry and focus areas.
    """
    prompt = (
        f"Generate AI/GenAI use cases for the {industry_name} industry.\n"
        f"Focus Areas: {focus_areas}\n\n"
        "Use Case: [Title]\n"
        "AI Application: [Detailed description]\n"
        "Cross-Functional Benefit: [List benefits across teams/functions]"
    )
    
    # Tokenize the input prompt
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs["input_ids"],
        max_length=500,
        num_return_sequences=1,
        temperature=0.7
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

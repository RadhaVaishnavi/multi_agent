from transformers import pipeline

def generate_use_cases(industry):
    # Predefined prompt for generating use cases
    prompt = f"""
    Industry: {industry}
    Task: Propose 3 AI/ML use cases using GenAI and LLMs to enhance operational efficiency and customer satisfaction.
    """
    generator = pipeline("text-generation", model="gpt-3.5-turbo")  # Replace with the appropriate model
    use_cases = generator(prompt, max_length=300, num_return_sequences=1)
    return use_cases

# Example Usage
use_cases = generate_use_cases(industry)

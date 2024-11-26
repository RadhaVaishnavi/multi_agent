import openai

# You can define any extra task logic here if needed
def generate_use_case(industry):
    prompt = f"Generate AI, ML, and automation use cases for the {industry} industry."
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=300,
        temperature=0.7
    )
    return response.choices[0].text.strip()

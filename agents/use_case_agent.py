from openai import OpenAI

def analyze_use_cases(industry):
    prompt = f"Analyze AI/ML use cases for the {industry} industry."
    response = OpenAI.Completion.create(model="openai:gpt-4o", prompt=prompt, max_tokens=200)
    return response.choices[0].text

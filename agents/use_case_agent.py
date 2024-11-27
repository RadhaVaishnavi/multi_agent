import openai

def generate_use_cases(industry):
    openai.api_key = 'your-api-key-here'
    prompt = f"Generate AI/ML use cases for the {industry} industry. Focus on improving operations, customer satisfaction, and boosting operational efficiency."

    try:
        response = openai.Completion.create(
            model="gpt-4",  # GPT-4 model for more accurate results
            prompt=prompt,
            max_tokens=250
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

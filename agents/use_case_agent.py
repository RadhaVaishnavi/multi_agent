import openai

def analyze_use_cases(industry):
    openai.api_key = 'your-openai-api-key'  # Replace with your OpenAI API key

    prompt = f"Analyze AI/ML use cases for the {industry} industry."
    
    try:
        response = openai.Completion.create(
            model="gpt-4",  # GPT-4 model
            prompt=prompt,
            max_tokens=200
        )
        return response.choices[0].text.strip()  # Return the use case ideas
    except Exception as e:
        return f"Error: {str(e)}"

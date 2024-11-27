import openai

# Set up OpenAI API Key
openai.api_key = 'your-api-key'

def generate_use_cases(industry):
    prompt = f"Generate AI/ML use cases for the {industry} industry, focusing on improving processes, customer satisfaction, and operational efficiency."

    try:
        # Using the correct method for ChatGPT-based models like GPT-4
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or use "gpt-3.5-turbo" for GPT-3.5
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Extracting and returning the text from the response
        use_cases = response['choices'][0]['message']['content']
        return use_cases
    except Exception as e:
        return f"Error generating use cases: {e}"

from flask import Flask, render_template, request
from research_agent import classify_industry, fetch_vision_and_product_info
from use_case_agent import generate_use_cases
from resource_agent import search_kaggle_resources, search_huggingface_resources, search_github_resources

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the home page with a form to input the company name.
    """
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    """
    Process the input company name, run the agents, and display the results.
    """
    company_name = request.form['company_name']
    if not company_name:
        return render_template('index.html', error="Please enter a company name.")

    # Research Agent
    try:
        industry = classify_industry(company_name)
        vision_info = fetch_vision_and_product_info(company_name)
    except Exception as e:
        return render_template('index.html', error=f"Error in Research Agent: {e}")

    # Use Case Agent
    try:
        use_cases = generate_use_cases(industry)
    except Exception as e:
        return render_template('index.html', error=f"Error in Use Case Agent: {e}")

    # Resource Agent
    try:
        resources = {
            "Kaggle": search_kaggle_resources(industry),
            "Hugging Face": search_huggingface_resources(industry),
            "GitHub": search_github_resources(industry),
        }
    except Exception as e:
        return render_template('index.html', error=f"Error in Resource Agent: {e}")

    # Render the results page
    return render_template(
        'results.html',
        company_name=company_name,
        industry=industry,
        vision_info=vision_info,
        use_cases=use_cases,
        resources=resources
    )

if __name__ == "__main__":
    app.run(debug=True)

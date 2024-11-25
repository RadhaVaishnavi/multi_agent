def generate_use_cases(industry):
    """
    Generate AI/GenAI use cases for a given industry.
    """
    use_cases_mapping = {
        "Electric vehicles and renewable energy": [
            {
                "title": "Autonomous Vehicle Insights",
                "application": "Use LLMs to analyze driving patterns and improve vehicle autonomy.",
                "benefits": [
                    {"team": "Engineering", "description": "Enhanced navigation algorithms."},
                    {"team": "Marketing", "description": "Data-driven safety insights for campaigns."}
                ]
            },
            {
                "title": "Predictive Energy Management",
                "application": "Leverage ML models to optimize solar and battery performance in real time.",
                "benefits": [
                    {"team": "Operations", "description": "Reduced energy waste."},
                    {"team": "Finance", "description": "Lower operational costs."}
                ]
            }
        ],
        "Automotive": [
            {
                "title": "Smart Manufacturing Insights",
                "application": "AI models to optimize production lines and predictive maintenance.",
                "benefits": [
                    {"team": "Operations", "description": "Maximized production efficiency."},
                    {"team": "Maintenance", "description": "Predict equipment failures and reduce downtime."}
                ]
            }
        ]
    }

    return use_cases_mapping.get(industry, [])

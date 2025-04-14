import openai

openai.api_key = "YOUR_API_KEY"

def suggest_clauses(contract_type):
    prompt = f"Suggest ideal clauses for a {contract_type} contract."
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7
    )
    return response.choices[0].text.strip()

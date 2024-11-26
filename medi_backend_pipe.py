from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Set your Hugging Face API token
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"  # Change the model if needed
HUGGINGFACE_API_KEY = "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"

def generate_ai_suggestions(input_text, num_suggestions=3, max_length=10):
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
    }
    payload = {
        "inputs": input_text,
        "parameters": {
            "max_length": max_length,
            "temperature": 0.7,
            "top_k": 20,
            "top_p": 0.9,
        }
    }
    suggestions = []
    try:
        for _ in range(num_suggestions):  # Make multiple calls for suggestions
            response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            if isinstance(result, list) and result:
                suggestions.append(result[0]['generated_text'].strip())
    except requests.exceptions.RequestException as e:
        return [f"Error: {str(e)}"]
    return suggestions


@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.get_json()
    user_input = data.get('input', '')

    if user_input:
        ai_suggestions = generate_ai_suggestions(user_input, num_suggestions=3)
        return jsonify({'suggestions': ai_suggestions})

    return jsonify({'suggestions': []})

# Endpoint to get the first prompt as the placeholder
@app.route('/get-first-prompt', methods=['GET'])
def get_first_prompt():
    return jsonify({'prompt': "Type something here..."})

if __name__ == '__main__':
    app.run(debug=True)

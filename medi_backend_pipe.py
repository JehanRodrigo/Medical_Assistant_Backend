
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# app = Flask(__name__)
# CORS(app)

# # model_name = "microsoft/BioGPT"
# # tokenizer = AutoTokenizer.from_pretrained(model_name)
# # model = AutoModelForCausalLM.from_pretrained(model_name)
# # text_gen_model = pipeline('text-generation', model=model, tokenizer=tokenizer, truncation=True) # device=0 to use GPU in mac



# def generate_ai_suggestions(input_text, num_suggestions=1):
#     generated = text_gen_model(input_text, max_length=10, num_return_sequences=num_suggestions, num_beams=1)
#     return [g['generated_text'].strip() for g in generated]

# @app.route('/suggest', methods=['POST'])
# def suggest():
#     data = request.get_json()
#     user_input = data.get('input', '')

#     if user_input:
#        # common_suggestions = difflib.get_close_matches(user_input, common_phrases, n=2, cutoff=0.1)
#         ai_suggestions = generate_ai_suggestions(user_input, num_suggestions=1)
#         return jsonify({'suggestions': ai_suggestions}) 

#     return jsonify({'suggestions': []})

# # Endpoint to get the first prompt as the placeholder
# @app.route('/get-first-prompt', methods=['GET'])
# def get_first_prompt():
    
#     return jsonify({'prompt': "Type something here..."})

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
# from dotenv import load_dotenv
# import os

# Load environment variables
# load_dotenv()
# API_KEY = os.getenv("GPT2_API2")

# Hugging Face API configuration
API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()  # Ensure any errors are raised
    return response.json()

# Flask application setup
app = Flask(__name__)
CORS(app)

def generate_ai_suggestions(input_text, num_suggestions=1):
    try:
        payload = {
            "inputs": input_text,
            "parameters": {
                "max_length": 50,  # Adjust this as needed
                "num_return_sequences": num_suggestions
            }
        }
        results = query(payload)
        # Extract generated text from API response
        return [result['generated_text'].strip() for result in results]
    except Exception as e:
        return [f"Error generating suggestions: {str(e)}"]

@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.get_json()
    user_input = data.get('input', '')

    if user_input:
        ai_suggestions = generate_ai_suggestions(user_input, num_suggestions=1)
        return jsonify({'suggestions': ai_suggestions})

    return jsonify({'suggestions': []})

# Endpoint to get the first prompt as the placeholder
@app.route('/get-first-prompt', methods=['GET'])
def get_first_prompt():
    return jsonify({'prompt': "Type something here..."})

if __name__ == '__main__':
    app.run(debug=True)

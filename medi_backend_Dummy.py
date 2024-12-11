
from flask import Flask, request, jsonify
from flask_cors import CORS
# from transformers import pipeline, GPT2LMHeadModel, GPT2Tokenizer
import difflib

app = Flask(__name__)
CORS(app)

common_phrases = [
    "how are you",
    "how are you doing",
    "how are things going",
    "how are you feeling today",
    "how are you doing today",
    "how is the weather",
    "how to train a dog",
    "how to bake a cake",
    "how do I install Streamlit",
    "how do transformers models work"
]

# Endpoint to provide suggestions based on user input
@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.get_json()
    user_input = data.get('input', '')

    if user_input:
        # Find suggestions based on the input
        suggestions = difflib.get_close_matches(user_input, common_phrases, n=3, cutoff=0.1)
        return jsonify({'suggestions': suggestions})

    return jsonify({'suggestions': []})

# Endpoint to get the first prompt as the placeholder
@app.route('/get-first-prompt', methods=['GET'])
def get_first_prompt():
    if common_phrases:
        return jsonify({'prompt': common_phrases[0]})
    return jsonify({'prompt': "Type something here..."})

if __name__ == '__main__':
    app.run(debug=True)
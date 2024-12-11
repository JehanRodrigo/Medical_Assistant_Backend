
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

app = Flask(__name__)
CORS(app)

model_name = "microsoft/BioGPT"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
text_gen_model = pipeline('text-generation', model=model, tokenizer=tokenizer, truncation=True, ddevice=-1) # device=0 to use GPU in mac

def generate_ai_suggestions(input_text, num_suggestions=1):
    generated = text_gen_model(input_text, max_length=10, num_return_sequences=num_suggestions, num_beams=1)
    return [g['generated_text'].strip() for g in generated]

# Endpoint to check if the server is running
@app.route('/', methods=['GET'])
def status_check():
    
    return jsonify({'prompt': "Server is Up and Running..."})

@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.get_json()
    user_input = data.get('input', '')

    if user_input:
       # common_suggestions = difflib.get_close_matches(user_input, common_phrases, n=2, cutoff=0.1)
        ai_suggestions = generate_ai_suggestions(user_input, num_suggestions=1)
        return jsonify({'suggestions': ai_suggestions}) 

    return jsonify({'suggestions': []})

# Endpoint to get the first prompt as the placeholder
@app.route('/get-first-prompt', methods=['GET'])
def get_first_prompt():
    
    return jsonify({'prompt': "Type something here..."})

if __name__ == '__main__':
    app.run(debug=True)


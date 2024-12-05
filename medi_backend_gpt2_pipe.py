
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import  AutoTokenizer, AutoModelForCausalLM
import torch
import logging


# for configure the logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ModelManager:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        self.model_name = "openai-community/gpt2"
        self.tokenizer = None
        self.model = None

    
    def load_model(self):
        try:
            # Load tokenizer and model
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(self.model_name)

        # Optional: Move to GPU if available
            if torch.cuda.is_available():
                self.model = self.model.to('cuda')
            
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.error(f"Model loading failed: {e}")
            raise

    def generate_text(self, input_text, max_length=50):
        try:
            # Validate model is loaded
            if not self.model or not self.tokenizer:
                raise ValueError("Model not initialized")

            # Tokenize input
            inputs = self.tokenizer.encode(
                input_text, 
                return_tensors='pt', 
                add_special_tokens=True
            )

            # Move to GPU if available
            if torch.cuda.is_available():
                inputs = inputs.to('cuda')

            # Generate text with advanced parameters
            outputs = self.model.generate(
                inputs,
                max_length=max_length,
                num_return_sequences=1,
                do_sample=True,
                top_k=50,
                top_p=0.95,
                temperature=0.7
            )

            # Decode generated text
            generated_text = self.tokenizer.decode(
                outputs[0], 
                skip_special_tokens=True
            )

            return generated_text
        except Exception as e:
            logger.error(f"Text generation error: {e}")
            return "Unable to generate text"

# Initialize model manager
model_manager = ModelManager.get_instance()


app = Flask(__name__)
CORS(app)



#def generate_ai_suggestions(input_text, num_suggestions=1):
#   generated = text_gen_model(input_text, max_length=10, num_return_sequences=num_suggestions, num_beams=1)
#   return [g['generated_text'].strip() for g in generated]

@app.route('/suggest', methods=['POST'])
def suggest():
    try:
        data = request.get_json()
        user_input = data.get('input', '')

        if not user_input:
            return jsonify({'suggestions': []})

#   if user_input:
       # common_suggestions = difflib.get_close_matches(user_input, common_phrases, n=2, cutoff=0.1)
#        ai_suggestions = generate_ai_suggestions(user_input, num_suggestions=1)
#       return jsonify({'suggestions': ai_suggestions}) 


    # Generate suggestion
        suggestion = model_manager.generate_text(user_input)
    
        return jsonify({

            'suggestions': [suggestion],
            'status': 'success'

        })

    except Exception as e:
        logger.error(f"Suggestion generation error: {e}")
        return jsonify({
            'error': str(e),
            'status': 'error',
            'suggestions': []
        }), 400

# Endpoint to get the first prompt as the placeholder
@app.route('/get-first-prompt', methods=['GET'])
def get_first_prompt():
    
    return jsonify({'prompt': "Type something here..."})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'model_loaded': model_manager.model is not None
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


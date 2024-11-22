import requests

from dotenv import load_dotenv
import os


load_dotenv()
# API_KEY= os.getenv("GPT2_API2")

API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
# headers = {"Authorization": f"Bearer {API_KEY}"}

headers = {"Authorization": "Bearer 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"}
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your ",
})

print(output)
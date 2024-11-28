import requests

API_URL = "https://api-inference.huggingface.co/models/microsoft/biogpt"
headers = {"Authorization": "Bearer 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"}

# headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your ",
})

print(output)
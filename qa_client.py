import os
import requests

# API endpoint URL
url = "http://localhost:8000/predict"

# Get the question and context from environment variables
question = os.environ.get("QUESTION")
context = os.environ.get("CONTEXT")

# Payload containing the question and context
payload = {
    "question": question,
    "context": context
}

# Send the POST request
response = requests.post(url, json=payload)

# Get the response JSON
result = response.json()

# Extract the answer from the result
answer = result["answer"]

# Print the answer
print("Answer:", answer)

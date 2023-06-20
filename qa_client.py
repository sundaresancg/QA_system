import os
import requests

url = "http://localhost:8000/predict"

question = os.environ.get("QUESTION")
context = os.environ.get("CONTEXT")

payload = {
    "question": question,
    "context": context
}

response = requests.post(url, json=payload)

result = response.json()

answer = result["answer"]

print("Answer:", answer)

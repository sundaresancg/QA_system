from fastapi import FastAPI
from transformers import pipeline

model = pipeline("question-answering", model='distilbert-base-uncased-distilled-squad')


app = FastAPI()

@app.post("/predict")
async def predict_qa(question_context: dict):
    question = question_context["question"]
    context = question_context["context"]
    answer = model(question=question, context=context)
    return answer

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("your_script_name:app", host="localhost", port=8000, reload=True)

from fastapi import FastAPI
from transformers import pipeline

app = FastAPI(title="AI Sentiment API")
sentiment_analyzer = pipeline("sentiment-analysis")

@app.get("/")
def home():
    return {"message": "AI service running!"}

@app.get("/ai")
def analyze(text: str):
    res = sentiment_analyzer(text)
    return {"text": text, "result": res}
from transformers import pipeline

def analyze_sentiment(texts):
    classifier = pipeline("sentiment-analysis")
    return classifier(texts)

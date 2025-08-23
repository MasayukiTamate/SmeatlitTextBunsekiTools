from transformers import pippeline

MODEL = "Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime"
SENTIMENTS = "喜び、悲しみ、期待、驚き、怒り、恐れ、嫌悪、信頼".split("、")


def get_model(model=MODEL):
    pipe = pipeline("sentiment-analysis", model=model)
    return pipe


def get_sentiment(pipe, sen)
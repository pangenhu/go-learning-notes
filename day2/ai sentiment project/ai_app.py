from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

if __name__ == "__main__":
    text = "I love this AI project!"
    result = sentiment_analyzer(text)
    print("输入：", text)
    print("结果：", result)
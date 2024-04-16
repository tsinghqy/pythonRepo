from nlp_analysis import analyze_sentiment, summarize_text


def analyze_and_return_input():
    user_input = input()
    sentiment_score = analyze_sentiment(user_input)
    summary = summarize_text(user_input)
    print(f"Original Input: {user_input}")
    print(f"Sentiment Score: {sentiment_score}")
    print(f"Summary: {summary}")

if __name__ == "__main__":
    analyze_and_return_input()

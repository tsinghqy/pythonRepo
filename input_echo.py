import nlp_analysis

try:
    def echo_input():
        user_input = input()
        print(user_input)
        try:
            sentiment_score = nlp_analysis.analyze_sentiment(user_input)
            summary = nlp_analysis.summarize_text(user_input)
            print(f"Sentiment Score: {sentiment_score}")
            print(f"Summary: {summary}")
        except ValueError as e:
            print(f"Error processing input: {e}")

    if __name__ == "__main__":
        echo_input()
except ImportError:
    print("Failed to import nlp_analysis module.")
    echo_input()

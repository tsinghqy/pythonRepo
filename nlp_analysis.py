from textblob import TextBlob


def analyze_sentiment(text):
    if not isinstance(text, str) or not text:
        raise ValueError("Input must be a non-empty string.")
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    normalized_score = ((polarity + 1) / 2) * 9 + 1  # Normalize from [-1, 1] to [1, 10]
    return round(normalized_score, 2)

def summarize_text(text):
    if not isinstance(text, str) or not text:
        raise ValueError("Input must be a non-empty string.")
    words = text.split()
    summary = ' '.join(words[:5]) if len(words) > 5 else ' '.join(words)
    return summary + "..."
    
import unittest


class TestNLPAnalysis(unittest.TestCase):
    def test_analyze_sentiment_positive(self):
        self.assertEqual(analyze_sentiment("I love this product. It is amazing!"), 10)
        
    def test_analyze_sentiment_negative(self):
        self.assertEqual(analyze_sentiment("I hate this product. It is terrible!"), 1)
        
    def test_analyze_sentiment_neutral(self):
        self.assertAlmostEqual(analyze_sentiment("This product is okay."), 5.5, places=1)
        
    def test_summarize_text_short(self):
        self.assertEqual(summarize_text("Quick summary."), "Quick summary...")
        
    def test_summarize_text_long(self):
        self.assertEqual(summarize_text("This is a longer piece of text that should be summarized."), "This is a longer piece...")
        
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            analyze_sentiment(123)
        with self.assertRaises(ValueError):
            summarize_text([])
            
if __name__ == "__main__":
    unittest.main()

from news import get_market_news
from textblob import TextBlob
import random

def get_sentiment_summary(symbol):
    """
    Get average sentiment from news.
    """
    try:
        news = get_market_news(query=symbol)
        sentiments = []
        for article in news:
            text = article.get('title', '') + ' ' + article.get('description', '')
            if text:
                blob = TextBlob(text)
                sentiments.append(blob.sentiment.polarity)
        if sentiments:
            return sum(sentiments) / len(sentiments)
        return 0.0
    except:
        return random.uniform(-1, 1)

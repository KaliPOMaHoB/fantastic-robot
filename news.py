from newsapi import NewsApiClient
from config import NEWS_API_KEY
import random

newsapi = NewsApiClient(api_key=NEWS_API_KEY)

def get_market_news(query='cryptocurrency OR stocks', language='en', page_size=10):
    """
    Fetch market news.
    """
    try:
        top_headlines = newsapi.get_top_headlines(q=query, language=language, page_size=page_size)
        return top_headlines['articles']
    except Exception as e:
        # Mock news if API fails
        return [
            {'title': f'Mock News {i}', 'description': f'Description {i}', 'url': 'https://example.com', 'publishedAt': '2023-01-01'}
            for i in range(5)
        ]
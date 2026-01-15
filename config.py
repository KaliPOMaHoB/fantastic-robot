# Configuration file for the market analysis bot

# Market symbols to analyze (e.g., stocks or crypto)
SYMBOLS = ['AAPL', 'GOOGL', 'BTC-USD', 'ETH-USD', 'XRP-USD', 'XLM-USD', 'SOL-USD', 'ADA-USD', 'DOT-USD', 'LINK-USD', 'AVAX-USD']

# Time period for historical data
PERIOD = '60d'  # Last 60 days for sufficient data

# Interval for data (1h for hourly, to include intraday since market opened)
INTERVAL = '1h'

# For top traders, perhaps use a placeholder or API
# For demo, we'll simulate or use public data

# API keys if needed (e.g., for Alpha Vantage)
ALPHA_VANTAGE_API_KEY = 'your_api_key_here'  # Replace with actual key

# Alpaca API for trading
ALPACA_API_KEY = 'your_alpaca_api_key'  # Replace with actual
ALPACA_SECRET_KEY = 'your_alpaca_secret'  # Replace with actual
ALPACA_BASE_URL = 'https://paper-api.alpaca.markets'  # Paper trading

# Stripe for payments
STRIPE_PUBLISHABLE_KEY = 'your_stripe_publishable_key'  # Replace
STRIPE_SECRET_KEY = 'your_stripe_secret_key'  # Replace

# NewsAPI for news
NEWS_API_KEY = 'your_news_api_key'  # Replace with NewsAPI key

# NewsAPI for sentiment
NEWS_API_KEY = 'your_newsapi_key'  # Replace

# Thresholds for buy/sell signals
BUY_THRESHOLD = 0.02  # 2% increase predicted
SELL_THRESHOLD = -0.02  # 2% decrease predicted
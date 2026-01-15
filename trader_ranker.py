import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_top_traders():
    """
    Fetch top traders from Binance futures leaderboard.
    Note: This is a demo; scraping may violate terms.
    """
    url = 'https://www.binance.com/en/futures-activity/leaderboard'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # This is simplified; actual parsing would require inspecting the page
    # For demo, return mock data
    traders = [
        {'name': 'Trader1', 'pnl': 150.5, 'win_rate': 0.75},
        {'name': 'Trader2', 'pnl': 120.3, 'win_rate': 0.68},
        {'name': 'Trader3', 'pnl': 100.0, 'win_rate': 0.72},
    ]
    return pd.DataFrame(traders)

if __name__ == "__main__":
    top_traders = get_top_traders()
    print(top_traders)
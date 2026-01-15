import yfinance as yf
import pandas as pd
from config import SYMBOLS, PERIOD, INTERVAL

def fetch_historical_data(symbol):
    """
    Fetch historical data for a given symbol.
    """
    ticker = yf.Ticker(symbol)
    data = ticker.history(period=PERIOD, interval=INTERVAL)
    return data

def get_all_data():
    """
    Fetch data for all symbols.
    """
    data = {}
    for symbol in SYMBOLS:
        data[symbol] = fetch_historical_data(symbol)
    return data

if __name__ == "__main__":
    data = get_all_data()
    print("Data fetched for symbols:", list(data.keys()))
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL

# Mock trading for demo
def place_order(symbol, side, qty=1):
    """
    Mock place a market order.
    """
    return f"Mock order: {side} {qty} shares of {symbol}"

def get_positions():
    """
    Mock get current positions.
    """
    return [
        {'symbol': 'AAPL', 'qty': 10, 'avg_entry_price': 150.0},
        {'symbol': 'BTC-USD', 'qty': 0.1, 'avg_entry_price': 50000.0},
        {'symbol': 'ETH-USD', 'qty': 1, 'avg_entry_price': 3000.0}
    ]

def get_account():
    """
    Mock get account info.
    """
    class MockAccount:
        cash = 10000.0
        portfolio_value = 15000.0
    return MockAccount()
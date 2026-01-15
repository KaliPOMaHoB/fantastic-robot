class RealTimeData:
    def __init__(self):
        self.latest_data = {
            'AAPL': {'close': 150.0},
            'GOOGL': {'close': 2800.0},
            'BTC-USD': {'close': 50000.0},
            'ETH-USD': {'close': 3000.0},
            'XRP-USD': {'close': 0.5},
            'XLM-USD': {'close': 0.1},
            'SOL-USD': {'close': 100.0},
            'ADA-USD': {'close': 0.4},
            'DOT-USD': {'close': 10.0},
            'LINK-USD': {'close': 15.0},
            'AVAX-USD': {'close': 30.0}
        }

    def get_latest(self, symbol):
        return self.latest_data.get(symbol, {'close': 0.0})
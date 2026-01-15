from data_fetcher import get_all_data
from analyzer import analyze_symbol
from trader_ranker import get_top_traders
from config import SYMBOLS

def main():
    print("Fetching historical data...")
    data = get_all_data()

    print("Analyzing patterns and predicting...")
    results = {}
    for symbol in SYMBOLS:
        result = analyze_symbol(data[symbol])
        results[symbol] = result
        print(f"{symbol}: Signal - {result['signal']}, Predicted Profit - {result['predicted_profit']:.2f}")

    print("\nTop Traders:")
    top_traders = get_top_traders()
    print(top_traders)

if __name__ == "__main__":
    main()
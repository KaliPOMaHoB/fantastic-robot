import pandas as pd
import pandas_ta as ta
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np
from config import BUY_THRESHOLD, SELL_THRESHOLD

def add_indicators(data):
    """
    Add technical indicators to the data.
    """
    data['RSI'] = ta.rsi(data['Close'], length=14)
    data['MACD'] = ta.macd(data['Close'])['MACD_12_26_9']
    data['SMA_20'] = ta.sma(data['Close'], length=20)
    data['SMA_50'] = ta.sma(data['Close'], length=50)
    data.dropna(inplace=True)
    return data

def prepare_features(data):
    """
    Prepare features for ML model.
    """
    features = ['RSI', 'MACD', 'SMA_20', 'SMA_50']
    # Target: 1 if next close > current close, else 0
    data['Target'] = (data['Close'].shift(-1) > data['Close']).astype(int)
    data.dropna(inplace=True)  # Drop NaN values
    X = data[features]
    y = data['Target']
    return X, y

def train_model(X, y):
    """
    Train a random forest classifier.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model accuracy: {accuracy:.2f}")
    return model

def predict_signal(model, latest_data):
    """
    Predict buy/sell signal for latest data.
    """
    features = ['RSI', 'MACD', 'SMA_20', 'SMA_50']
    X_pred = latest_data[features].iloc[-1:]  # Keep as DataFrame
    pred = model.predict(X_pred)[0]
    if pred == 1:
        return 'BUY'
    else:
        return 'SELL'

def backtest_signals(data, model):
    """
    Backtest the model on historical data.
    """
    features = ['RSI', 'MACD', 'SMA_20', 'SMA_50']
    data['Predicted'] = model.predict(data[features].values)  # Use .values for array
    data['Strategy_Return'] = data['Predicted'].shift(1) * data['Close'].pct_change()
    cumulative_return = (1 + data['Strategy_Return']).cumprod().iloc[-1] - 1
    return cumulative_return

def analyze_symbol(data):
    """
    Analyze a single symbol's data.
    """
    data = add_indicators(data)
    X, y = prepare_features(data)
    model = train_model(X, y)
    signal = predict_signal(model, data)
    # Predict profit: simple, assume based on signal
    current_price = data['Close'].iloc[-1]
    predicted_change = BUY_THRESHOLD if signal == 'BUY' else SELL_THRESHOLD
    predicted_profit = current_price * predicted_change

    # Backtest
    backtest_return = backtest_signals(data.copy(), model)

    return {
        'signal': signal,
        'current_price': current_price,
        'predicted_profit': predicted_profit,
        'model_accuracy': 0.8,  # placeholder
        'backtest_return': backtest_return
    }

if __name__ == "__main__":
    # Example
    from data_fetcher import fetch_historical_data
    data = fetch_historical_data('AAPL')
    result = analyze_symbol(data)
    print(result)
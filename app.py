import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from data_fetcher import get_all_data
from analyzer import analyze_symbol
from trader_ranker import get_top_traders
from trading import place_order, get_positions, get_account
from payments import create_subscription
from news import get_market_news
from streaming import RealTimeData
from config import SYMBOLS

st.title("Fantastic Market Analysis Bot")
st.markdown("The ultimate trader's app for analysis, trading, and insights!")

# Sidebar for inputs
st.sidebar.header("Settings")
selected_symbols = st.sidebar.multiselect("Select Symbols", SYMBOLS, default=SYMBOLS)
live_mode = st.sidebar.checkbox("Live Mode (Refresh Data)")

if st.button("Run Analysis") or live_mode:
    try:
        with st.spinner("Fetching data and analyzing..."):
            data = get_all_data()
            results = {}
            for symbol in selected_symbols:
                if symbol in data:
                    result = analyze_symbol(data[symbol])
                    # Add sentiment
                    try:
                        sentiment = get_sentiment_summary(symbol)
                    except Exception as e:
                        sentiment = 0.0  # Default if API fails
                    result['sentiment'] = sentiment
                    results[symbol] = result

            top_traders = get_top_traders()
    except Exception as e:
        st.error(f"Error during analysis: {e}")
        results = {}
        top_traders = pd.DataFrame()

    # Display results
    st.header("Analysis Results")
    for symbol, result in results.items():
        st.subheader(f"{symbol}")
        st.write(f"**Signal:** {result['signal']}")
        st.write(f"**Current Price:** ${result['current_price']:.2f}")
        st.write(f"**Predicted Profit:** ${result['predicted_profit']:.2f}")
        st.write(f"**Model Accuracy:** {result['model_accuracy']:.2f}")
        st.write(f"**Backtest Cumulative Return:** {result['backtest_return']:.2%}")
        st.write(f"**News Sentiment:** {result['sentiment']:.2f} (Bullish if >0)")

        # Live Candlestick Chart with Plotly
        df = data[symbol].reset_index()
        fig = go.Figure(data=[go.Candlestick(x=df['Datetime'] if 'Datetime' in df else df.index,
                                             open=df['Open'],
                                             high=df['High'],
                                             low=df['Low'],
                                             close=df['Close'])])
        fig.update_layout(title=f"{symbol} Live Candlestick Chart", xaxis_rangeslider_visible=False)
        st.plotly_chart(fig)

        # Trading Button
        if st.button(f"Execute {result['signal']} for {symbol}"):
            try:
                order = place_order(symbol, result['signal'])
                st.success(f"Order placed: {order}")
            except Exception as e:
                st.error(f"Error placing order: {e}. Check API keys.")

    st.header("Top Traders")
    st.dataframe(top_traders)

    # Account Info
    st.header("Trading Account")
    try:
        account = get_account()
        st.write(f"Cash: ${account.cash}")
        st.write(f"Portfolio Value: ${account.portfolio_value}")
        positions = get_positions()
        if positions:
            st.dataframe(pd.DataFrame([p.__dict__ for p in positions]))
    except Exception as e:
        st.error(f"Error fetching account: {e}. Check API keys.")
        st.error(f"Error fetching account: {e}")

    # Monetization
    st.markdown("---")
    st.markdown("**Upgrade to Premium for Real-Time Alerts and Unlimited Access!**")
    if st.button("Subscribe Now"):
        try:
            url = create_subscription('price_123456789')  # Replace with actual price ID
            st.markdown(f"[Subscribe Here]({url})")
        except Exception as e:
            st.error(f"Error creating subscription: {e}. Check Stripe keys.")

st.markdown("---")
st.markdown("**⚠️ WARNING: This app is for educational and demonstration purposes only. Trading involves significant risk of loss. Use at your own risk. Not financial advice. Test with paper trading only. The developers are not responsible for any losses.**")

# Real-Time Streaming Section
stream_mode = st.sidebar.checkbox("Enable Real-Time Streaming")
if stream_mode:
    st.header("Real-Time Data Streaming")
    rt = RealTimeData()
    for symbol in selected_symbols:
        latest = rt.get_latest(symbol)
        st.write(f"{symbol} Latest Close: ${latest['close']:.2f}")
    st.write("Mock streaming enabled.")
    # Placeholder for streaming
# Additional Features
st.header("Market News")
try:
    news = get_market_news()
    for article in news[:5]:
        st.subheader(article["title"])
        st.write(article["description"])
        st.write(f"[Read more]({article['url']})")
except Exception as e:
    st.error(f"Error fetching news: {e}")

st.header("Risk Calculator")
capital = st.number_input("Capital ($)", value=10000)
risk_per_trade = st.slider("Risk per trade (%)", 0.1, 5.0, 1.0)
stop_loss_pct = st.slider("Stop Loss (%)", 0.5, 10.0, 2.0)
position_size = (capital * (risk_per_trade / 100)) / (stop_loss_pct / 100)
st.write(f"Suggested Position Size: ${position_size:.2f}")

st.header("Watchlist")
watchlist = st.multiselect("Add to Watchlist", SYMBOLS, default=[])
if watchlist:
    st.write("Watchlist:", watchlist)


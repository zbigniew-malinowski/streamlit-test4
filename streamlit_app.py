"""Streamlit app displaying a BTC/USD price chart."""

import pandas as pd
import requests
import streamlit as st


@st.cache_data(show_spinner=False)
def load_data() -> pd.DataFrame:
    """Fetch the last week of BTC/USD prices from the CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {"vs_currency": "usd", "days": "7", "interval": "hourly"}

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    prices = response.json()["prices"]

    df = pd.DataFrame(prices, columns=["Timestamp", "Price"])
    df["Date"] = pd.to_datetime(df["Timestamp"], unit="ms")
    df = df.drop(columns=["Timestamp"]).set_index("Date").sort_index()
    return df


st.header("BTC/USD Price Chart")
data = load_data()
st.line_chart(data["Price"])

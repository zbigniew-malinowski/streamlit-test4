"""Streamlit app displaying a BTC/USD price chart."""

from datetime import date, timedelta

import pandas as pd
import requests
import streamlit as st


@st.cache_data(show_spinner=False)
def load_data() -> pd.DataFrame:
    """Fetch last month of BTC/USD prices from the CoinDesk API."""
    end_date = date.today()
    start_date = end_date - timedelta(days=30)
    url = "https://api.coindesk.com/v1/bpi/historical/close.json"
    params = {"start": start_date.strftime("%Y-%m-%d"), "end": end_date.strftime("%Y-%m-%d")}

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()["bpi"]

    df = pd.DataFrame(list(data.items()), columns=["Date", "Price"])
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.set_index("Date").sort_index()
    return df


st.header("BTC/USD Price Chart")
data = load_data()
st.line_chart(data["Price"])

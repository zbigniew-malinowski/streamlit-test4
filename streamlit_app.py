"""Streamlit app displaying a BTC/USD price chart."""

from pathlib import Path

import pandas as pd
import streamlit as st


def load_data() -> pd.DataFrame:
    """Load sample BTC/USD prices from the data folder."""
    csv_path = Path(__file__).parent / "data" / "btc_usd_sample.csv"
    df = pd.read_csv(csv_path)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.set_index("Date")
    return df


st.header("BTC/USD Price Chart")
data = load_data()
st.line_chart(data["Price"])

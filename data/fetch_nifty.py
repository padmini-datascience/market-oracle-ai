import yfinance as yf
import pandas as pd

def get_nifty_data():

    data = yf.download(
        "^NSEI",
        period="5d",
        interval="5m",
        auto_adjust=True
    )

    # Convert MultiIndex columns to normal columns
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.dropna()

    return data


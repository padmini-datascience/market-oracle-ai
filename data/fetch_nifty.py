import yfinance as yf
import pandas as pd

def get_nifty_data():

    data = yf.download(
        "^NSEI",
        period="5d",
        interval="5m"
    )

    data = data.dropna()

    return data

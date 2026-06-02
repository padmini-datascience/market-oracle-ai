import pandas as pd

def calculate_vwap(data):

    cumulative_price_volume = (
        (data['Close'] * data['Volume'])
        .cumsum()
    )

    cumulative_volume = (
        data['Volume']
        .cumsum()
    )

    data['VWAP'] = (
        cumulative_price_volume
        / cumulative_volume
    )

    return data

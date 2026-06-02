from ta.volatility import AverageTrueRange

def calculate_atr(data, window=14):

    atr = AverageTrueRange(
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        window=window
    )

    data['ATR'] = atr.average_true_range()

    return data

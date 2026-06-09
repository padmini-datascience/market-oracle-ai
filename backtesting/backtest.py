import pandas as pd

def run_backtest(data):

    total_signals = len(data)

    profitable = 0

    losing = 0

    for i in range(1, len(data)):

        if data["Close"].iloc[i] > data["Close"].iloc[i-1]:
            profitable += 1
        else:
            losing += 1

    win_rate = round((profitable / total_signals) * 100, 2)

    return {
        "Total Signals": total_signals,
        "Profitable": profitable,
        "Losing": losing,
        "Win Rate": win_rate
    }
import pandas as pd

def calculate_supertrend(data, multiplier=3):

    hl2 = (data['High'] + data['Low']) / 2

    upperband = hl2 + (multiplier * data['ATR'])
    lowerband = hl2 - (multiplier * data['ATR'])

    supertrend = [True]

    for i in range(1, len(data)):

        if data['Close'].iloc[i] > upperband.iloc[i - 1]:
            supertrend.append(True)

        elif data['Close'].iloc[i] < lowerband.iloc[i - 1]:
            supertrend.append(False)

        else:
            supertrend.append(supertrend[i - 1])

    data['Supertrend'] = supertrend

    return data

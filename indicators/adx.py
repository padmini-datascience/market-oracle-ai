from ta.trend import ADXIndicator

def calculate_adx(data, window=14):

    adx = ADXIndicator(
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        window=window
    )

    data['ADX'] = adx.adx()

    return data

def generate_entry_signal(data):

    latest = data.iloc[-1]

    if (
        latest['Close'] > latest['VWAP']
        and latest['ADX'] > 25
        and latest['Supertrend'] == True
    ):

        return {
            "signal": "BUY",
            "confidence": "Medium"
        }

    return {
        "signal": "NO TRADE",
        "confidence": "Low"
    }

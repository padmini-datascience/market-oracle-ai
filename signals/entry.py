def generate_entry_signal(data):

    latest = data.iloc[-1]

    if (
        latest['ADX'] > 25
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
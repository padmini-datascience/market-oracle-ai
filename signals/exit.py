def generate_exit_signal(data):

    latest = data.iloc[-1]

    if (
        latest['ADX'] < 20
        or latest['Supertrend'] == False
    ):

        return {
            "signal": "EXIT",
            "confidence": "Medium"
        }

    return {
        "signal": "HOLD",
        "confidence": "High"
    }
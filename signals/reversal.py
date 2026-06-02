def detect_reversal(data):

    latest = data.iloc[-1]

    previous = data.iloc[-2]

    if (
        latest['ADX'] < previous['ADX']
        and latest['Close'] < latest['VWAP']
    ):

        return {
            "reversal": True,
            "message": "Possible bearish reversal detected"
        }

    return {
        "reversal": False,
        "message": "Trend remains active"
    }

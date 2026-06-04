def detect_reversal(data):

    latest = data.iloc[-1]
    previous = data.iloc[-2]

    # Only consider reversals if trend strength exists
    if latest["ADX"] < 20:
        return {
            "reversal": False,
            "message": "Market too weak for reversal analysis"
        }

    if (
        latest["ADX"] < previous["ADX"]
        and latest["Supertrend"] == False
    ):

        return {
            "reversal": True,
            "message": "Possible bearish reversal detected"
        }

    elif (
        latest["ADX"] > previous["ADX"]
        and latest["Supertrend"] == True
    ):

        return {
            "reversal": True,
            "message": "Possible bullish reversal detected"
        }

    return {
        "reversal": False,
        "message": "No reversal signal detected"
    }
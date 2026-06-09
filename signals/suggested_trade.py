def get_suggested_trade(
    market_sentiment,
    trend_strength,
    signal_agreement
):

    if signal_agreement == "CONFLICT":
        return "NO TRADE"

    if (
        market_sentiment == "BULLISH"
        and trend_strength != "WEAK"
    ):
        return "BUY CALL"

    elif (
        market_sentiment == "BEARISH"
        and trend_strength != "WEAK"
    ):
        return "BUY PUT"

    return "NO TRADE"
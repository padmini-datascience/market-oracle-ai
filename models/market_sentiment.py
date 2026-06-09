def get_market_sentiment(
    trend_strength,
    pcr_status
):

    if (
        trend_strength == "STRONG"
        and pcr_status == "BULLISH"
    ):
        return "STRONGLY BULLISH"

    elif (
        trend_strength == "STRONG"
        and pcr_status == "BEARISH"
    ):
        return "STRONGLY BEARISH"

    elif pcr_status == "BULLISH":
        return "BULLISH"

    elif pcr_status == "BEARISH":
        return "BEARISH"

    return "NEUTRAL"
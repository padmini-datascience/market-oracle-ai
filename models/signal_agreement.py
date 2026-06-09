def get_signal_agreement(
    signal,
    market_sentiment
):

    if (
        signal == "BUY"
        and market_sentiment == "BULLISH"
    ):
        return "AGREE"

    elif (
        signal == "SELL"
        and market_sentiment == "BEARISH"
    ):
        return "AGREE"

    return "CONFLICT"
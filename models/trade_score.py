def calculate_trade_score(
    price_above_vwap,
    adx,
    supertrend
):

    score = 0

    if price_above_vwap:
        score += 40

    if adx > 25:
        score += 30

    if supertrend:
        score += 30

    return score

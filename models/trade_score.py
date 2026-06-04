def calculate_trade_score(adx, supertrend):

    score = 0

    # ADX Score
    if adx > 25:
        score += 50

    # Supertrend Score
    if supertrend:
        score += 50

    return score
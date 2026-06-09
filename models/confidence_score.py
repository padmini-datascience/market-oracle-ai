def get_confidence_score(
    trade_score,
    signal_agreement
):

    score = trade_score

    if signal_agreement == "AGREE":
        score += 20

    elif signal_agreement == "CONFLICT":
        score -= 20

    score = max(0, min(score, 100))

    return score
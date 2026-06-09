def get_trade_readiness(
    adx,
    signal_agreement,
    confidence_score
):

    readiness = confidence_score

    if adx > 25:
        readiness += 20

    if signal_agreement == "AGREE":
        readiness += 20

    readiness = min(readiness, 100)

    return readiness
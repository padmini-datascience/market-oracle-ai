def get_decision_reason(
    trend_strength,
    signal_agreement,
    confidence,
    suggested_trade
):

    reasons = []

    if trend_strength == "WEAK":
        reasons.append("Weak trend detected")

    if signal_agreement == "CONFLICT":
        reasons.append("Price and Options signals conflict")

    if confidence == "LOW":
        reasons.append("Low confidence setup")

    if suggested_trade == "BUY CALL":
        reasons.append("Bullish conditions detected")

    elif suggested_trade == "BUY PUT":
        reasons.append("Bearish conditions detected")

    if suggested_trade == "NO TRADE":
        reasons.append("Waiting for better opportunity")

    return reasons
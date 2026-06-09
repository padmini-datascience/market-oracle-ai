def get_risk_management(
    current_price,
    atr,
    suggested_trade
):

    if suggested_trade == "BUY CALL":

        stop_loss = round(current_price - atr, 2)

        target = round(current_price + (2 * atr), 2)

    elif suggested_trade == "BUY PUT":

        stop_loss = round(current_price + atr, 2)

        target = round(current_price - (2 * atr), 2)

    else:

        stop_loss = "-"

        target = "-"

    return {
        "Stop Loss": stop_loss,
        "Target": target
    }
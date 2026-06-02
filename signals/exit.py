def generate_exit_signal(
    entry_price,
    current_price,
    atr
):

    profit = current_price - entry_price

    if profit >= atr:

        return {
            "action": "BOOK_PARTIAL_PROFIT",
            "message": "Book 50% and trail remaining position"
        }

    return {
        "action": "HOLD",
        "message": "Trend still active"
    }

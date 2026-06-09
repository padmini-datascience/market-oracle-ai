import pandas as pd
import os

def get_accuracy_rate():

    file_name = "signal_history.csv"

    if not os.path.exists(file_name):

        return {
            "Correct": 0,
            "Wrong": 0,
            "Accuracy": 0
        }

    history = pd.read_csv(file_name)

    correct_signals = len(
        history[
            history["Accuracy"] == "CORRECT"
        ]
    )

    wrong_signals = len(
        history[
            history["Accuracy"] == "WRONG"
        ]
    )
    pending_signals = len(
    history[
        history["Accuracy"] == "PENDING"
        ]
    )

    total = correct_signals + wrong_signals

    if total > 0:
        accuracy_rate = round(
            (correct_signals / total) * 100,
            2
        )
    else:
        accuracy_rate = 0

    return {
        "Correct": correct_signals,
        "Wrong": wrong_signals,
        "Pending": pending_signals,
        "Accuracy": accuracy_rate
    }
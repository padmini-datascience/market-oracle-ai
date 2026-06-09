import pandas as pd
from datetime import datetime
import os

import pandas as pd
from datetime import datetime
import os

def log_signal(price, signal, verdict, accuracy):

    file_name = "signal_history.csv"

    new_row = pd.DataFrame([{
        "DateTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Price": price,
        "Signal": signal,
        "Verdict": verdict,
        "Accuracy": accuracy
    }])

    if os.path.exists(file_name):

        old = pd.read_csv(file_name)

        if len(old) > 0:

            last_signal = old.iloc[-1]["Signal"]

            if last_signal == signal:
                return

        new_data = pd.concat(
            [old, new_row],
            ignore_index=True
        )

    else:

        new_data = new_row

    new_data.to_csv(
        file_name,
        index=False
    )
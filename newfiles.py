import pandas as pd
from datetime import date, time

test_df = pd.DataFrame({
            "date": date(2025, 1, 1),
            "day": "Wednesday",
            "punch_in": time(8,0),
            "punch_out": time(18,0),
            "early-leave": False,
            "total-earning" : "₹ 483.67",
            "notes": "-",
        },
        index = [0])

test_df.to_csv("CSVs/test.csv",
            header = True,
            index = False)
import pandas as pd
import calendar
import os
from datetime import time

def get_dates_days(month, year):
    num_days = calendar.monthrange(year,month)[1]
    dates = []
    from datetime import date
    for day in range(1, num_days + 1):
        dates.append(date(year,month,day))
    days = []
    for date in dates:
        days.append(date.strftime("%A"))
    return dates,days


def create_new_datafile(month, year):
    columns = ["date" , "day" , "punch_in" , "punch_out", 
            "early-leave", "total-earning" , "notes"]
    dates, days = get_dates_days(month, year)

    num_rows = len(dates)

    df = pd.DataFrame({
            "date": dates,
            "day": days,
            "punch_in": time(8,0) * num_rows,
            "punch_out": time(18,0) * num_rows,
            "early-leave": [False] * num_rows,
            "total-earning" : ['-'] * num_rows,
            "notes": ['-'] * num_rows,
        })
    month_name = calendar.month_name[month]
    df.to_csv(f'CSVs/{month_name}-{year}.csv',
              header = True,
              index = False)


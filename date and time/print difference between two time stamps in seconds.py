from datetime import datetime
def get_seconds_diff(timestamp1, timestamp2):
    date_format = "%d-%m-%Y %H:%M:%S"
    dt1 = datetime.strptime(timestamp1, date_format)
    dt2 = datetime.strptime(timestamp2, date_format)
    diff_in_seconds = abs((dt2 - dt1).total_seconds())
    return int(diff_in_seconds)
ts1 = input().strip()
ts2 = input().strip()
print(get_seconds_diff(ts1, ts2))

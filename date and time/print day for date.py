import datetime
day, month, year = map(int, input().split())
date_obj = datetime.date(year, month, day)
day_name = date_obj.strftime("%A").upper()
print(day_name)

import datetime

def dayOfTheWeek(day, month, year):
    date = datetime.datetime(year, month, day)
    return date.strftime("%A")

day = 31
month = 8
year = 2019
print(dayOfTheWeek(day, month, year))  # Output: "Saturday"

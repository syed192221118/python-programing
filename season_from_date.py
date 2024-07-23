def season_from_date(month, day):
    if month in ["mar", "apr", "may"]:
        return "spring"
    elif month in ["jun", "jul", "aug"]:
        return "summer"
    elif month in ["sep", "oct", "nov"]:
        return "fall"
    elif month in ["dec", "jan", "feb"]:
        return "winter"
    else:
        if month == "mar" and day >= 20:
            return "summer"
        elif month == "jun" and day >= 21:
            return "summer"
        elif month == "sep" and day >= 22:
            return "fall"
        elif month == "dec" and day >= 21:
            return "winter"

month = input("Enter the month: ")
day = int(input("Enter the date: "))
print(f"The season is currently {season_from_date(month, day)}")

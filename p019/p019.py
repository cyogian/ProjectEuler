def getDay(date):
    """
    A function that returns the day that occurs on the provided date.
    Note: It works only for dates after 1 January, 1900.
    """
    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    noOfDays = 0
    for year in range(1900, date["year"]):
        if year % 400 == 0:
            noOfDays += 366
        elif year % 4 == 0 and year % 100 != 0:
            noOfDays += 366
        else:
            noOfDays += 365

    for month in range(date["month"]):
        noOfDays += daysInMonth[month]
    
    if date["month"] > 1:
        if date["year"] % 400 == 0:
            noOfDays += 1
        elif date["year"] % 4 == 0 and date["year"] % 100 != 0:
            noOfDays += 1

    noOfDays += date["day"]
    return noOfDays % 7

def countingSundays(firstYear, lastYear):
    sundays = 0
    for year in range(firstYear, lastYear + 1):
        for month in range(12):
            date = {
                "year" : year,
                "month": month,
                "day": 1
            }
            if getDay(date) == 0:
                sundays += 1
    return sundays

if __name__ == "__main__":
    print(countingSundays(1901, 2000))

    




def decline_year(year):
    year = int(year)
    if (year % 100) >= 11 and (year % 100) <= 19:
        return "лет"
    if (year % 10) == 1:
        return "год"
    if (year % 10) >= 2 and (year % 10) <= 4:
        return "года"
    return "лет"

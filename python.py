month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False

def days_in_month(year, month):
    if month < 1 or month > 12:
        return 'Invalid month'
    if month == 2 and is_leap(year):
        return 29 
    return month_days[month]

print(is_leap(2017)) 
print(days_in_month(2021, 4))  
print(days_in_month(2020, 2))  
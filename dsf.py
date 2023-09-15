from datetime import datetime


def calc_date(date1, date2):
    date1 = datetime.strptime(date1, '%d.%m.%Y')
    date2 = datetime.strptime(date2, '%d.%m.%Y')
    diff = date2-date1
    year = diff.days//365
    remaining_days = diff.days % 365
    month = remaining_days//30
    days = month % 30
    return f"There are left {year} years, {month} months and {days} days"

d1 = input('Enter first date: ')
d2 = input('Enter second date: ')
# d1 = '21.08.2023'
# d2 = '23.08.1948'

print(calc_date(d1, d2))
from datetime import datetime

print("Your date of birth")

def age_f(day, month, year, current_date=None):
    birth = datetime(year, month, day)

    if not current_date:
        current_date = datetime.today()

    day = current_date.day - birth.day
    month = current_date.month - birth.month
    year = current_date.year - birth.year

    if day < 0:
        month-= 1
        day+= 30

    if month < 0:
        year -= 1
        month += 12
        

    return year, month, day, 

c = int(input("Enter your year: ")) 
b = int(input("Enter your month: "))
a = int(input("Enter your day: "))

year, month, day = age_f(day=a, month=b, year=c)

print("Your Years =", year)
print("Month =", month)
print("Day = ",day)
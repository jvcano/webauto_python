from datetime import date
import calendar
import holidays

curr_date = date.today()
print(curr_date)
print(type(curr_date))
print(calendar.day_name[curr_date.weekday()])
check_holidays = '2023-01-01'

today_date = calendar.day_name[curr_date.weekday()]
print(today_date)
# Select country
US_holidays = holidays.US()
if  today_date == "Monday":
    if curr_date in US_holidays == True:
        print("today is a monday and a holiday")
    else:
        print("is just a monday")
elif today_date== "Tuesday":
    if today_date== True:
        print("today is a Tuesday and a holiday")
    else:
        print("is just a Tuesday")
elif today_date == "Wednsday":
    if curr_date in US_holidays== True:
        print("today is a Wednsday and a holiday")
    else:
        print("is just a Wednsday")
elif today_date == "Thursday":
    if curr_date in US_holidays== True:
        print("today is a Thursday and a holiday")
    else:
        print("is just a Thursday")
elif today_date == "Friday":
    if curr_date in US_holidays== True:
        print("today is a Friday and a holiday")
    else:
        print("is just a Friday")
elif today_date == "Sunday":
    if curr_date in US_holidays== True:
        print("today is a Sunday and a holiday")
    else:
        print("is just a Sunday")    
else:
    print("Not a week day")


""" for ptr in holidays.USA(years = 2022).items():
    print(ptr)
 
print(f'{calendar.day_name[curr_date.weekday()]}'".txt")
print(f'{calendar.day_name[curr_date.weekday()]}' ".txt")
print (today_date)
print (f'{today_date}.txt')
print(f'{today_date}.png')


 """
from datetime import date
import calendar
import holidays

curr_date = date.today()
print(curr_date)
print(calendar.day_name[curr_date.weekday()])

today_date = calendar.day_name[curr_date.weekday()]
# Select country
US_holidays = holidays.US()
if  calendar.day_name[curr_date.weekday()] == "Monday":
    if curr_date in US_holidays == True:
        print("today is a monday and a holiday")
    else:
        print("is just a monday")
elif calendar.day_name[curr_date.weekday()] == "Tuesday":
    if curr_date in US_holidays == True:
        print("today is a Tuesday and a holiday")
    else:
        print("is just a Tuesday")
elif calendar.day_name[curr_date.weekday()] == "Wednsday":
    if curr_date in US_holidays== True:
        print("today is a Wednsday and a holiday")
    else:
        print("is just a Wednsday")
elif calendar.day_name[curr_date.weekday()] == "Thursday":
    if curr_date in US_holidays== True:
        print("today is a Thursday and a holiday")
    else:
        print("is just a Thursday")
elif calendar.day_name[curr_date.weekday()] == "Friday":
    if curr_date in US_holidays== True:
        print("today is a Friday and a holiday")
    else:
        print("is just a Friday")
    
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
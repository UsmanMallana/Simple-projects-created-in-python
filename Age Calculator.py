# Age Calculator by Usman Mallana
import os
from datetime import date
# To get birth date from user
print("The age should be given in this form DD-MM-YYYY i.e 30-12-2050")
user_age = str(input("Enter age = "))
age_parts = user_age.split("-")
user_day = int(age_parts[0])
user_month = int(age_parts[1])
user_year = int(age_parts[2])
# To get current date
today = date.today()
current_day = int(today.strftime('%d'))
current_month = int(today.strftime('%m'))
current_year = int(today.strftime('%Y'))
total_days = 0

for i in range(1,current_month):
    if i==2:
        total_days += 29
    elif i%2==1:
        total_days += 31
    elif i%2==0:
        total_days += 30
total_days +=(current_day -1)
if user_year%4==0 and user_year%100:
    if user_month>2:
        total_days +=1
    else:
        pass
elif user_year%400==0:
    if user_month>2:
        total_days +=1
    else:
        pass
else:
    pass
if current_month>user_month:
    total_years = current_year - user_year
elif current_month==user_month:
    if current_day==user_day:
        print("Today is your birthday! Happy Birthday.")
        total_years = current_year - user_year
    else:
        total_years = (current_year - user_year)-1
else:
    total_years = (current_year - user_year)-1
# This is a rough estimate of the leap years as i didn't wanted to solely rely on datetime and this might result in wrong days calculations as well. But it will never be more off than a few days.
leap_years = total_years // 4
total_days_in_leap_years = leap_years * 366
left_years = total_years - leap_years
total_days_in_normal_years = left_years * 365
total_days_of_previous_years = total_days_in_leap_years + total_days_in_normal_years
total_days_since_birth = total_days_of_previous_years + total_days
print(f"It has been {total_days_since_birth} days since your birth.")
total_weeks = total_days//7
total_hours = total_days*24
total_minutes = total_hours * 60
total_seconds = total_minutes * 60
print(f"Or {total_weeks} weeks")
print(f"Or {total_hours} hours")
print(f"Or {total_minutes} minutes")
print(f"Or {total_seconds} seconds")
proceed = input("Results has been calculated!\nPress any key to continue")


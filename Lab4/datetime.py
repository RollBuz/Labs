from datetime import datetime as dt
from datetime import *

#1task
print("Task 1")
x = dt.now()
y = x - timedelta(days=5)

print(y)

print("--------------------------------------------")
#2task
print("Task 2")
today = dt.now()
print("today: ", today.strftime("%Y-%m-%d"))

yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)

print("Yesterday : ", yesterday.strftime("%Y-%m-%d"))
print("Tomorrow : ", tomorrow.strftime("%Y-%m-%d"))

print("--------------------------------------------")

#task3
print("Task 3")

current_date = dt.now().replace(microsecond=0)

print(current_date)

print("--------------------------------------------")

#task 4
print("Task 4")

date1 = dt(2025, 2, 15, 11, 0, 0)
date2 = dt(2025, 2, 15, 12, 0, 0)
difference = (date2 - date1).total_seconds()
print("Difference in seconds:", difference)

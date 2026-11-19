# Version 2: Added Date Formatting
from datetime import datetime

event_title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

event_date = datetime(year, month, day)

formatted_date = event_date.strftime("%B %d, %Y").replace(" 0", " ")
month_name = event_date.strftime("%B")
weekday_name = event_date.strftime("%A")

print("\nFormatted Output:")
print("Event:", event_title.upper())
print("Date:", formatted_date)
print("Year:", year)
print("Month:", month_name)
print("Day:", day)
print("Weekday:", weekday_name)

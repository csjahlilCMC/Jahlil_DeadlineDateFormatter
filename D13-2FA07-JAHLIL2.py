# --- DEADLINE AND DATE FORMATTER ---
# General Information
event_title = input("Enter your event title: ")
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

# Version 2.0
from datetime import datetime
event_date = datetime(year, month, day)

print()
print("=== Formatted Output ===\n")
print("Event: ", event_title.upper())
print("Event Date: ", event_date.strftime("%B %d, %Y"))
print("Year: ", event_date.year)
print("Month: ", event_date.strftime("%B"))
print("Day: ", event_date.day)
print("Weekday: ", event_date.strftime("%A"))
print()

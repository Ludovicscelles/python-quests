# Mission 9  : Create a function that takes a day as a parameter and return the next day. (i.e. for "Monday" it will return "Tuesday", for "Tuesday" it will return "Wednesday", etc.)
# You can use lists or dictionaries to solve this problem.

def next_day(day):
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  if day in days:
    index = days.index(day)
    return days[(index + 1) % len(days)]
  else:    return "Invalid day"


print(next_day("Monday")) # This will return "Tuesday", because Tuesday is the next day after Monday.
print(next_day("Sunday")) # This will return "Monday", because Monday is the next day after Sunday.
print(next_day("dfqflksqmdj")) # This will return "Invalid day", because "dfqflksqmdj" is not a valid day.


# Other way to do it:

def next_day_2(day):
  days = {
    "Monday": "Tuesday",
    "Tuesday": "Wednesday",
    "Wednesday": "Thursday",
    "Thursday": "Friday",
    "Friday": "Saturday",
    "Saturday": "Sunday",
    "Sunday": "Monday"
  }
  return days.get(day, "Invalid day")

print(next_day_2("Monday")) # This will return "Tuesday", because Tuesday is the next day after Monday.
print(next_day_2("Sunday")) # This will return "Monday", because Monday is the next day after Sunday.
print(next_day_2("dfqflksqmdj")) # This will return "Invalid day", because "dfqflksqmdj" is not a valid day.
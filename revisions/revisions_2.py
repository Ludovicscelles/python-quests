# Mission 9  : Create a function that takes a day as a parameter and return the next day. (i.e. for "Monday" it will return "Tuesday", for "Tuesday" it will return "Wednesday", etc.)
# You can use lists or dictionaries to solve this problem.

def next_day(day):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if day in days:
        index_of_day = days.index(day)
        return days[(index_of_day + 1) % len(days)]
    else: return "Invalid day"

print (next_day("Monday"))
print (next_day("Wednesday"))
print (next_day("Sunday"))
print (next_day("Tuday"))
print("")

def next_day_2(day):
  days = {
    "Monday" : "Tuesday",
    "Tuesday" : "Wednesday",
    "Wednesday" : "Thursday",
    "Thursday" : "Friday",
    "Friday" : "Saturday",
    "Saturday" : "Sunday",
    "Sunday" : "Monday"
  }
  return days.get(day, "Invalid day")


print (next_day_2("Monday"))
print (next_day_2("Thursday"))
print (next_day_2("Sunday"))
print (next_day_2("Sanurday"))

  
words = []

def add_word(sentence):
  words.append(sentence)

add_word("Hello")
add_word("World")

print(words)
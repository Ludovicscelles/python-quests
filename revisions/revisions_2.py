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

# Mission 10 : Create a function that fills an empty list with values (words) from the following string :
# "After twelve soft showers are the arch-duchess' socks dry, arch-dry?"

words = []

def fill_a_list(string):
   for word in string.split():
      words.append(word)

fill_a_list("After twelve soft showers are the arch-duchess' socks dry, arch-dry?")
print(words)

# Other solution

words_2 = []

def fill_a_list_2(string):
   words_2.extend(string.split())

fill_a_list_2("Once upon a time, in a far away land, a young prince lived in a shining castle.")
print(words_2)

# Revise Statistics Functions for Strings


# Count the number of words in a string

def count_words(string):

  words = string.split()

  if not words:
    raise ValueError("La chaîne de caractères est vide.")
  
  return len(words)

phrase = "My name is Ludovic Scelles"
print(count_words(phrase))

# other way to do it:

def count_words_2(string):
  
  words = string.split()

  if not words:
    raise ValueError("La chaîne de caractères est vide.")

  return {"Nombre total de mots": len(words)}

phrase = "I have two dogs and a cat named Max and Whiskers"
print(count_words_2(phrase))

# Count the number of characters in a string

def count_characters(string):

  if not string:
    raise ValueError("La chaîne de caractères est vide.")

  return len(string)

sentence = "Hello, how are you doing today ?"
print(count_characters(sentence))

# Other way to do it (return a dictionary):

def count_characters_2(string):

  if not string:
    raise ValueError("La chaîne de caractères est vide.")

  return {"Nombre total de caractères": len(string)}

sentence_2 = "Hi, what are you doing this holiday season ?"
print(count_characters_2(sentence_2))


# Count the number of characters in a string without spaces

def count_ch_without_spaces(string):

  if not string:
    raise ValueError("La chaîne de caractères est vide")
  
  text = string.replace(" ", "")
  return len(text)

sentence = "Hello, how are you doing today ?"
print(count_ch_without_spaces(sentence))

# Other way to do it (return a dictionary)

def count_ch_without_spaces_2(string):

  if not string:
    raise ValueError("La chaîne de caractères est vide.")
  
  text = string.replace(" ", "")
  return {"Nombre total de caractères sans espaces" : len(text)}

sentence_2 = "Hi, what are you doint this holiday season ?"
print(count_ch_without_spaces_2(sentence_2))


# Return the biggest word

def biggest_word(string):
  
  words = string.split()

  if not words:
    raise ValueError("La chaîne de caractères est vide.")
  
  longest_word = words[0]

  for word in words:
    if len(word) >= len(longest_word):
      longest_word = word
  return longest_word
  
sentence = "Hello, this morning I went to the park and saw a beautiful butterfly"
print(f"Le mot le plus long de la phrase est {biggest_word(sentence)}.")


# Other way to do it (return a dictionary)

def biggest_word_2(string):

  words = string.split()

  if not words:
    raise ValueError("La chaîne de caractères est vide.")

  longest_word = words[0]

  for word in words:
    if len(word) >= len(longest_word):
      longest_word = word
  
  return {"Mot le plus long": longest_word}


sentence_2 = "Tonight, I will be going to the cinema with my friends to watch a new action movie"
print(biggest_word_2(sentence_2))

# Length average of words in a string

def length_average_words(string):

  words = string.split()
  
  if not words:
    raise ValueError("La chaîne de caractères est vide.")
  
  average = count_ch_without_spaces(string)/count_words(string)

  return average

sentence = "Last year, I traveled to Europe and visited several countries including France, Italy, and Spain"
print(round(length_average_words(sentence),2))

# Other way to do it (return a dictionary)

def length_average_words_2(string):

  words = string.split()

  if not words:
    raise ValueError("La chaîne de caractères est vide.")
  
  total_length = sum(len(word) for word in words)
  average_length = round(total_length / len(words), 2)

  return {"Longueur moyenne des mots": average_length}

sentence_2 = "This summer, I plan to go on a road trip across the United States and visit several national parks"
print(length_average_words_2(sentence_2))


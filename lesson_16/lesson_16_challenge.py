"""
Challenge
On pratique
Dans ce challenge tu vas reprendre ton objet data analyst précédemment crée. 
Tu lui feras en plus hériter d'une classe mère "statisticien".

La classe mère statisticien aura 3 attributs : Chacun d'entre eux peut avoir des valeurs entières (integer) allant de 0 à 100 :

logique
memoire
creativite
La classe mère aura pour méthodes :

les fonctions de la quête "Au secours des statisticiens - partie 2"
initialisation() : une méthode qui attribue aléatoirement une valeur aux 3 attributs en faisant en sorte que la somme totale soit comprise entre 111 et 177, 
les valeurs paires et multiples de 5 exclues. Cette méthode sera lancée par le constructeur de l'objet.
Initialise un notebook sur Google colab. Tu coderas tes classes mères et filles dans ce notebook, puis tu instancieras un objet de la classe fille.

Une fois réalisé, poste le lien vers ton notebook en commentaire pour validation, sans oublier de le rendre accessible en lecture 
pour toute personne disposant du lien.


"""


import random
from datetime import datetime

class Statisticien:

  def __init__(self):
    self.initialization()

  @staticmethod
  def next_day(day):

    days = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

    if day in days:
      index = days.index(day)
      return days[(index + 1) %len(days)]
    else: return "Invalid day"

  @staticmethod
  def fill_a_list(sentence):
   return sentence.split()
  
  @staticmethod
  def capitalize_certain_vowels(string):
    vowels = "aeiouy"
    result = ""

    for index, letter in enumerate(string.lower()):
      if letter in vowels and index % 2 == 0:
        result += letter.upper()
      else:
        result += letter

    return result

  @staticmethod
  def create_empty_grid(n):
    return [[[] for j in range (n)] for i in range(n)]
  
  @staticmethod
  def display_your_age(year_of_birth, first_name):
    current_year = datetime.now().year
    age = current_year - year_of_birth

    return (
      "Hello "
      + first_name
      + ", today you are (or you will be this year) "
      + str(age)
      + " years old."
      )

  def initialization(self):
    
    authorized_values = [
      number
      for number in range(0, 101)
      if number % 2 != 0 and number % 5 != 0
    ]



    while True:

      self.logic = random.choice(authorized_values)
      self.memory = random.choice(authorized_values)
      self.creativity = random.choice(authorized_values)

      sum_attributes = sum([self.logic, self.memory, self.creativity])

      if 111 <= sum_attributes <= 177:
        break
      
    print(f"La somme des attributs est de {sum_attributes}")


class DataAnalyst(Statisticien):
  def __init__(self, lastname, firstname, age, sexe, previous_training):
    super().__init__()
    self.lastname = lastname
    self.firstname = firstname
    self.age = age
    self.sexe = sexe
    self.previous_training = previous_training
    self.motivation = 100
    self.progressing = 0

  # Methodes pour simuler les actions du data analyst et modifier les attributs motivation et progression

  def do_training(self):

    motivation_loss = random.randint(5, 25)
    self.motivation -= motivation_loss

    progressing_gain = random.randint(20, 30)
    self.progressing += progressing_gain

    return self.motivation, self.progressing
  
  def work_harder(self):

    motivation_gain = random.randint(10, 30)
    self.motivation += motivation_gain
    self.progressing += motivation_gain

    return self.motivation, self.progressing
  
  def failed(self):
    
    motivation_loss = random.randint(20, 40)
    self.motivation -= motivation_loss

    progressing_gain = random.randint(20, 40)
    self.progressing += progressing_gain

    return self.motivation, self.progressing
  
  def succeed(self):

    motivation_gain = random.randint(20, 40)
    self.motivation += motivation_gain

    progressing_gain = random.randint(10, 20)
    self.progressing += progressing_gain

    return self.motivation, self.progressing

tom = DataAnalyst("Dubois", "Tom", 28, "masculin", "Devops")

print("Logique :", tom.logic)
print("Mémoire :", tom.memory)
print("Créativité :", tom.creativity)

total_attributes = sum([tom.logic, tom.memory, tom.creativity])
print(f"La somme des attributs est de {total_attributes}")

print(tom.capitalize_certain_vowels("bonjour tout le monde"))
import random

# Générer un entier aléatoire

integer = random.randint(0, 200)
print(integer)

# Générer un nombre décimal

decimal_number = random.random()
print(decimal_number)

# Générer un nombre décimal dans un intervall

dec_num = random.uniform(1, 28)
print(dec_num)

# Générer un élément aléatoire dans une liste

cheesecakes = ["New York", "Cheesecake", "Chocolate Cheesecake", "Strawberry Cheesecake", "Lemon Cheesecake", "Blueberry Cheesecake", "Pumpkin Cheesecake", "Oreo Cheesecake"]

cheesecake = random.choice(cheesecakes)
print(cheesecake)

# Choisir plusieurs éléments

# Sans répétition

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20]

draw = random.sample(numbers, 4)
print(draw)

# Mélanger une liste

cards = ["As", "Roi", "Dame", "Valet", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

shuffled_cards = cards.copy()
random.shuffle(shuffled_cards)

print(shuffled_cards)

# Générer un nombre avec pas 

even_number = random.randrange(0, 500, 2)
print(even_number)

multiple_of_5 = random.randrange(0, 1000, 5)
print(multiple_of_5)

# function

motivation = 100
progression = 0

def do_training(motivation, progression):

  motivation_loss = random.randint(5, 25)
  motivation -= motivation_loss

  progress_gain = random.randint(20, 30)
  progression += progress_gain

  return motivation, progression

motivation, progression = do_training(motivation, progression)

print(f"Motivation: {motivation}, Progression: {progression}")

# Class

# La classe mère statisticien aura 3 attributs : Chacun d'entre eux peut avoir des valeurs entières (integer) allant de 0 à 100 :

# logique
# memoire
# creativite
# initialisation() : une méthode qui attribue aléatoirement une valeur aux 3 attributs en faisant en sorte que la somme totale soit comprise entre 111 et 177, 
# les valeurs paires et multiples de 5 exclues. Cette méthode sera lancée par le constructeur de l'objet.

class Statisticien:
  def __init__(self):
    self.initialization()

  def initialization(self):

    autorized_values = [
      number
      for number in range(0, 100)
      if number % 2 != 0 and number % 5 != 0
    ]

    while True:
      self.logic = random.choice(autorized_values)
      self.memory = random.choice(autorized_values)
      self.creativity = random.choice(autorized_values)

      sum_attributes = sum([self.logic, self.memory, self.creativity])

      if 111 <= sum_attributes <= 177:
        break
    
    print("La somme des attributs est de : ", sum_attributes)

statisticien1 = Statisticien()
statisticien1.initialization()

      

    


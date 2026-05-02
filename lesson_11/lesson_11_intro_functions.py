# A Function

# A function is a block of code that performs a specific task. 
# It can take inputs, called parameters, and can return an output. 
# Functions help to organize code and make it reusable.

# Example of a function that adds dice rolls together:  

def dice_roll_sum(coup_1, coup_2, coup_3):
    total = coup_1 + coup_2 + coup_3

    if total < 8:
        return "bad bad not good"
    elif total < 13:
        return "good"
    else:
        return "amazing !"
    
print(dice_roll_sum(1, 2, 3)) # Output: "bad bad not good"
print(dice_roll_sum(3, 4, 5)) # Output: "good"
print(dice_roll_sum(5, 6, 6)) # Output: "amazing !"

# Function without parameters:

def hello_world():
    return "Hello World!"

print(hello_world()) # Output: "Hello World!"


# Functions can be used in loops to perform repetitive tasks.

import random

"""
Le module random de Python permet de faire beaucoup de choses.
On va utiliser la fonction randint pour générer des valeurs aléatoires entre 1 et 6, comme chaque lancé de dé.
"""

final_players = 0 # On initialise un compteur à 0. Ce compteur compte le nombre de participants accédant à la finale.

for i in range(100): # On fait une boucle en s'assurant que notre code exécute 32 fois notre fonction.
    result = dice_roll_sum(random.randint(1,6), random.randint(1,6), random.randint(1,6))
    if result == "amazing !":
      final_players += 1 

"""
Le résultat ("bad bad not good", "good" ou "amazing !") est attribué à la variable result.
Si le résultat obtenu est "amazing !", c'est que le joueur a fait un total supérieur à 12, et donc il est qualifié.
On ajoute 1 à la variable 'final_players' à chaque fois qu'un joueur est qualifié.
"""

print(f"Il y a {final_players} joueurs qualifiés pour la finale !")
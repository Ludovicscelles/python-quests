"""
Challenge
Dans ce challenge tu vas créer ta 1ère classe dataAnalyst qui va simuler la vie d'un data analyst. 

Voici les caractéristiques de ta classe :

attributs :

nom (str) 
prenom (str) 
age (int) 
sexe (str) 
formationPrecedente (str) 
motivation (int valant 100 à l'instanciation) 
progression (int valant 0 à l'instanciation)

méthodes : 

suivreFormation() : chaque fois qu'elle est utilisée, cette méthode diminue la motivation d'une valeur entière aléatoire (random) entre 5 et 25 
et augmente la progression d'une valeur entière aléatoire entre 20 et 30 ; 

bosserPlus() : chaque fois qu'elle est utilisée, cette méthode augmente la motivation 
et la progression d'une valeur entière aléatoire entre 10 et 30 ; 

echouer() : chaque fois qu'elle est utilisée baisse la motivation d'une valeur entre 20 et 40 
et augmente la progression d'une valeur entre 20 et 40 ; 

reussir() : chaque fois qu'elle est utilisée, augmente la motivation d'une valeur entre 20 et 40 
et augmente la progression d'une valeur random entre 10 et 20

Instancie un objet dataAnalyst et indique un nom, un prenom, le sexe et la formationPrecedente. 
L'attribut motivation vaudra 100 au début et l'attribut progression vaudra 0.

Le programme va automatiquement et aléatoirement lancer des méthodes et afficher le récapitulatif de l'état des attributs motivation 
et progression. Le programme s'arrête quand la motivation tombe à zéro et affiche "BRAVO TU AS GAGNÉ !!!" 
ou quand progression atteint 100 et affiche "BRAVO TU AS APPRIS !!!".

Exemple de résultat attendu :

Tour 1
La méthode echouer() a été utilisée.
motivation vaut maintenant 60
progression vaut maintenant 20

Tour 2
La méthode bosserPlus() a été utilisée.
motivation vaut maintenant 60
progression vaut maintenant 35

...

Tour 7
La méthode reussir() a été utilisée.
motivation vaut maintenant 10
progression vaut maintenant 110
BRAVO TU AS APPRIS !!!


"""
import random

class DataAnalyst:

  def __init__(self, lastname, firstname, age, sexe, previous_training):
    self.lastname = lastname
    self.firstname = firstname
    self.age = age
    self.sexe = sexe
    self.previous_training = previous_training
    self.motivation = 100
    self.progress = 0


  def take_course(self):

    motivation_loss = random.randint(5, 25)
    self.motivation -= motivation_loss

    progress_gain = random.randint(20, 30)
    self.progress += progress_gain

    self.motivation = max(0, self.motivation)

    return self.motivation, self.progress
  

  def work_harder(self):

    gain = random.randint(10, 30)

    self.motivation += gain

    self.progress += gain

    return self.motivation, self.progress
  

  def fail(self):

    motivation_loss = random.randint(20, 40)
    self.motivation -= motivation_loss
    
    progress_gain = random.randint(20, 40)
    self.progress += progress_gain

    self.motivation = max(0, self.motivation)

    return self.motivation, self.progress
  
  
  def succeed(self):
    
    motivation_gain = random.randint(20, 40)
    self.motivation += motivation_gain

    progress_gain = random.randint(10, 20)
    self.progress += progress_gain

    return self.motivation, self.progress
  

tom = DataAnalyst("David", "Tom", 33, "masculin", "data_ia")

print(
  f"{tom.firstname} {tom.lastname} a {tom.age} ans. Cette personne est de sexe {tom.sexe}\n"
  f"Il a suivi la formation {tom.previous_training}.\n"
  f"Sa motivation est initialisée à {tom.motivation} et sa progression est initialisée à {tom.progress}."
)

methods = [
  tom.take_course,
  tom.work_harder,
  tom.fail,
  tom.succeed,
]


def launch_program():

  tour = 1

  while tom.motivation > 0 and tom.progress < 100:

    action = random.choice(methods)
    action()

    print(
      f"Tour {tour}\n"
      f"La méthode {action.__name__} a été utilisée.\n"
      f"motivation vaut maintenant {tom.motivation}\n"
      f"progression vaut maintenant {tom.progress}\n"
    )
  
    tour += 1


  if tom.motivation <= 0:
    print("BRAVO TU AS GAGNÉ !!!")
  else:
    print("BRAVO TU AS APPRIS !!!")


launch_program()
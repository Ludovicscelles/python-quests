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
    self.progressing = 0

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

print(tom.lastname, tom.firstname, tom.age, tom.sexe, tom.previous_training, tom.motivation, tom.progressing)

print(f"{tom.firstname} {tom.lastname} a {tom.age} ans, il est de sexe {tom.sexe}.\n" 
      f"Il a suivi la formation {tom.previous_training}.\n" 
      f"Sa motivation est de {tom.motivation} et sa progression est de {tom.progressing}.")

methods = [
tom.do_training,
tom.work_harder,
tom.failed,
tom.succeed
]


while tom.motivation > 0 and tom.progressing < 100:
  action = random.choice(methods)
  action()

  print(
    f"Motivation : {tom.motivation} "
    f"Progression : {tom.progressing}"
  )

if tom.motivation <= 0:
  print("BRAVO TU AS GAGNÉ !!!")
else:
  print("BRAVO TU AS APPRIS !!!")


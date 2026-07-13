# Héritage

# L'héritage est un concept de la programmation orientée objet qui permet de créer une nouvelle classe à partir d'une classe existante. 
# La nouvelle classe, appelée classe dérivée ou sous-classe, hérite des attributs et des méthodes de la classe existante, 
# appelée classe de base ou super-classe. 
# Cela permet de réutiliser le code et de créer des hiérarchies de classes.

# Par exemple, si nous avons une classe "Animal" avec des attributs et des méthodes communs à tous les animaux,
# nous pouvons créer des sous-classes "Chien" et "Chat" qui héritent de la classe "Animal" et ajoutent des attributs et des méthodes spécifiques à chaque type d'animal.

# Exemple de code :
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def respirer(self):
        print(f"{self.nom} respire.")

    def se_deplacer(self):
        print(f"{self.nom} se déplace.")
    

class Chien(Animal):
    def __init__(self, nom, age, race):
        super().__init__(nom, age)
        self.race = race

    def aboyer(self):
        print(f"{self.nom} aboie.")

class Chat(Animal):
    def __init__(self, nom, age, couleur):
        super().__init__(nom, age)
        self.couleur = couleur

    def miauler(self):
        print(f"{self.nom} miaule.")
  

# Différence entre héritage et composition :

# L'héritage est une relation "est un" entre les classes, tandis que la composition est une relation "a un" entre les classes.

# Par exemple, si nous avons une classe "Automobile" et une classe "Moteur", 
# nous pouvons dire que voiture est une automobile (héritage), mais une voiture a un moteur (composition).

class Moteur:
    def __init__(self, puissance):
        self.puissance = puissance

class Automobile:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

class Voiture(Automobile):
    
    def __init__(self, marque, modele, moteur, couleur):
        super().__init__(marque, modele)
        self.moteur = moteur
        self.couleur = couleur

moteur = Moteur(200)
puma = Voiture("Ford", "Puma", moteur, "Bleu")

print(f"Marque : {puma.marque}, Modèle : {puma.modele}, Puissance : {puma.moteur.puissance}, Couleur : {puma.couleur}")

# Accessibilité des attributs et méthodes dans l'héritage :

# Les attributs et méthodes d'une classe de base sont accessibles dans une classe dérivée.
# Les attributs commençant par deux underscores sont renommés automatiquement par Python 
# afin d’éviter les accès accidentels et les conflits dans les sous-classes. 
# Ils ne sont cependant pas totalement privés, ils sont protégés par un mécanisme de nommage appelé "name mangling".

# Exemple de code :

class Car:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        self.__moteur = "V8"  # attribut avec name mangling

    def __demarrer_moteur(self):  # méthode avec name mangling
        print(f"{self.marque} {self.modele} démarre le moteur {self.__moteur}.")

    def demarrer(self):
        self.__demarrer_moteur()  # appel interne à la classe

    def eteindre(self):
        print(f"{self.marque} {self.modele} s'éteint.")


class MyCar(Car):
    def __init__(self, marque, modele):
        super().__init__(marque, modele)
    
    def demarrer(self):
        super().demarrer()  # appel de la méthode publique de la classe parente
        print("Le mode sport est activé.")

    def eteindre(self):
        print("Le moteur est en train de s'éteindre...")
        super().eteindre()  # appel de la méthode publique de la classe parente

    def demarrer_moteur(self):
        self.__demarrer_moteur()  
        # Ne fonctionne pas : Python cherche
        # _MyCar__demarrer_moteur() au lieu de _Car__demarrer_moteur() 

# Nous voyons que MyCar hérite de Car, mais elle ne peut pas accéder directement à __moteur ni à __demarrer_moteur. 
# En effet, Python applique un mécanisme appelé name mangling, 
# qui renomme automatiquement ces membres afin d'éviter les accès accidentels 
# et les conflits de noms dans les sous-classes.

# L'encapsulation

# L'encapsulation est un concept de la programmation orientée objet qui consiste à regrouper les données (attributs) et les comportements (méthodes) 
# dans une même classe, tout en contrôlant l'accès à ces données afin de préserver la cohérence de l'objet.

# Le name mangling, les attributs avec _ ou __, ainsi que le propriété (property) sont des mécanismes de conventions
# qui permettent de mieux mettre en œuvre ce principe de Python.

# Exemple de code :

class SuperCar:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color
    
    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed
    
    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color

ford = SuperCar(200, "red")
honda = SuperCar(250, "blue")
audi = SuperCar(300, "black")

print(ford.get_speed())

ford.set_speed(300)

ford.__speed = 400

print(ford.get_speed())
print(ford.get_color())

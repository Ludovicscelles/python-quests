# La programmation orientée objet (POO)

# Lorsqu'un programme devient conséquent, il est souvent nécessaire de le structurer afin qu'il soit plus lisible, 
# plus facile à maintenir et qu'il évite les duplications de code (principe DRY : Don't Repeat Yourself). 
# Pour cela, on peut utiliser différentes techniques comme les fonctions, les modules ou encore la programmation orientée objet (POO).
# La POO consiste à représenter les éléments d'un programme sous forme d'objets qui regroupent des données (les attributs) 
# et les actions qu'ils peuvent réaliser (les méthodes).
# Les objets possèdent des attributs (leurs données ou caractéristiques) et des méthodes (les fonctions qui leur sont associées).

# Chaque fois que l'on veut créer un objet et l'utiliser, on dit qu'on "instancie" un objet de la classe correspondante. Une classe est un modèle ou un plan qui définit les attributs et les méthodes d'un objet.

# Par exemple, ci-dessous, on crée une classe "Car" et l'on instancie deux objets "car1" et "car2" de cette classe. 
# Chaque objet a ses propres attributs et peut utiliser les méthodes définies dans la classe.

class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        

    def start_engine(self):
        print(f"The engine of the {self.brand} {self.model} is starting.")

    def stop_engine(self):
        print(f"The engine of the {self.brand} {self.model} is stopping.")


# Instanciation de deux objets de la classe Car
car1 = Car("Toyota", "Corolla", 2020, "Red")
car2 = Car("Honda", "Civic", 2019, "Blue")

# Utilisation des méthodes des objets
car1.start_engine()  # Output: The engine of the Toyota Corolla is starting.
car2.start_engine()  # Output: The engine of the Honda Civic is starting.
car1.stop_engine()   # Output: The engine of the Toyota Corolla is stopping.
car2.stop_engine()   # Output: The engine of the Honda Civic is stopping.

# Chaque voiture a ses propres attributs : l'une est rouge et l'autre est bleue, elles ont des marques et des modèles différents, 
# mais elles partagent les mêmes méthodes pour démarrer et arrêter le moteur.

# Un autre exemple d'utilisation de la POO est la création d'une classe "Person" avec des attributs comme le nom, l'âge et le sexe, et des méthodes pour afficher les informations de la personne.

# Nous pouvons créer des objets humains avec des caractéristiques différentes, et les faire interagir avec des objets Car.
# En effet, les objets s'utilisent entre eux pour créer des interactions et des comportements complexes.
# Cela permet de mieux organiser le code et de le rendre plus lisible et maintenable.

# Exemple d'une classe "Person" avec des méthodes pour interagir avec des objets "Car".

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender 

    def drive_car(self, car):
        print(f"{self.name} is driving the {car.color} {car.brand} {car.model}.")
        car.start_engine()
        car.stop_engine()

# Instanciation d'un objet de la classe Person
person1 = Person("Alice", 30, "Female")

# Utilisation de la méthode drive_car pour faire interagir l'objet Person avec l'objet Car
person1.drive_car(car1)  # Output: Alice is driving the Red Toyota Corolla.
person1.drive_car(car2)  # Output: Alice is driving the Blue Honda Civic.


# La POO permet de nombreux avantages, tels que :

# - un code plus modulaire : les objets peuvent être testés indépendamment, ce qui facilite la détection et la correction des erreurs.

# - un code plus court et mieux structuré : les objets peuvent être réutilisés dans différents contextes, ce qui réduit la duplication de code.

# - une meilleure organisation du code : les objets peuvent être regroupés en modules, ce qui facilite la navigation et la compréhension du code.

# - une meilleure maintenabilité : les objets peuvent être modifiés ou remplacés sans affecter le reste du code, ce qui facilite la mise à jour et l'évolution du programme.


# La POO avec Python

# On ne s'en rend pas forcément compte, mais Python est un langage orienté objet.
# En effet, presque toutes les valeurs sont des objets en Python : les nombres, les chaînes de caractères, les listes, les dictionnaires, les fonctions, etc. sont tous des objets.
# Ce sont des objets de types : int, str, list, dict, function, etc. qui possèdent des attributs et des méthodes.
# On utilise aussi des méthodes pour manipuler ces objets, comme par exemple la méthode upper() pour convertir une chaîne de caractères en majuscules, 
# ou la méthode append() pour ajouter un élément à une liste.


# Ce qu'il faut retenir de la POO :

# - On crée une classe avec le mot-clé "class" suivi du nom de la classe.

# - Le constructeur de la classe est une méthode spéciale appelée "__init__" qui est appelée automatiquement lors de l'instanciation d'un objet.

# - Le mot clé "self" est utilisé pour faire référence à l'objet courant et accéder à ses attributs et méthodes.

# - On instancie un objet de la classe en appelant le nom de la classe avec les arguments nécessaires pour le constructeur.

# - Chaque objet possède ses propres attributs et peut utiliser les méthodes définies dans la classe.
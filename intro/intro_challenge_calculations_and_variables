"""

Lors d'une bousculade à la sortie d'un cours, un des enfants a malencontreusement fait tomber votre robot dans les escaliers ! Celui-ci a subi des chocs et vous craignez qu'il ne fonctionne plus. Dans le petit manuel d'utilisation du robot, il est indiqué que le test de base pour savoir si le robot fonctionne est de lui faire afficher le nombre 42.

Ce que doit faire votre programme :
Votre programme doit afficher le nombre 42.

"""

print()

def test_robot():
    print(42)

test_robot()


"""

Lors du cours d'astronomie que le professeur donne aux élèves, il leur explique le principe des éclipses, puis il leur indique la date de la prochaine éclipse totale sur Algoréa. 
Vous connaissez donc la date de l'éclipse ainsi que la date actuelle et vous vous demandez dans combien de jours aura donc lieu cette éclipse. Notez que ces deux dates sont exprimées en nombre de jours du calendrier algoréen.

Ce que doit faire votre programme :
Vous savez que l'éclipse aura lieu le 12581e jour et que la date actuelle est le 11937e jour. 
Votre programme doit calculer et afficher le nombre de jours qu'il faudra patienter avant de pouvoir admirer l'éclipse.

"""

print()

def days_until_eclipse():
    eclipse_day = 12581
    current_day = 11937
    days_to_wait = eclipse_day - current_day
    print(days_to_wait)

days_until_eclipse()

"""

Les élèves ne semblent pas à l'aise avec votre robot : ce n'est pas un être humain, ce n'est pas un animal non plus… ils sont donc très intrigués, voire même parfois un peu inquiets. Afin de les rassurer, vous souhaitez que votre robot distribue 3 bonbons à chaque élève. 
Pour cela, vous avez besoin de calculer le nombre de bonbons à acheter.

Ce que doit faire votre programme :
L'école est formée de 4 classes, constituées respectivement de 25, 30, 27 et 22 élèves. 
Cependant, 8 élèves sont absents aujourd'hui. 
Sachant que chaque élève présent doit recevoir 3 bonbons, écrivez un programme qui calcule puis affiche le nombre total de bonbons nécessaires.

Vous n'avez pas besoin de calculatrice : effectuez les calculs dans votre programme.

"""

print()

students_per_class = [25, 30, 27, 22]
total_students = sum(students_per_class)
absent_students = 8
present_students = total_students - absent_students
candies_per_student = 3

def calculate_candies():
    total_candies = present_students * candies_per_student
    print(total_candies)

calculate_candies()

"""
À la fin d'une course d'endurance, les élèves d'une classe sont épuisés. Leur enseignant leur parle de l'algoréathlon, un exercice d'endurance connu sur toute la planète. 
Il s'agit d'enchaîner 2 km de natation, 34 km de cyclisme et 6 km de course à pied en un jour, puis de le refaire un deuxième jour, et encore un troisième jour.
Les élèves se demandent quelle distance a été parcourue après chaque jour. Vous profitez de l'occasion pour faire intervenir votre robot.
Ce que doit faire votre programme :
L'algoréathlon se constitue de trois étapes à effectuer chaque jour : 2 km de natation, 34 km de cyclisme et 6 km de course à pied.
Sachant qu'un sportif répète ces trois étapes pendant 3 jours de suite, vous devez afficher la distance totale qu'il a parcourue à la fin du 1er jour, à la fin du 2e jour, puis à la fin de l'algoréathlon complet.
Afin de rendre l'affichage convivial sur l'écran du robot, vous souhaitez mettre les trois valeurs sur une même ligne, avec une espace entre chaque valeur et la suivante.
Important : pour écrire ce programme, vous devez mémoriser la distance parcourue en un jour en lui donnant un nom, puis utiliser ce nom pour calculer les trois réponses. Appuyez-vous sur les explications ci-dessous.


"""

print()

distance_swimming = 2
distance_cycling = 34
distance_running = 6
distance_per_day = distance_swimming + distance_cycling + distance_running
distance_after_day_1 = distance_per_day
distance_after_day_2 = distance_per_day * 2
distance_after_day_3 = distance_per_day * 3

def calculate_distances():
    print(distance_after_day_1, distance_after_day_2, distance_after_day_3)

calculate_distances()


"""
La cour de récréation de l'école a bien besoin d'être refaite : d'une part la clôture actuelle est trop rouillée pour résister à un Borlok, et d'autre part il faudrait couvrir le sol en terre par de belles pierres pour éviter d'avoir de la boue dès qu'il pleut.
Le professeur de la classe fait participer ses élèves : il leur demande de calculer l'aire et le périmètre du carré que forme leur cour de récréation. Les élèves n'ayant pas de règle assez longue, ils ont utilisé 4 bâtons de longueurs différentes pour mesurer le côté du carré. 
Afin d'aider les élèves dans leurs calculs, vous décidez d'écrire un programme.

Ce que doit faire votre programme :
La cour carrée a été mesurée avec quatre bâtons de longueurs respectives 17 m, 7 m, 5 m et 2 m. La longueur du côté de la cour est égale à 5 fois le premier bâton plus 2 fois le second plus 1 fois le troisième plus 2 fois le quatrième.
Votre programme doit afficher deux lignes : la première doit contenir la surface de la cour, et la seconde ligne doit contenir son périmètre. Les résultats doivent être exprimés en mètres carrés et en mètres, respectivement, mais vous ne devez pas afficher l'unité après la valeur numérique.
Important : dans votre programme, commencez par calculer la longueur du côté de la cour et l'enregistrer dans une variable.

"""

print()

stick1 = 17
stick2 = 7
stick3 = 5
stick4 = 2

length_of_side = 5 * stick1 + 2 * stick2 + 1 * stick3 + 2 * stick4
area = length_of_side ** 2
perimeter = 4 * length_of_side

def area_and_perimeter():
    print(area)
    print(perimeter)

area_and_perimeter()


print()

"""
À la récréation, vous croisez un groupe d'enfants qui vous proposent de participer à leur jeu. Vous acceptez de bon cœur et voilà votre robot engagé dans une partie de cache-cache !

Ce que doit faire votre programme :
Le robot devra compter jusqu'à 100, c'est à dire afficher les entiers de 1 à 100, un par ligne, et ensuite afficher « J'arrive ! ». Ainsi, s'il ne devait compter que jusqu'à 3 au lieu de 100, votre robot devrait afficher :

↳
1
2
3
J'arrive !
Important : votre programme ne doit pas faire plus d'une quinzaine de lignes.

"""


def hide_and_seek():
    for i in range(1, 101):
        print(i)
    print("J'arrive !")

hide_and_seek()


""" Orthonart, l'un des élèves de la classe, vous a demandé de lui apprendre à utiliser votre petit robot. Après lui avoir expliqué les bases de la programmation, vous lui prêtez le robot pendant une petite heure, le temps de planifier quelques projets avec le professeur de la classe. Lorsque vous revenez, vous décrouvrez qu'il a eu le temps d'écrire 7 programmes. Un bon nombre d'entre eux sont cependant invalides. Indiquez-lui lesquels afin qu'il puisse apprendre de ses erreurs.

Ce que doit faire votre programme :
Vous devez lire attentivement les programmes donnés ci-dessous pour déterminer s'ils sont valides ou non, et ce sans essayer de les exécuter. Pour chacun des 7 programmes, vous devez afficher sur une ligne soit la lettre « V » pour indiquer que le programme est valide, soit la lettre « I » pour indiquer qu'il est invalide. Par exemple, si vous pensez que les 4 premiers programmes s'exécuteront sans erreur et que les 3 suivants entraîneront des erreurs, faites afficher à votre programme :

↳
V
V
V
V
I
I
I

Voici les sept programmes.

1.
nbBillesRouges = 4
nbBillesBleues = 6
print(nbBillesRouges + nbBillesBleues)

2.
taille = 4
taille = 6
print(taille)

3.
nbBillesBleues = 3
print(nbBillesRouges)

4.
2 = 2
print(2)

5.
âge1 = 6
âge2 = 4
âge2 = âge1
print(âge2)

6.
prix = 10
prix - 2 = prix
print(prix)

7.
prix = âge - 7
âge = 12
print(prix)

"""

print()

valid = "V"
invalid = "I"

def check_programs():
    print(valid)  # Programme 1
    print(valid)  # Programme 2
    print(invalid)  # Programme 3
    print(invalid)  # Programme 4
    print(valid)  # Programme 5
    print(invalid)  # Programme 6
    print(invalid)  # Programme 7

check_programs()

"""
Afin d'amuser un groupe d'enfants, vous décidez de leur construire une fusée. 
Après leur avoir rappelé qu'il ne faut pas le faire sans un adulte, vous sortez un sachet de thé de votre poche et annoncez que ce sera votre fusée ! Incrédules, les enfants vous voient enlever l'agrafe, l'étiquette, vider le thé, et former un cylindre. 
Il ne reste plus qu'à allumer le haut du cylindre et faire le décompte avant le décollage de la fusée !

Ce que doit faire votre programme :
Votre programme devra lancer le décompte en partant de 100 puis annoncer le décollage, c'est-à-dire afficher une séquence d'annonces de la forme :

↳
100
99
...
2
1
0
Décollage ! 
en remplaçant les « … » par toutes les valeurs intermédiaires.

Important : votre programme ne doit pas faire plus d'une quinzaine de lignes.



"""
def rocket_takeoff():
    for i in range(100, -1, -1):
        print(i)
    print("Décollage !")

rocket_takeoff()


"""

L'automne ayant été très pluvieux, les Bufo Algo, une espèce locale de crapauds, se sont reproduits en grand nombre, et les habitants ont constaté que leur nombre doublait chaque semaine ! 
Leurs prédateurs naturels, les couleuvres (un type de serpent), sont complètement dépassés !

Avoir trop de crapauds est très gênant (on ne peut plus dormir) ! 
Les villageois décident donc d'élever un grand nombre de couleuvres avec lesquelles ils pourront contrôler le nombre de crapauds. 
Il leur faut tout d'abord estimer le nombre de crapauds qu'il y aura au cours des semaines qui viennent.
Ils vous demandent votre aide.

Ce que doit faire votre programme :
Sachant qu'il y a actuellement 1337 crapauds et que leur nombre double chaque semaine, votre programme devra afficher le nombre de crapauds qu'il y aura après la 12e semaine.

Important : vous devez utiliser une boucle pour calculer le nombre de crapauds.

"""

print()

def total_toads():
    toads_number = 1337
    total_of_toads = toads_number
    for _ in range(12):
        total_of_toads *= 2

    return total_of_toads
    
print(total_toads())
        


"""

C'est la dernière semaine de cours et l'école organise une grande kermesse. L'un des stands, « La foire aux bonbons », propose un jeu permettant de gagner des bonbons. Le jeu est simple : il faut atteindre le plus grand nombre de fois possible une cible sans jamais la rater. On peut gagner gros, car plus on touche la cible, et plus on gagne de bonbons à chaque fois qu'on touche la cible ! Les élèves aimeraient connaître le nombre de bonbons qu'ils peuvent gagner en fonction du nombre de tirs consécutifs réussis.

Ce que doit faire votre programme :
Toucher la cible au premier tir rapporte un bonbon, toucher la cible au deuxième tir rapporte deux bonbons de plus, la toucher au troisième tir rapporte encore trois bonbons de plus, etc. Écrivez un programme qui affiche sur la première ligne le nombre total de bonbons obtenus si l'on ne réussit qu'1 tir, puis qui affiche sur la deuxième ligne le nombre de bonbons récupérés si l'on réussit 2 tirs de suite, puis sur la troisième ligne le nombre de bonbons récupérés si l'on réussit 3 tirs de suite, etc. jusqu'à la valeur que l'on peut récupérer si l'on réussit 50 tirs de suite.

Par exemple, si votre programme s'arrêtait à 5 et non à 50, il devrait afficher ceci :

↳
1
3
6
10
15


"""

def total_candies():  
    total_of_candies = 1
    for i in range(1, 51):
        total_of_candies += i
        print(total_of_candies)
    
    
total_candies()

"""

Les enfants de la classe de maternelle décident de construire une très grande tour à l'aide de petits cubes en bois. 
Ils savent exactement la forme qu'ils souhaitent pour leur tour, mais ils n'arrivent pas à savoir s'ils auront suffisamment de cubes pour la construire. 
Ils vous demandent de les aider à calculer le nombre de cubes nécessaires.

Ce que doit faire votre programme :
L'objectif est de construire une tour à l'aide de petits cubes en bois, sachant que la forme de cette tour consiste en un ensemble de grands cubes placés les uns au-dessus des autres.
La base de la tour est un cube de taille 17×17×17, c'est-à-dire composé de 17×17×17 = 4 913 petits cubes. 
Sur ce cube est posé un autre cube de taille 15×15×15. 
Au-dessus de ce dernier se trouve un cube de 13×13×13. 
La tour continue ainsi jusqu'à atteindre le sommet, qui consiste en un cube de taille 1×1×1.

Votre programme doit calculer et afficher le nombre total de petits cubes nécessaires pour construire la pyramide. 
Effectuez les calculs dans le programme en y intégrant une boucle.

"""

def total_cubes():
    total_of_cubes = 0
    for i in range(17, 0, -2):
        total_of_cubes += i ** 3
    return total_of_cubes

print(total_cubes())

""""
C'est l'heure du cours de mathématiques et aujourd'hui les enfants vont travailler la multiplication. Malheureusement, l'institutrice ne retrouve que la petite table de multiplication, qui va jusqu'à 5 fois 5, mais pas la grande table, qui va jusqu'à 20 fois 20. Elle souhaiterait que vous lui imprimiez une nouvelle table allant jusqu'à 20 fois 20, pour qu'elle puisse l'afficher au mur.

Ce que doit faire votre programme :
Voici à quoi ressemble la table de multiplication allant jusqu'à 5 fois 5.

↳
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
Écrivez un programme qui affiche une table de multiplication allant jusqu'à 20 fois 20.

"""


def multiplication_table():
    for i in range(1, 21):
        for j in range(1 , 21):
            print(i * j, end=" ")
        print()

multiplication_table()
""""
Espion étranger

Le gouverneur de la ville vous a convoqué dans son bureau pour une affaire d'une extrême importance. 
En effet, un espion étranger s'est introduit dans la ville et il faut absolument le démasquer. 
Heureusement, grâce à des informateurs grassement payés, on sait à quelques jours près à quelle date l'espion est arrivé. 
Il suffira donc de regarder les registres des entrées de la ville puis d'aller interroger toutes les personnes correspondantes.

Pour avoir une idée de l'ampleur de la tâche, le roi vous a demandé de calculer le nombre de personnes qu'il faudra interroger.

Ce que doit faire votre programme :
On vous donne un intervalle de temps pendant lequel on sait qu'un espion est arrivé, puis la date d'arrivée d'un certain nombre de personnes. 
Déterminez combien de ces personnes peuvent être cet espion.

Votre programme doit d'abord lire deux entiers : la date de début et la date de fin de l'intervalle pendant lequel on sait que l'espion est arrivé en ville. 
Il doit ensuite lire un entier nbEntrées, le nombre total de personnes entrées dans la ville, puis les nbEntrées nombres suivants qui représentent les dates d'entrée (non triées) des différentes personnes.

Votre programme doit afficher le nombre de personnes entrées entre les deux dates données, incluses.

Exemple
entrée :

6
10
5
7
11
8
3
6
sortie :

3
Commentaires
Dans l'exemple, l'espion est entré dans la ville entre le jour 6 et le jour 10, et 5 personnes sont enregistrées dans les données de la ville. 

Pour chaque personne Pi, on a représenté sa date d'entrée dans la ville avec une barre (accompagnée du numéro de la personne). 
On voit que 3 dates se trouvent dans l'intervalle.

"""

# start_date = int(input())
# end_date = int(input())
# entries_number = int(input())
# suspected_persons = 0

# for entry in range (entries_number):
#   arrival_date = int(input())

#   if start_date <= arrival_date <= end_date:
#     suspected_persons += 1

# print(suspected_persons)

"""
On sait qu'un espion est présent dans la ville mais, grâce à des recoupements d'informations, il a été possible de déterminer que l'espion était forcément dans une certaine zone de la ville. 
Le gouverneur va donc envoyer des soldats fouiller chaque maison et interroger les habitants. 
Afin de pouvoir estimer combien de temps va durer l'opération, il souhaiterait savoir combien de maisons sont présentes dans la zone en question.

Ce que doit faire votre programme :
On vous décrit une zone de recherche rectangulaire, parallèle aux axes, puis la position d'un certain nombre de maisons. 
Écrivez un programme qui détermine combien de maisons sont dans cette zone.

Votre programme devra lire, dans l'ordre : l'abscisse minimale, l'abscisse maximale, l'ordonnée minimale et l'ordonnée maximale du rectangle. 
Il lira ensuite le nombre total de maisons, puis pour chaque maison, son abscisse et son ordonnée.

Votre programme devra déterminer puis afficher le nombre de maisons qui se trouvent dans la zone de recherche. 
Si une maison est exactement sur le bord de la zone, elle doit ête comptée.

"""

# min_axis_x = int(input())
# max_axis_x = int(input())
# min_axis_y = int(input())
# max_axis_y = int(input())
# houses_in_the_zone = 0

# houses_number = int(input())

# for house in range(houses_number):
#   axis_x = int(input())
#   axis_y = int(input())
#   if min_axis_x <= axis_x <= max_axis_x and min_axis_y <= axis_y <= max_axis_y:
#     houses_in_the_zone += 1

# print(houses_in_the_zone)

"""

Nombre de jours dans le mois

Les soldats de la garnison de la ville sont payés à la journée et pas au mois, ce qui fait que leur salaire n'est pas le même selon le mois. Le trésorier étant malade et les soldats voulant être payés vous vous proposez pour le remplacer. Certains soldats revenant de mission à l'extérieur, ils doivent recevoir leur paye pour les mois précédents également. Afin de ne pas faire d'erreur, vous décidez d'écrire un programme pour vous aider.

Ce que doit faire votre programme :
Écrivez un programme qui lit un numéro de mois algoréen, et affiche le nombre de jours de celui-ci. Les Algoréens disposent de leur propre calendrier. Voici les informations dont vous avez besoin :

Numéro du mois	Nombre de jours
1	30
2	30
3	30
4	31
5	31
6	31
7	30
8	30
9	30
10	31
11	29
Exemple
entrée :

6
sortie :

31

"""

# month_number = int(input())

# if month_number == 11:
#   print(29)
# elif 4 <= month_number <= 6 or month_number == 10:
#   print(31)
# else:
#   print(30)

"""
Amitié entre gardes

Comme dans tout métier, certains soldats sont devenus amis, et on peut facilement dire si deux soldats sont amis : si à un moment ils sont de garde en même temps alors ils sont amis, sinon ils ne le sont pas. Afin de développer les relations amicales entre les soldats, le colonel en charge des tours de garde souhaiterait autant que possible mettre en binôme des soldats qui ne sont pas encore amis. Il vous demande votre aide pour déterminer si deux soldats sont amis ou pas.

Ce que doit faire votre programme :
Vous devez écrire un programme qui détermine si deux soldats ont été de garde en même temps.

Votre programme doit lire quatre entiers : la date du début et la date de fin (incluse) du service du premier soldat puis celles du second soldat.

Si les deux soldats ont, à un moment (même une seule seconde), été de garde en même temps le programme devra écrire "Amis" et sinon "Pas amis".

Exemples
Exemple 1
entrée :

2
5
3
6
sortie :

Amis
Exemple 2
entrée :

1
5
10
15
sortie :

Pas amis
Exemple 3
entrée :

2
4
4
6
sortie :

Amis


"""

# soldier_1_start_date = int(input())
# soldier_1_end_date = int(input())
# soldier_2_start_date = int(input())
# soldier_2_end_date = int(input())

# if soldier_2_end_date < soldier_1_start_date or soldier_1_end_date < soldier_2_start_date:
#   print("Pas Amis")
# else:
#   print("Amis")

"""
Le gouverneur a organisé une petite fête à laquelle tous les notables étaient invités. Il souhaiterait à présent faire réaliser une petite affiche vantant le succès de la fête et indiquant en particulier le nombre de personnes présentes au moment le plus intense de la fête.

Ce que doit faire votre programme :
On vous décrit les arrivées et départs des participants d'une fête, et votre programme doit afficher le nombre maximum de personnes qui ont été présentes au même moment. Chacun des invités est identifié par un numéro.

Le premier entier à lire est nbPersonnes : le nombre total de personnes qui se sont rendues à la fête. Ensuite, il y a 2 × nbPersonnes entiers à lire, dans l'ordre chronologique des arrivées et départs. Si l'entier est positif, c'est que la personne de numéro correspondant vient d'arriver, s'il est négatif, elle vient de partir. Une fois qu'une personne est partie, elle ne revient pas.

Votre programme doit déterminer puis afficher le nombre maximum de personnes qui étaient là simultanément.

Exemple
entrée :

5
1
2
-1
3
4
-2
-4
5
-3
-5
sortie :

3
Commentaires
Au cours de la fête décrite par l'exemple, on a donc les flux suivants :

l'invité n°1 entre ;
l'invité n°2 entre ;
l'invité n°1 sort ;
l'invité n°3 entre ;
l'invité n°4 entre ;
l'invité n°2 sort…
Le nombre de présents est maximal lors de l'arrivée de la personne n°4 : il y a alors trois invités qui sont arrivés et restés.


"""

guests_number = int(input())

guests_presents = 0
max_guests_presents = 0

for guest in range (2 * guests_number):
  guests_arrival_or_departure = int(input()) 

  if guests_arrival_or_departure > 0:
    guests_presents += 1
  else:
    guests_presents -= 1

  if guests_presents > max_guests_presents:
      max_guests_presents = guests_presents

print(max_guests_presents)




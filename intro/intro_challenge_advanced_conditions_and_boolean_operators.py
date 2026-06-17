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

min_axis_x = int(input())
max_axis_x = int(input())
min_axis_y = int(input())
max_axis_y = int(input())
houses_in_the_zone = 0

houses_number = int(input())

for house in range(houses_number):
  axis_x = int(input())
  axis_y = int(input())
  if min_axis_x <= axis_x <= max_axis_x and min_axis_y <= axis_y <= max_axis_y:
    houses_in_the_zone += 1

print(houses_in_the_zone)

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

month_number = int(input())

if month_number == 11:
  print(29)
elif 4 <= month_number <= 6 or month_number == 10:
  print(31)
else:
  print(30)

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

soldier_1_start_date = int(input())
soldier_1_end_date = int(input())
soldier_2_start_date = int(input())
soldier_2_end_date = int(input())

if soldier_2_end_date < soldier_1_start_date or soldier_1_end_date < soldier_2_start_date:
  print("Pas Amis")
else:
  print("Amis")

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


"""
Casernes de pompiers

La ville comprend de nombreuses casernes de pompiers et chacune a sa propre zone d'intervention qui lui est réservée. 
Cependant en regardant ces zones il vous semble qu'elles ne sont pas très bien choisies car parfois elles se recoupent alors que certains endroits de la ville sont en dehors de toutes les zones et donc ne sont pas protégées par les pompiers. 
Vous décidez d'aider le maire à mieux organiser l'action des pompiers.

Ce que doit faire votre programme :
Votre programme doit lire la description de plusieurs paires de zones rectangulaires, et pour chaque paire, déterminer si les deux zones s'intersectent.

Vous devez lire un premier entier, le nombre de paires de zones que votre programme devra tester. 
Ensuite, pour chaque paire possible, deux zones rectangulaires et parallèles aux axes vous sont données l'une après l'autre. 
Chaque zone est décrite par 4 entiers : son abscisse minimale et maximale puis son ordonnée minimale et maximale.

Sur cet exemple, la zone du bas est donc décrite par les 4 entiers (1, 6, 1, 5) et l'autre par (4, 9, 3, 8) :

"""
number_of_pairs = int(input())

for pair in range(number_of_pairs):
  min_x_zone_1 = int(input())
  max_x_zone_1 = int(input())
  min_y_zone_1 = int(input())
  max_y_zone_1 = int(input())
  min_x_zone_2 = int(input())
  max_x_zone_2 = int(input())
  min_y_zone_2 = int(input())
  max_y_zone_2 = int(input())

  if (max_x_zone_1 <= min_x_zone_2 or max_x_zone_2 <= min_x_zone_1) or (max_y_zone_1 <= min_y_zone_2 or max_y_zone_2 <= min_y_zone_1):
    print("NON")
  else:
    print("OUI")

"""
Personne disparue

Un personnage important de la cité n'est pas rentré chez lui hier soir et tout le monde est à sa recherche. 
Or tout habitant de la ville a un numéro unique qui lui est associé et doit signer une sorte de registre quand il sort de la ville. 
Vous souhaitez savoir si le registre a été signé, auquel cas il faudra étendre les recherches à l'extérieur de la ville.

Ce que doit faire votre programme :
On vous donne un entier, le numéro d'une personne recherchée, puis un entier tailleListe, et enfin tailleListe entiers parmi lesquels vous devez chercher le numéro de la personne. 
Si le numéro est présent dans la liste (il peut l'être plusieurs fois) vous devez afficher le texte "Sorti de la ville" sinon "Encore dans la ville".

Exemple
entrée :

42
5
1
7
172
2
41
sortie :

Encore dans la ville


"""

wanted_person = int(input())
number_of_people_outside = int(input())

is_out = False

for people in range(number_of_people_outside):
  identity_number = int(input())
  if identity_number == wanted_person:
    is_out = True

if is_out:
  print("Sorti de la ville")
else:
  print("Encore dans la ville")


"""
La grande fête

Un espion était présent à la grande fête organisée la semaine dernière par le gouverneur. 
Bien qu'on n'ait pas pu l'identifier, on a réussi à intercepter son rapport et à estimer en fonction de ce qu'il a pu voir, à quelle période il a été présent. 
Sachant pour chaque invité sa date d'arrivée et de départ, on aimerait interroger tous les suspects potentiels. 
Vous souhaitez savoir combien de suspects il faudra interroger.

Ce que doit faire votre programme :
On vous donne une période de temps à étudier, et les dates d'arrivée et de départ d'un certain nombre d'invités d'une fête. 
Écrivez un programme qui détermine combien d'invités ont été présents à un moment de la période étudiée.

Votre programme doit d'abord lire deux entiers : la date de début et la date de fin de la période étudiée. L'entier suivant, nbInvites, est le nombre total d'invités. 
Pour chaque invité, votre programme doit ensuite lire deux entiers : sa date d'arrivée et de départ. 
Un invité est suspect si la période à laquelle il a été présent intersecte la période étudiée. 
Votre programme doit afficher le nombre d'invités suspects.

Exemple
entrée :

8
12
5
4
7
2
11
3
6
1
8
14
19
sortie :

2


"""

start_date = int(input())
end_date = int(input())
total_guests = int(input())
number_of_suspects = 0

for guest in range(total_guests):
  start_date_guest = int(input())
  end_date_guest = int(input())

  if start_date_guest <= end_date and end_date_guest >= start_date :
    number_of_suspects += 1

print(number_of_suspects)

"""
L'espion est démasqué !

Grâce à un certain nombre d'informateurs plus ou moins fiables, le chef de la police a recueilli des indications qui devraient lui permettre enfin de démasquer cet espion qui lui échappe depuis des semaines. 
La population de la ville étant relativement importante, il vous demande votre aide afin d'automatiser un peu les choses. 
Vous devez estimer la probabilité qu'une personne soit un espion.

Ce que doit faire votre programme :
Votre programme doit lire entier : un nombre de personnes à considérer. Ensuite, pour chaque personne, il doit lire son signalement sous la forme de cinq entiers : sa taille en centimètres, son âge en années, son poids en kilogrammes, un entier valant 1 si la personne possède un cheval et 0 sinon, et un entier valant 1 si la personne à les cheveux bruns et 0 sinon.

On veut déterminer pour chaque personne à quel point elle correspond aux 5 critères suivants :

il aurait une taille supérieure ou égale à 178 cm et inférieure ou égale à 182 cm ;
il aurait au moins 34 ans ;
il pèserait strictement moins de 70 kg ;
il n'a pas de cheval ;
il a les cheveux bruns.
Lorsque cela n'est pas précisé explicitement, les inégalités sont au sens large.

Pour chaque personne, vous devez tester tous les critères. S'ils sont vérifiés tous les 5, vous devez afficher « Très probable ». 
Si seulement 3 ou 4 sont vérifiés, vous devez afficher « Probable ». 
Si aucun n'est vérifié, vous devez afficher « Impossible », et dans les autres cas, vous devez afficher « Peu probable ».

Exemple
entrée :

1
180
40
65
0
1
sortie :

Très probable

"""

number_of_suspects = int(input())

for suspect in range(number_of_suspects):
  height = int(input())
  age = int(input())
  weight = int(input())
  has_horse = int(input())
  brown_hair = int(input())
  criteria = 0

  if 178 <= height <= 182:
    criteria += 1
  if age >= 34:
    criteria += 1
  if weight < 70:
    criteria += 1
  if not has_horse:
    criteria += 1
  if brown_hair:
    criteria += 1

  if criteria == 5:
    print("Très probable")
  elif criteria == 3 or criteria == 4:
    print("Probable")
  elif criteria == 0:
    print("Impossible")
  else:
    print("Peu probable")


"""
Zones de couleurs

Un espion a été démasqué dans la ville où vous vous trouvez. Son interrogatoire n'a pas été très fructueux : la seule chose que vous savez, c'est qu'il espionnait les savants de l'université, une puissance étrangère étant intéressée par leurs recherches. 
Vous vous rendez donc à l'université pour discuter avec les chercheurs mais à peine arrivé, vous êtes recruté comme assistant par le laboratoire d'étude du comportement humain.

Celui-ci réalise une expérience consistant à demander à plusieurs personnes de placer chacune un jeton sur une table contenant des zones de différentes couleurs. 
Les chercheurs souhaitent ainsi étudier si le choix de la zone où une personne place son jeton est lié à la couleur des vêtements qu'elle porte.

Ce que doit faire votre programme :
Sur une table est placée une feuille de papier rectangulaire de 90 cm de large et 70 cm de haut, composée de zones de différentes couleurs, comme le décrit la figure ci-dessous. 
Un certain nombre de personnes placent l'une après l'autre un jeton où elles le souhaitent sur la table, à l'exception des frontières entre les différentes zones.

On vous donne en entrée le nombre de jetons qui ont été déposés, puis, pour chaque jeton, ses coordonnées sur la feuille par rapport à l'origine en haut à gauche, sous la forme d'une abscisse et d'une ordonnée entre −1 000 et 1 000.

Votre programme devra qualifier chaque jeton avec l'un des textes suivants, en fonction de la couleur sur laquelle il se trouve :

« En dehors de la feuille »
« Dans une zone jaune »
« Dans une zone bleue »
« Dans une zone rouge »
Essayez d'écrire votre programme de sorte qu'il y ait au maximum une condition par possibilité de texte affiché.

Exemple
entrée :

4
16
12
30
22
64
62
-5
86
sortie :

Dans une zone bleue
Dans une zone jaune
Dans une zone rouge
En dehors de la feuille
Commentaires
Dans l'exemple, on a 4 jetons, de coordonnées (16 ; 12), (30 ; 22), (64 ; 62) et (-5 ; 86).

"""
number_of_tokens = int(input())

for token in range(number_of_tokens):
  axis_x = int(input())
  axis_y = int(input())

  if axis_x < 0 or axis_x > 90 or axis_y < 0 or axis_y > 70:
    print("En dehors de la feuille")
  elif ((15 <= axis_x <= 45 or 60 <= axis_x <= 85) and (60 <= axis_y <= 70)):
    print("Dans une zone rouge")
  elif ((10 <= axis_x <= 85 and 10 <= axis_y <= 55) and not (25 <= axis_x <= 50 and 20 <= axis_y <= 45)):
    print("Dans une zone bleue")
  else:
    print("Dans une zone jaune")
  





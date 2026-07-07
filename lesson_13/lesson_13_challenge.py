# Essayer de réaliser chacune des missions suivantes avec une syntaxe classique et ensuite avec une syntaxe courte en une seule ligne.

# Une fonction qui convertit des montants en dollars vers des montants en euros (prends le cours euro/dollar du jour où tu fais la quête).

conv = 0.88
conv_dollars_euros = lambda dollars: f"{dollars * conv:.2f}, €"

print(conv_dollars_euros(1000))

# Une fonction qui renvoie la somme des nombres pairs présents dans une liste contenant des nombres entiers.

integers = [1, 2, 3, 4, 5, 6, 7]
even_numbers_sum = sum(i for i in integers if i % 2 == 0)
print(even_numbers_sum)

# Une fonction qui convertit une liste de nombres entiers positifs ou négatifs) en une nouvelle liste contenant leurs valeurs absolues.
# Tu peux prendre la liste suivante pour exemple :

test_list = [0, 3, -6, 9, 12, -15, 18, -21, 24, 27]

abs_values_list = [abs(i) for i in test_list]

print(abs_values_list)

# Other way to do it:

integers_list =[0, 3, -6, 9, 12, -15, 18, -21, 24, 27, -122, 588]

absolute_values = [-i if i < 0 else i for i in integers_list]

print(absolute_values)
# Challenge lesson_02

# 1. Calcul d'un prix

# Ecrivez un programme faisant saisir à l’utilisateur un prix unitaire HT, 
# un taux de TVA et un nombre d’articles, 
# et qui calcule le montant TTC de l’achat.
# Affichez le montant TTC.

unit_price = float(input("Saisissez le prix unitaire : "))
vat = float(input("Saisissez le taux de TVA : "))
articles_number = int(input("Saisissez le nombre d'articles : "))
HT_amount = float(unit_price * articles_number)
VAT_amount = float(HT_amount * vat)/100
TTC_amount = float(HT_amount + VAT_amount)
print("Le montant TTC de votre commande est de : ", TTC_amount)


# 2. Conversion de durées (1)

# Ecrivez un programme demandant une durée en secondes à l’utilisateur, et qui la convertit en heures, minutes, secondes.
# Affichez le résultat.
# Par exemple 12334 deviendra 3 heures, 25 minutes et 34 secondes.


duration = int(input("Saisissez la durée en secondes : "))

duration_hour = (duration // 3600)
duration_hour_rest = duration % 3600

duration_min = duration_hour_rest // 60
duration_min_rest = duration_hour_rest % 60

duration_sec = duration_min_rest

print("La durée exacte de votre intervention est de " + str(duration_hour) + " heures, " + str(duration_min) + " minutes et " + str(duration_sec) + " secondes.")


# 3. Conversion de durées (2)

# Ecrivez un programme demandant une durée en heures, minutes, secondes à l’utilisateur et qui la convertit en secondes.
# Affichez le résultat.
# Par exemple 3 heures, 25 minutes et 34 secondes deviendra 12334 secondes.

duration_hour = int(input("Saisissez le nombre d'heures : "))
duration_min = int(input("Saisissez le nombre de minutes : "))
duration_second = int(input("Saississez le nombre de secondes : "))
duration_from_hours = duration_hour * 3600
duration_from_min = duration_min * 60
total_duration_in_second = duration_from_hours + duration_from_min + duration_second
print("Le durée totale est de " + str(total_duration_in_second) + " secondes.")
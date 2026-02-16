salaire_annuel = 36000
nb_mois = 12
print(salaire_annuel)
print(nb_mois)
print()

salaire_mensuel = salaire_annuel/nb_mois
print(f"Salaire mensuel : {int(salaire_mensuel)}")
print()

salaire_annuel2 = 40000
prenom = "Lionel"
print(type(salaire_annuel))
print(type(prenom))
print()

age_str = "25"
age_int = int(age_str)
print(type(age_str))
print(type(age_int))
print()

salaire_annuel = 36000
salaire_str = str(salaire_annuel)
print(type(salaire_annuel))
print(type(salaire_str))
print()

age_flottant = float(age_int)
print(age_flottant)

nom = input("Quel est ton nom ?\n")
print("Bonjour, " + nom + " !")
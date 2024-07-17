import random

# Creation du tableau aleatoire
tab = []
for i in range(10):
    rng = random.randrange(0, 11)
    tab.append(rng)
print(tab)

# Demande à l'utilisateur
target = int(input("Valeur chercher : "))

# Recherche de l'élément et stock de l'index
resultat = set()
for index, valeur in enumerate(tab):
    if valeur == target:
        resultat.add(index)

# Affichage du resultat
if len(resultat) > 0:
    msg = "aux positions" if len(resultat) > 1 else "à la position"

    print("La valeur a été trouvée", msg, ": ", end="")

    for elem in resultat:
        position = elem + 1  # "+1" pour la position "compté" et non l'index
        print(position, " ", end="")
    print()
else:
    print("Valeur non trouvée")
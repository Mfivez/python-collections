import random

# Generation d'un tableau aleatoire trié
tab = []
tab.append(random.randrange(0, 10))

for i in range(1, 5):
    tab.append(random.randrange(tab[i - 1], tab[i - 1] + 10))

# Pour l'exercice :
# - Pas de fonction insert / remove

quitter = False

while not quitter:
    print(tab)
    choice = input("Ajouter (+) / Supprimer (-) / Quitter (q) : ")

    if choice == "q":
        quitter = True
    elif choice == "+" or choice == "-":

        nombre = int(input("Nombre : "))

        if choice == "+":
            if nombre > tab[len(tab) -1]:
                tab.append(nombre)
            else:
                # Recherche position
                target = 0
                while nombre > tab[target]:
                    target += 1

                # tab.insert(target, nombre)

                # tab_av = tab[:target]
                # tab_av.append((nombre))
                # tab = tab_av + tab[target:]

                tab = tab[:target] + [nombre] + tab[target:] # Spécifique au Python


        else:
            # Suppression
            trouve = False
            i = 0
            while not trouve and i < len(tab):
                if tab[i] == nombre:
                    trouve = True
                else:
                    i += 1

            if trouve:
                tab = tab[:i] + tab[i+1:] # Spécifique au Python

    else:
        print("Choix non-supporté")

print("Au revoir")

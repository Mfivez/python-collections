import random as rng

tab = [3, 11, -5, 5, 13, 42, 25, 10, 7, 14, -2, 10]

# Affichage du tableau initial
for elem in tab:
    print(elem, end=" > ")
print()

print("Trie... Ceci peut prendre du temps!")

# Algo de tri aleatoire https://fr.wikipedia.org/wiki/Tri_stupide
nb_iteration = 0
est_trier = False
taille = len(tab)

while not est_trier:
    nb_iteration += 1
    nb_inversion = rng.randrange(10, 51)

    # Melange
    for i in range(nb_inversion):

        cible_a = rng.randrange(0, taille)
        cible_b = rng.randrange(0, taille)

        temp = tab[cible_a]
        tab[cible_a] = tab[cible_b]
        tab[cible_b] = temp

    # Verrif si trier
    count = 0
    est_trier = True
    while est_trier and count < taille - 1:
        if tab[count] > tab[count + 1]:
            est_trier = False
        count += 1


# Affichage du tableau trier
for elem in tab:
    print(elem, end=" > ")
print()
print("Nombre d'iteration", nb_iteration)
import random
TAILLE = 10

# Initialisation la collection
tab = []
for i in range(0, TAILLE):
    # valeur = random.randint(0, 10)
    valeur = random.randrange(0, 11, 1)
    tab.append(valeur)

print("Valeur initial :", tab)

# Inversion du tableau (Swap)
for i in range(TAILLE // 2):
    pos = TAILLE - 1 - i

    # Swap avec variable temp
    temp = tab[i]
    tab[i] = tab[pos]
    tab[pos] = temp

    # Swap sans variable - Math ♥
    # tab[i] = tab[pos] + tab[i]
    # tab[pos] = tab[i] - tab[pos]
    # tab[i] = tab[i] - tab[pos]

    # Swap sans variable - Python
    # tab[i], tab[pos] = tab[pos], tab[i]

print("Valeur inversé :", tab)


# Inversion du tableau (Ajout / Supp)
target = TAILLE - 1
while target >= 0:
    tab.append(tab[target])
    tab.pop(target)

    target -= 1

print("Valeur ré-inversé :", tab)
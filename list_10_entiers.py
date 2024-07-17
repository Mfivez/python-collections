LIMITE = 10
tab = [2]

for i in range(1, LIMITE):
    tab.append(tab[i]*2)


# print(tab)

# Sans recup l'index
for item in tab:
    if item == tab[LIMITE-1]:
        espace = "."    # Bug possible, si la dernier valeur est répété dans la liste
    else:
        espace = " > "
    print(item, end=espace)

print()

# Recuperation de l'index (sans range())
for index, valeur in enumerate(tab):
    sym = " > "
    if index == LIMITE-1:
        sym = "."

    elem = str(valeur) + sym
    print(elem, end="")


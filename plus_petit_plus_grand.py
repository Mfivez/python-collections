NB_VALEUR = 10

# Saisie utilisateur
tab = []
for i in range(NB_VALEUR):
    valeur = int(input("Valeur " + str(i + 1) + " : "))
    tab.append(valeur)


min = tab[0]
max = tab[0]

for i in range(1, len(tab)):

    if tab[i] < min:
        min = tab[i]

    elif tab[i] > max:
        max = tab[i]

print("Min :", min)
print("Max :", max)

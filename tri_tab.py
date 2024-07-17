tab = [4, 42, 5, 10, 3, -5, 3, 25]
#      0   1  2   3  4   5  6   7

index_current = 0
while index_current < len(tab) - 1:
    index_min = index_current
    k = index_current + 1

    # Recherche de l'index du plus petit
    while k < len(tab):
        if tab[k] < tab[index_min]:
            index_min = k
        k += 1

    # Inversion
    if index_current != index_min:
        temp = tab[index_current]
        tab[index_current] = tab[index_min]
        tab[index_min] = temp

    index_current += 1


print(tab)


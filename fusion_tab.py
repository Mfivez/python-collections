tab1 = [ 5,  42,  3, 10, -5, 6, 8]
tab2 = [-2, 10, 40, 25, 2]


fusion = []

taille = len(tab2)
if len(tab1) > len(tab2):
    taille = len(tab1)

# taille = len(tab1) if len(tab1) > len(tab2) else len(tab2)

for i in range(0, taille):

    if(i < len(tab1) and i < len(tab2)):
        if(tab1[i] < tab2[i]):
            temp = [tab1[i], tab2[i]]
        else:
            temp = [tab2[i], tab1[i]]
    else:
        if len(tab1) > len(tab2):
            temp = [tab1[i]]
        else:
            temp = [tab2[i]]


    if len(fusion) == 0:
        fusion.extend(temp)
        print(fusion)

    else:
        k = 0
        target = 0
        while target < len(temp) and k < len(fusion) :

            if(temp[target] < fusion[k]):
                fusion.insert(k, temp[target])
                target += 1
            elif k >= len(fusion) - 1:
                fusion.append(temp[target])
                target += 1

            k += 1


        print(fusion)

# Import d'un lib pour la console windows uniquement!
# https://docs.python.org/2/library/msvcrt.html
import msvcrt as m


SYM_CASE = "_"
SYM_PION = "X"
TAILLE_ZONE = 10

game = list()   # equivaut à []
position = 0


# Zone initial
for i in range(0, TAILLE_ZONE, 1):
    game.append(SYM_CASE)
game[position] = SYM_PION


# Zone de jeu
quitter = False

print("Q : Gauche / D : Droite / E : Quitter")
while not quitter:
    # Affichage
    for case in game:           # for i in range(TAILLE_ZONE):
        print(case, end="")     #    print(game[i], end="")
    print()                     # print()

    # Lecture clavier
    # choice = input()
    choice = m.getwch()     # Attention, ne fonctionne pas avec la console de PyCharm!!!
    choice = choice.lower()

    if choice != "e":
        # Deplacement du pion
        game[position] = SYM_CASE

        if choice == "q" and position > 0:
            position -= 1
        elif choice == "d" and position < TAILLE_ZONE - 1:
            position += 1

        game[position] = SYM_PION

    else:
        quitter = True

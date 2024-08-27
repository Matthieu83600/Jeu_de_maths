import random

NB_MIN = 1
NB_MAX = 10
NB_QUESTIONS = 4
nb_points = 0
moyenne_points = int(NB_QUESTIONS / 2)

def poser_question():
    a = random.randint(NB_MIN, NB_MAX)
    b = random.randint(NB_MIN, NB_MAX)
    o = random.randint(0, 3)
    operateur_str = "+"
    if o == 1:
        operateur_str = "*"
    elif o == 2:
        operateur_str = "-"
    elif o == 3:
        operateur_str = "/"

    response_str = input(f"Calculez : {a} {operateur_str} {b} = ")
    response_float = float(response_str)

    calcul = a + b
    if o == 1:
        calcul = a * b
    elif o == 2:
        calcul = a - b
    elif o == 3:
        calcul = a / b

    if response_float == calcul:
        return True
    else:
        return False

for i in range (0, NB_QUESTIONS):
    print(f"Question n°{i+1} sur {NB_QUESTIONS} : ")
    if poser_question():
        nb_points += 1
        print("Reponse correcte.")
    else:
        print("Réponse incorrecte.")
    print()

print(f"Votre note est : {nb_points} / {NB_QUESTIONS}.")
if nb_points == NB_QUESTIONS:
    print("Excellent !")
elif moyenne_points < nb_points < NB_QUESTIONS:
    print("Pas mal")
elif moyenne_points >= nb_points > 0:
    print("Peut mieux faire")
elif nb_points == 0:
    print("Révisez vos maths")
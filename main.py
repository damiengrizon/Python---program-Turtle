import turtle


# faire une fonction  escalier qui prends en parametre( taille de pixel et nombre de marche


# def escalier(taille, nb):
#     for i in range(0, nb):
#         t.forward(taille)
#         t.left(90)
#         t.forward(taille)
#         t.right(90)
#         taille = taille - 1
#     t.forward(taille)
#     turtle.done()


def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)


def carres(taille_depart, nb):
    for i in range(1, nb):
        taille = taille_depart * (i+1)
        carre(taille)


def carres_bouge(taille_depart, nb):
    for i in range(1, nb):
        taille = taille_depart * (i+1)
        carre(taille)
        t.left(10)


t = turtle.Turtle()

# escalier(30, 5)
carres_bouge(35, 5)
turtle.done()

# t.forward(100)
# t.left(90)
# t.forward(50)
# t.backward(100)
# t.right(45)
# t.forward(50)

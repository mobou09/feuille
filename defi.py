from functools import cache
import timeit
import math
import turtle


def diviseur(n):
    liste = []
    for i in range(1, n//2+1):
        if n % i == 0:
            liste.append(i)
    return liste


@cache
def nombre_ami(x):
    resultat = []
    for i in range(1, x+1):
        divi_1 = diviseur(i)
        somme_1 = sum(divi_1)
        divi_2 = diviseur(somme_1)
        somme_2 = sum(divi_2)
        if somme_2 == i and somme_1 != i:
            if somme_1 > i:
                tu = (i, somme_1)
            else:
                tu = (somme_1, i)
            if tu not in resultat:
                resultat.append(tu)
    return resultat

def c_temps(x):
    T = []
    N = []
    for nombre in range(x):
        N.append(nombre+1)
        T.append(timeit.timeit(nombre_ami(x)))
    return N, T



def nombre_ami_v_2(x):
    pass

def ecriteur(nom, chaine):
    a = open(nom+".txt", "w")
    a.write(chaine)
    a.close()

chc = "mohamedyounesomarmarwanismailwafa\nmathiaspythonfreecadpygame"


def compteur(nom):
    compte = 0
    with open(nom) as file:
        texte = file.read()
    for char in texte:
        if char >= 'A' and char <= 'z':
            compte += 1
    list_of_words = texte.split()
    nombre = len(list_of_words)
    return compte, nombre

def volume(rayon):
    calcule = 4/3*math.pi*rayon**3
    return calcule

def poly(n, l, tortue):
    angle = 360/n
    for i in range(n):
        tortue.forward(l)
        tortue.left(angle)


def dessin_geometrique(l, h):
    turtle.Screen().setup(l, h)
    t = turtle.Turtle()
    t.penup()
    t.goto(-l/5, h/6)
    t.pendown()
    poly(4, l/10, t)
    t.penup()
    t.goto(l/5, h/4)
    t.pendown()
    poly(3, l/10, t)
    t.penup()
    t.goto(l/5, -h/8)
    t.pendown()
    t.circle(l/10)
    t.penup()
    t.goto(-l/5, -h/8)
    t.pendown()
    poly(5, l/10, t)

    turtle.Screen().exitonclick()

dessin_geometrique(400, 300)

def carre(n):
    calcule = n**2
    return calcule

def quatre(f, n):
    return f(n)*4


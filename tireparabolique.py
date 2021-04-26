import turtle
import datetime
import math
import random

def x(x0, v0, t):
    return x0 + v0*t


def y(y0, v0, t, a):
    pos = y0 + v0*t + 0.5*a*t**2
    v = v0 + a*t
    return pos, v


def trajectoire(x0, y0, v, angle, t, a, vent):
    angle_rad = math.radians(angle)
    vx0 = v*math.cos(angle_rad)
    vy0 = v*math.sin(angle_rad)
    posx = x(x0, vx0 + vent, t)
    posy, vy = y(y0, vy0, t, a)
    dire = math.degrees(math.atan(vy/vx0))
    return posx, posy, vx0, vy, dire


w = 1200
h = 700
turtle.setup(w, h)
turtle.title("tire parabolique")
projectile = turtle.Turtle()
projectile.hideturtle()
projectile.penup()
joueur_1 = turtle.Turtle(shape='square')
joueur_2 = turtle.Turtle(shape='triangle')
joueur_1.penup()
joueur_2.penup()
joueur_1.color("#F50B0B")
joueur_2.color("#2F8AD0")
joueur_1.shapesize(1, 1, 12)
joueur_2.shapesize(1, 1, 12)
wind = 0
effaceur = turtle.Turtle()
effaceur.color("white")
effaceur.pensize(6)
effaceur.penup()
effaceur.hideturtle()
joueur_1.hideturtle()
joueur_2.hideturtle()
PX_1 = random.randint(-400, -200)
PY_1 = random.randint(-300, 0)
PX_2 = random.randint(200, 400)
PY_2 = random.randint(-300, 0)
joueur_1.goto(PX_1, PY_1)
joueur_2.goto(PX_2, PY_2)
joueur_1.pendown()
joueur_2.pendown()
joueur_1.showturtle()
joueur_2.showturtle()

deltat = 0.01*10**6

while True:
    vitor = int(turtle.numinput("vitesse", "quel vitesse voulez vous utiliser j1? "))
    angor = int(turtle.numinput("angle", "quel angle voulez vous utiliser j1? "))
    projectile.setheading(angor)
    t1 = datetime.datetime.now()
    t2 = t1 + datetime.timedelta(milliseconds=5)
    D = t2 - t1
    Y = 1
    X = 1
    T = 0
    projectile.hideturtle()
    projectile.penup()
    projectile.goto(PX_1, PY_1)
    projectile.showturtle()
    projectile.pendown()
    while True:
        if D.microseconds > deltat:
            T += D.microseconds
            X, Y, _1, _2, DI = trajectoire(0, 0, vitor, angor, T/1000000, -9.81, wind)
            projectile.goto(PX_1 + X*10, PY_1 + Y*10)
            projectile.setheading(DI)
            t1 = t2
        t2 = datetime.datetime.now()
        D = t2 - t1
        if PY_1 + Y*10 < -600 or PX_1 + X*10 > 1000 or PX_1 + X*10 == PX_1 and PY_1 + Y*10 == PY_1:
            break

    t1 = datetime.datetime.now()
    t2 = t1 + datetime.timedelta(milliseconds=5)
    D = t2 - t1
    Y = 1
    X = 1
    T = 0

    effaceur.penup()
    effaceur.hideturtle()
    effaceur.goto(PX_1, PY_1)
    effaceur.pendown()
    while True:
        if D.microseconds > deltat:
            T += D.microseconds
            X, Y, _1, _2, DI = trajectoire(0, 0, vitor, angor, T/1000000, -9.81, wind)
            effaceur.goto(PX_1 + X*10, PY_1 + Y*10)
            effaceur.setheading(DI)
            t1 = t2
        t2 = datetime.datetime.now()
        D = t2 - t1
        if PY_1 + Y*10 < -600 or PX_1 + X*10 > 1000:
            break

    joueur_1.showturtle()
    joueur_2.showturtle()


    t1 = datetime.datetime.now()
    t2 = t1 + datetime.timedelta(milliseconds=5)
    D = t2 - t1
    vitor = int(turtle.numinput("vitesse", "quel vitesse voulez vous utiliser j2? "))
    angor = int(turtle.numinput("angle", "quel angle voulez vous utiliser j2? "))
    X = 1
    Y = 1
    T = 0
    projectile.penup()
    projectile.hideturtle()
    projectile.goto(PX_2, PY_2)
    projectile.showturtle()
    projectile.pendown()
    while True:
        if D.microseconds > deltat:
            T += D.microseconds
            X, Y, _1, _2, DI = trajectoire(0, 0, vitor, angor, T/1000000, -9.81, wind)
            projectile.goto(PX_2 - X*10, PY_2 + Y*10)
            projectile.setheading(180 - DI)
            t1 = t2
        t2 = datetime.datetime.now()
        D = t2 - t1
        if PY_2 + Y*10 < -600 or PX_2 - X*10 < -1000 or PX_2 - X*10 == PX_2:
            break

    t1 = datetime.datetime.now()
    t2 = t1 + datetime.timedelta(milliseconds=5)
    D = t2 - t1
    Y = 1
    X = 1
    T = 0

    effaceur.penup()
    effaceur.hideturtle()
    effaceur.goto(PX_2, PY_2)
    effaceur.pendown()
    while True:
        if D.microseconds > deltat:
            T += D.microseconds
            X, Y, _1, _2, DI = trajectoire(0, 0, vitor, angor, T/1000000, -9.81, wind)
            effaceur.goto(PX_2 - X*10, PY_2 + Y*10)
            effaceur.setheading(180 - DI)
            t1 = t2
        t2 = datetime.datetime.now()
        D = t2 - t1
        if PY_2 + Y*10 < -600 or PX_2 - X*10 < -1000:
            break

    joueur_1.showturtle()
    joueur_2.showturtle()


turtle.exitonclick()

import turtle
import random

class Arbre:
    def __init__(self, x, y, taille, tortue):
        self.x = x
        self.y = y
        self.taille = taille
        self.t = tortue
        self.t.penup()

    def tron(self):
        epaiseur = 5
        hauteur = 35
        self.t.goto(self.x, self.y)
        self.t.pendown()
        for i in range(2):
            self.t.forward(epaiseur*self.taille)
            self.t.left(90)
            self.t.forward(hauteur*self.taille)
            self.t.left(90)

for i in range(5):
    x1 = random.randint(-300, 300)
    y1 = random.randint(-150, 10)
    t1 = random.randint(1, 5)
    Arbre(x1, y1, t1, turtle.Turtle)

if __name__ == "__main__":
    pass
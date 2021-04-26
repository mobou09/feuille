def pluralize(total, singular, plural=None):
    assert isinstance(total, int) and total >= 0

    if not plural:
        plural = singular + "s"

    string = singular if total <= 1 else plural

    return f'{total} {string}'

print(pluralize(1, "évènement", "évènements"))


class Produit:
    def __init__(self, nom="p", prix=0):
        self.__nom = nom
        self.__prix = prix
        self.__ing = []

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, name):
        self.__nom = name

    @property
    def prix(self):
        return self.__nom

    @prix.setter
    def prix(self, p):
        self.__nom = p

    def dollar(self):
        return self.__prix * 1.2

    def __str__(self):
        chaine = "nom".center(20) + "||" + "prix €".center(10) + "||" + "prix $".center(10) + "\n"
        chaine_2 = "-" * 44 + "\n"
        chaine_3 = f"{self.__nom.center(20)}||{str(self.__prix).center(10)}||{str(self.dollar()).center(10)}"
        return chaine + chaine_2 + chaine_3

    def __add__(self, other):
        n = self.nom.split(" ")[0]+"//"+other.nom.split(" ")[0]
        return Produit(nom=n, prix=self.__prix+other.__prix)

    def ingredients(self, ing):
        self.__ing.append(ing)
        self.__ing = sorted(self.__ing, reverse=False)

    def __getitem__(self, item):
       return self.__ing[item]

    @property
    def calorie(self):
        resultat = 0
        for ingredients in self.__ing:
            resultat += ingredients[2]
        return resultat


salade = Produit(nom="salade césar", prix=1.7)
sandwich = Produit(nom="sandwich de poulet", prix=2)
salade.nom = "salade de légumes"
print(salade+sandwich+salade)
print(dir(salade))
salade.ingredients(("tomates", 50, 27))
salade.ingredients(("carotes", 100, 30))
salade.ingredients(("chicon", 300, 40))
print(salade[0])
print(salade.calorie)

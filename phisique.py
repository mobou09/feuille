def equdeux(a, b, c):
    delta = b**2-4*a*c
    if delta >= 0:
        return [(-b+pow(delta, 0.5))/(2*a), (-b-pow(delta, 0.5))/(2*a)]
    else:
        return "il n'y a pas de solution (réel)"


def MRURA1(x0, v0, a):
    reponse = input("x/v(t) ou t(x) ? x/t ")
    if reponse == "x":
        t = float(input("temps ? "))
        return [x0 + v0*t + 1/2*a*t**2, v0 + a*t]
    else:
        x = float(input("x ? "))
        return equdeux(a/2, v0, x0-x)

print(MRURA1(309, 0, -9.81))



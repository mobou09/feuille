import random

def jules(chaine, n, code):
    resultat = ""
    n = n % len(code)
    # création du dictionaire code
    for lettre in chaine:
        if lettre in code:
            idx = code.index(lettre)
            if idx + n > len(code) - 1:
                resultat += code[idx + n - len(code)]
            else:
                resultat += code[idx + n]
        else:
            resultat += lettre
    return resultat


abc = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789"

nc = random.sample(abc, k=len(abc))

print(nc)

message = jules(chaine="MATIAS", n=17, code=nc)

print(message)

messageoriginel = jules(chaine=message, n=-17, code=nc)

print(messageoriginel)
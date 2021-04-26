def s(*args, **kwargs):
    if kwargs.get("som",True):
        print(kwargs)
        print(type(kwargs))
        resultat = 0
        print(args)
        print(type(args))
        for a in args:
            resultat += a
    else:
        resultat = 1
        for a in args:
            resultat *= a
    return resultat

def nombre(*args):
    c = len(args)
    a = type(args[0])
    for ar in args:
        if a != type(ar):
            return c, False
    return c, True

def aire(base, h):
    calcule = base*h/2
    return calcule

print(aire(4, 8))


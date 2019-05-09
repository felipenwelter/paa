def potencia(b,e):
    r = 0
    if (e < 1):
        return 1
    r = potencia(b,e/2)
    if (e % 2 == 0):
        return r*r
    else:
        return r*r*b


result = potencia(4,3)
print("%d" % result)

def soma(valor1, valor2=10):
    return valor1 + valor2

print(soma(valor1=1))

print soma(1,2)

d = {'valor1':3, 'valor2':1}

print soma(**d)


def calc(v1, v2, func):
    return func(v1, v2)

def mul(a,b):
    return a*b

opt = 'mul'

if opt == 'mul':
    print calc(10,7,mul)
elif opt == 'soma':
    print calc(10,2,soma)
# Implementação Fibonacci Recursivo
# 0 1 1 2 3 5 8 13 21 ...
# 0 1 2 3 4 5 6  7  8

def fibo(n):
    if (n <= 2):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

for x in range(1,10):
    print("%d: %d" % (x,fibo(x)) )

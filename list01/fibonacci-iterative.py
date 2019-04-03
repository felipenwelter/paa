# Implementação Fibonacci Iterativo
# 0 1 1 2 3 5 8 13 21 ...
# 0 1 2 3 4 5 6  7  8

def fibo(n):
    
    n1 = 0
    n2 = 1
    res = 0

    if (n < 2):
        return 1
    else:

        for x in range(1,n):
            res = n2 + n1
            n1 = n2
            n2 = res

    return res


for x in range(1,10):
    print("%d: %d" % (x,fibo(x)) )
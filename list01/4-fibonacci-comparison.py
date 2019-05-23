import time
import matplotlib.pyplot as plt

#quantidade de elementos a serem calculados
calc_limit = 200

# Implementação Fibonacci Iterativo
# 0 1 1 2 3 5 8 13 21 ...
# 0 1 2 3 4 5 6  7  8
def fibo_i(n):
    
    n1 = 0
    n2 = 1
    res = 0

    if (n < 2):
        return 1
    else:

        for x in range(1,n): # complexidade de tempo: O(n) * O(1)
            res = n2 + n1
            n1 = n2
            n2 = res

    return res


# Implementação Fibonacci Recursivo
# 0 1 1 2 3 5 8 13 21 ...
# 0 1 2 3 4 5 6  7  8
def fibo_r(n):
    if (n <= 2):
        return 1
    else:
        return fibo_r(n-1) + fibo_i(n-2)  # complexidade T(n) = T(n-1) + T(n-2) -> exponencial O(2^n)



# Impressão do resultado 
list_r = [] #armazena tupla com os dados (n element, result, time spent)
plot_ry = [] #tupla para impressao do tempo
for x in range(1,calc_limit):
    ini = time.time()
    res = fibo_r(x)
    fim = time.time()
    list_r.append( (x,res,fim-ini) )
    plot_ry.append( fim-ini )

list_i = [] #armazena tupla com os dados (n element, result, time spent)
plot_iy = [] #tupla para impressao do tempo
for x in range(1,calc_limit):
    ini = time.time()
    res = fibo_i(x)
    fim = time.time()
    list_i.append( (x,res,fim-ini) )
    plot_iy.append( fim-ini )

print('\nFibonacci Recursivo')
for x in list_r:
    print("%d: %d em %.9f" % (x[0], x[1], x[2]) )

print('\nFibonacci Iterativo')
for x in list_i:
    print("%d: %d em %.9f" % (x[0], x[1], x[2]) )

plt.plot(range(1,calc_limit),plot_ry)
plt.plot(range(1,calc_limit),plot_iy)
plt.xlabel('n element')
plt.ylabel('time spent (ms)')
plt.title('Tempo de execução Fibonacci Iterativo x Recursivo')
plt.show()
# LINK : https://judge.beecrowd.com/pt/problems/view/1158

n = int(input())

for i in range(1, n+1):
    somador = 0
    c = list(map(int, input().split()))

    if c[0]%2 == 0: # é par
        valor_inicial = c[0] + 1
    else: # é ímpar
        valor_inicial = c[0]

    for j in range(1, c[1]+1):
        somador += valor_inicial
        valor_inicial += 2
        
    print(somador)

# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
# LINK : https://judge.beecrowd.com/pt/problems/view/1010

item1 = list(map( float, input().split())) # qtd = item1[1], valor = item1[2]
item2 = list(map( float, input().split())) # qtd = item2[1], valor = item2[2]



print(f'VALOR A PAGAR: R$ {(item1[1] * item1[2] + item2[1] * item2[2]) :.2f}')

# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
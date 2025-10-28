# LINK : https://judge.beecrowd.com/pt/problems/view/1103

from datetime import datetime, timedelta

def all_zeros(list):
    return all(value == 0 for value in list)

while True:
    inp = list(map(int, input().split()))
    h1 = inp[0]
    m1 = inp[1]
    h2 = inp[2]
    m2 = inp[3]
    print(all_zeros(inp))

    h2 - h1


    if all_zeros(inp) == True:
        break
    
    







# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
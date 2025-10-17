# LINK : https://judge.beecrowd.com/pt/problems/view/1144

n = int(input())
i = 1
for i in range(i, n+1):
    for i2 in range(0, 2):
        if i2%2 == 0:
            print(f"{i} {i**2} {i**3}")
        else:
            print(f"{i} {(i**2)+1} {(i**3)+1}")

# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
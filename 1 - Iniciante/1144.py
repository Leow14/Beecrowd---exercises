# LINK : https://judge.beecrowd.com/pt/problems/view/1144

n = int(input()) * 2
i = 1
c2 = 0
c3 = 1

while i <= n:
    
    if c3%2 != 0:
        print(f"{i} {i**2} {i**3}")
    else:
        print(f"{i} {(i**2)+1} {(i**3)+1}")
    c2 += 1
    c3 += 1
    if c2 > 1:
        i += 1
        c2 = 0
    if c3 > n:
        i = c3+1

# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
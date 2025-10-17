# LINK : https://judge.beecrowd.com/pt/problems/view/1087

while True:
    e = list(map(int, input().split()))
    x = e[0]
    y = e[1]

    if e[0] == 0 or e[1] == 0 or e[2] == 0 or e[3] == 0:
        break
    if (e[0] == e[2] and e[1] == e[3]):
        print(0)
    elif (e[0] == e[2] or e[1] == e[3]) or abs(e[0] - e[2]) == abs(e[1] - e[3]):
        print(1)
    else:
        print(2)

# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
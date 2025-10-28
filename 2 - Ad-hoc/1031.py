# LINK : https://judge.beecrowd.com/pt/problems/view/1031

while True:
    n = int(input())

    if n == 0:
        break
    y = 1
    idx = 0
    array = [x for x in range(2, n+1)]

    while True:
        idx = (idx + y - 1) % len(array)
        array.pop(idx)
        #print(f"y={y}, idx={idx}, array={array}")
        if 13 not in array:
            array = [x for x in range(2, n+1)]
            y += 1
            idx = 0
        if len(array) == 1 and 13 in array:
            break
        

    print(y)

    # Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
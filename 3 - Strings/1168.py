# LINK : https://judge.beecrowd.com/pt/problems/view/1168


cases = int(input())
    
for i in range(cases):
    solution = 0
    conversion = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    n = str(input())

    for number in n:
        solution += conversion[int(number)]
    
    print(f"{solution} leds")


# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
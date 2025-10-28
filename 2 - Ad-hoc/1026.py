# LINK : https://judge.beecrowd.com/pt/problems/view/1026

while True:
    try:
        numbers_list = list(map(int, input().split()))
    except EOFError:
        break
        
    print(numbers_list[0] ^ numbers_list[1])

#print(carry, summatory, a, b)
# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
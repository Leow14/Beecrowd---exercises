# LINK : https://judge.beecrowd.com/pt/problems/view/1026

while True:
    try:
        numbers_list = list(map(int, input().split()))
    except EOFError:
        break

    a = (bin(numbers_list[0])[2:])
    b = (bin(numbers_list[1])[2:])
    bin_sum = 0
    solution = ''

    if len(a) < len(b):
        a = a.zfill(len(b))
    if len(b) < len(a):
        b = b.zfill(len(a))

    for i in range(len(a)):
        solution += str(int(a[i]) ^ int(b[i]))
        
    print(int(solution, 2))
#sum_numbers =
#print(carry, summatory, a, b)
# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
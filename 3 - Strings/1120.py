# LINK : https://judge.beecrowd.com/pt/problems/view/1120

while True:
    try:
        n = list(map(str, input().split()))
    #print(n)
    except EOFError:
        break
    
    contract = [number for number in n[1]]

    if n[0] == '0' and n[1] == '0':
        break

    solution = ''.join([number for number in contract if number != n[0]])
    
    if solution == '':
        solution = 0 
    print(int(solution))

# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
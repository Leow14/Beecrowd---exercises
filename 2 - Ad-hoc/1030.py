# LINK : https://judge.beecrowd.com/pt/problems/view/1030

num_testes = int(input())
i = 0


while i < num_testes:
    nk = list(map(int, input().split()))
    homens = [x for x in range(1, nk[0]+1)]
    idx = 0

    while len(homens) > 1:
        idx = (idx + nk[1] - 1) % len(homens)    
        homens.pop(idx)


    print(f"Case {i + 1}: {homens[0]}")
    i += 1

# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
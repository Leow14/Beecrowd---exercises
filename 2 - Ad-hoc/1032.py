# % é o que faz tudo ficar circular

def criar_lista_primos(n):
    lista = []
    count = 0

    for i in range(n):
        for j in range(2, i//2):
            if i % j == 0: # n eh primo
                return 'numero n eh primo'
        lista.append(i)



while True:
    n = int(input())
    if n == 0:
        break

    n_list = [x for x in range(1, n+1)]
    print(n_list)



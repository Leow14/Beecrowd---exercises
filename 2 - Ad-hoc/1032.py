# % é o que faz tudo ficar circular
def ePrimo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(2, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def criar_lista_primos(size):
    lista = []
    count = 0
    number = 2
    # com excessao do 3, n primos são sempre impares
    # o único fator de n que é maior que n/2 é o próprio n
    
    while count < size:
        if ePrimo(number) == 1:
            lista.append(number)
            count += 1
        number += 1
    
    return lista

while True:
    n = int(input())
    if n == 0:
        break

    n_list = [x for x in range(1, n+1)]
    prime_list = criar_lista_primos(n)
    #print(n_list, prime_list)
    prime_index = 0
    idx = 0

    while len(n_list) > 1:
        idx = (idx + prime_list[prime_index] - 1) % len(n_list)
        n_list.pop(idx)
        prime_index += 1
    
    print(n_list[0])
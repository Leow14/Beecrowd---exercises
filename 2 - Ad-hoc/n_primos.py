# % é o que faz tudo ficar circular
def ePrimo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(2, n//2):
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
        

_list = criar_lista_primos(20)

print(_list)

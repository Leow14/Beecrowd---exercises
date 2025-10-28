def gerar_primos(n):
    if n <= 0:
        return []

    import math
    limite = max(15, int(n * (math.log(n) + math.log(math.log(n))) + 100)) if n >= 6 else 15

    crivo = [True] * (limite + 1)
    crivo[0] = crivo[1] = False

    for i in range(2, int(math.sqrt(limite)) + 1):
        if crivo[i]:
            for j in range(i * i, limite + 1, i):
                crivo[j] = False

    return [num for num in range(2, limite + 1) if crivo[num]][:n]


# Exemplo de uso
n = 5
lista = gerar_primos(n)
print(lista)  # [2, 3, 5, 7, 11]
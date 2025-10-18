# beecrowd 1237 - Substring
# Lê pares de linhas até EOF e imprime o tamanho da maior substring comum

out = []
while True:
    try:
        text1 = input()
        text2 = input()
    except EOFError:
        break

    # garante que s é a menor string
    if len(text1) <= len(text2):
        shorter, larger = text1, text2
    else:
        shorter, larger = text2, text1

    shorterLenght = len(shorter)
    largerLenght = len(larger)
    ans = 0

    # tenta do maior comprimento possível para o menor
    c = shorterLenght
    found = False
    while c > 0 and not found:
        # gera todas as janelas de tamanho L de s
        subs = set()
        limit_s = shorterLenght - c + 1
        for i in range(limit_s):
            subs.add(shorter[i:i+c])

        # verifica janelas de tamanho L em t
        limit_t = largerLenght - c + 1
        for j in range(limit_t):
            if larger[j:j+c] in subs:
                ans = c
                found = True
                break

        c -= 1

    out.append(str(ans))

print("\n".join(out))
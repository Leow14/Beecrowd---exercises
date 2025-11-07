
while True:
    try:
        inp = list(map(int, input().split()))
    except EOFError:
        break

    max_linhas = inp[1]  # Máximo de linhas por página
    max_char = inp[2] # Máximo de caractéres por linha

    contador_linhas = 0
    contador_char = 0
    contador_pag = 0

    text = input().split()
    print(text)
    
    for char in text:
        ##if char == ' ' or (idx == len(text)):
        ##    contador_ += 1

        if contador_char + len(char) + 1 < max_char:
            contador_char += len(char) + 1
        else:
            contador_char = len(char) + 1
            contador_linhas += 1

        if contador_linhas == max_linhas:
            contador_linhas = 0
            contador_pag += 1

    
    
    print(contador_pag)

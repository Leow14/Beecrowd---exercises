# LINK : https://judge.beecrowd.com/pt/problems/view/1234

while True:
    try:
        text = list(input().lower())
    except EOFError:
        break
    
    solution = []
    maiuscula = True
    for letter in text:
        if letter.isalpha():
            if maiuscula == True:
                solution.append(letter.upper())
                maiuscula = False
            else:
                solution.append(letter)
                maiuscula = True
        else:
            solution.append(letter)

    solution = ''.join(solution)
    print(f'{str(solution)}')
    

# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
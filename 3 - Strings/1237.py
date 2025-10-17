
# LINK : https://judge.beecrowd.com/pt/problems/view/1237

while True:
    try:
        text1 = input()
        text2 = input()
    except EOFError:
        break

    
    shorter = ''
    lenght = 0
    solution = ''
    if len(text1) > len(text2):
        shorter, longer = text2, text1
    elif len(text2) >= len(text1):    
        shorter, longer = text1, text2

    for i in range(len(shorter)):
        for j in range(len(shorter)+1):
            comp = shorter[i:j]

            if (comp in longer) and (lenght <= len(comp)):
                print(comp)
                solution = comp
                lenght = len(comp)
    
    print(f'{len(solution)}')

    

# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
# LINK : https://judge.beecrowd.com/pt/problems/view/1069

count = int(input())

for i in range(count):
    extraction =  list(input())
    
    diamonds = 0
    #print(extraction)
    clean_extraction = [item for item in extraction if item != '.']

    #print(clean_extraction)
    while True:
        found = False
        for index in range(len(clean_extraction) - 1):
            if clean_extraction[index] == '<' and clean_extraction[index + 1] == '>':
                diamonds += 1
                del clean_extraction[index:index+2]
                found = True
                break
            
        if not found:
            #if ('>' and '<' in clean_extraction) and ()
            break

    #print(clean_extraction)
    print(diamonds)


# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14 
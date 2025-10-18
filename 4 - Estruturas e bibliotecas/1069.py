# LINK : https://judge.beecrowd.com/pt/problems/view/1069

count = int(input())

for i in range(count):
    extraction =  list(input())
    diamonds = 0
    #print(extraction)
    clean_extraction = [item for item in extraction if item != '.']

    print(clean_extraction)
    
    for index, item in enumerate(clean_extraction):
        #print(f'item: {item} || item: {clean_extraction[index]} index: {index} || item_prox: {clean_extraction[index + 1] } || index {index + 1}')
        if clean_extraction[index] == '<' and clean_extraction[index + 1] == '>':
            #print(f'item: {item} || item: {clean_extraction[index]} index: {index} || item_prox: {clean_extraction[index + 1] } || index {index + 1}')
            diamonds += 1
            print(index, index+1)
            del clean_extraction[index:index+2]

    print(clean_extraction)
    print(diamonds)


# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
while True:
    n = int(input())
    if n == 0:  
        break
    v = list(input())
    for spc in v:
        texto = ''.join(v)

    if "..." in texto:
        print("S")
    else:
        print("N")

print(texto)

#3... .X. XX. XXX-> sempre cai em vitória
#4.... .X.. .XX. XXX -> sempre cai em vitória
#5..... ..X.. -> sempre cai em vitória
#6...... ..X... ..X..X -> não é sempre
#7....... ...X... X..X... X..X..X -> sempre cai em vitória
#8........ ....X... ....X..X X...X..X -> não é sempre
#9......... ....X.... X...X.... X...X...X ->sempre cai em vitória
#10.......... .....X.... ..X..X.... ..X..X..X. -> não é sempre
#11...........
#12............



#6 ..X... ..X..X -> sempre em derrota
#6
#6
#6

# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
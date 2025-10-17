# LINK : https://judge.beecrowd.com/pt/problems/view/1141

while True:
    n = int(input())
    if n == 0:
        break
    contador = 0
    string_photos = []

    for i in range(n):
        string = input()
        string_photos.append(string)
        contador += 1

    string_photos.sort(key=len)

    for string, index in enumerate(string_photos):
        print(string_photos)
    
    print(string_photos)

# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
# LINK : https://judge.beecrowd.com/pt/problems/view/2152

q = int(input())

for i in range(1, q+1):
    porta = list(input().split())
    if porta[2] == "1":
        c = "abriu!" 
    elif porta[2] == "0":
        c = "fechou!"

    print(f"{porta[0].zfill(2)}:{porta[1].zfill(2)} - A porta {c}")

# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
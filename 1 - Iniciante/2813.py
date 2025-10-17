# LINK : https://judge.beecrowd.com/pt/problems/view/2813

q = int(input())
casa = 0
gc_casa = 0
escritorio = 0
gc_escritorio = 0

#tempo[0] = casa
#tempo[1] = escritório

for i in range(1 , q+1):
    tempo = list(input().split())
    if tempo[0] == "chuva" and gc_casa == 0: #está chovendo em casa e não temos o guarda_chuva
        casa += 1
        gc_escritorio += 1

    if tempo[0] == "chuva" and gc_casa > 0: #está chovendo em casa e temos o guarda_chuva
        gc_escritorio += 1
        gc_casa -= 1

    if tempo[1] == "chuva" and gc_escritorio == 0: #está chovendo no escritório e não temos o guarda_chuva
        escritorio += 1
        gc_casa += 1

    if tempo[1] == "chuva" and gc_escritorio > 0: #está chovendo no escritório e temos o guarda_chuva
        gc_casa += 1
        gc_escritorio -= 1

print(f"{casa} {escritorio}")

# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
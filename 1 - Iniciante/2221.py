# LINK : https://judge.beecrowd.com/pt/problems/view/2221

t = int(input()) #instâncias

for i in range(1, t+1):
    b = int(input()) #bônus
    guarte = list(map(int, input().split())) # guarte[0] -> ataque || guarte[1] -> defesa || guarte[2] -> level
    dabriel = list(map(int, input().split()))# dabriel[0] -> ataque || dabriel[1] -> defesa ||dabriel[2] -> level

    valor_golpe_guarte = ((guarte[0] + guarte[1])/2)
    if guarte[2] % 2 == 0: valor_golpe_guarte += b 

    valor_golpe_dabriel = ((dabriel[0] + dabriel[1])/2)
    if dabriel[2] % 2 == 0: valor_golpe_dabriel += b 

    if valor_golpe_guarte > valor_golpe_dabriel:
        print("Dabriel")
    elif valor_golpe_guarte < valor_golpe_dabriel:
        print("Guarte")
    else:
        print(f"Valor guarte: {valor_golpe_guarte} Valor dabriel: {valor_golpe_dabriel}")
        print("Empate")

# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
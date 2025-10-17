# LINK : https://judge.beecrowd.com/pt/problems/view/1013

numbers = list(map(int, input().split()))

a = numbers[0]
b = numbers[1]
c = numbers[2]

maiorAB = ((a + b + abs(a - b))/2)
maior = ((maiorAB + c + abs(maiorAB - c))/2)

print(f'{int(maior):.0f} eh o maior')

print()
# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
# LINK : https://judge.beecrowd.com/pt/problems/view/1062

count = int(input())
numbers_list = []
solution = []

for i in range(count):
    number = int(input())
    numbers_list.append(number)

numbers_list.sort()
even = [number for number in numbers_list if number % 2 == 0]
odd = [number for number in numbers_list if number % 2 != 0]

odd = sorted(odd, reverse=True)

solution = even + odd


for number in solution:
    print(f'{number}')


# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
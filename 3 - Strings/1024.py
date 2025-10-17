qtd = int(input())

for i in range(qtd):
    text = input()
    solution = []
    for letter in text[::-1]:
        if letter.isalpha():
            solution.append(chr(ord(letter) + 3))
        else:
            solution.append(letter)
    
    half = len(solution) // 2
    for index, letter in enumerate(solution[half::]):
        solution[index + half] = chr(ord(letter) - 1)

    str_solution = "".join(solution)
    print(str_solution)
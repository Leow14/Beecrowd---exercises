# LINK : https://judge.beecrowd.com/pt/problems/view/1122

while True:
    try:
        inp = list(map(int, input().split()))
    except EOFError:
        break

    sum_words_text = inp[0]
    max_lines = inp[1]
    max_char = inp[2]

    sum_char = 0
    sum_lines = 0
    sum_pages = 0

    text = input().split()

    for words in text:
        for letters in words:
            if sum_char >= max_char:
                sum_lines += 1
                sum_char = 0
            if sum_lines >= max_lines:
                sum_lines = 0
                sum_pages += 1
            sum_char += 1

            #if letters == len(letters) - 1:
                


    print(sum_char, sum_lines, sum_pages)


# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
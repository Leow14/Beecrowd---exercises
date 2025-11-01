while True:
    try:
        s = input()
    except EOFError:
        break

    b = 0
    for char in s:
        if char == '(':
            b += 1
        elif char == ')' and b >= 1:
            
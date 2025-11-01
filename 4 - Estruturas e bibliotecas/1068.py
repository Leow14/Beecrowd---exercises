while True:
    try:
        s = input()
    except EOFError:
        break

    count = 0

    for char in s:
        if char == '(':
            count += 1

        if char == ')' and count >= 1:
            count -= 1
        elif char == ')' and count <=1:
            count -= 1
            break
    
    if count == 0:
        print("correct")
    else:
        print("incorrect")
            
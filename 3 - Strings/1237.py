while True:  
    try:  
        text1 = input()  
        text2 = input()  
    except EOFError:  
        break  
  

    if len(text1) <= len(text2):  
        shorter, larger = text1, text2  
    else:  
        shorter, larger = text2, text1  
  
    shorterLenght = len(shorter)  
    largerLenght = len(larger)  
  
    ans = 0  

    c = shorterLenght  
    found = False  
    while c > 0 and not found:  

        subs = set()  
        limit_s = shorterLenght - c + 1  
        for i in range(limit_s):  
            subs.add(shorter[i:i+c])  
  

        limit_t = largerLenght - c + 1  
        for j in range(limit_t):  
            if larger[j:j+c] in subs:  
                ans = c  
                found = True  
                break  
  
        c -= 1  
  
    print(ans)
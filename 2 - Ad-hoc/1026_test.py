val = str(input("a"))

def swap(a):
    if a == '0':
        a = '1'
    elif a == '1':
        a = '0'
    else:
        raise ValueError("O valor deve ser em formato de string")
    return(a)


swap(val)

print(swap(val))
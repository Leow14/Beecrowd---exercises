# LINK : https://judge.beecrowd.com/pt/problems/view/1026

# 🅱️🅱️🅱️ NÃO FINALIZADO 🅱️🅱️🅱️

#while True:
#    try:
numbers_list = list(map(int, input().split()))
#    except EOFError:
#        break

a = (bin(numbers_list[0])[2:])
b = (bin(numbers_list[1])[2:])
bin_sum = 0
solution = ''

def swap(a):
    if a == '0':
        a = '1'
    elif a == '1':
        a = '0'
    else:
        raise ValueError("O valor deve ser em formato de string")
    return(a)

#                         ^
#Transformar para binário |

if len(a) < len(b):
    a = a.zfill(len(b))
if len(b) < len(a):
    b = b.zfill(len(a))



for i in range(len(a)):
    carry = (a[i] and b[i])
    bin_summatory = ((a[i] and swap(b[i])) or (swap(a[i]) and b[i]))
    solution += bin_summatory
    print(carry, bin_summatory, a[i], b[i])


print(solution)
#sum_numbers =
#print(carry, summatory, a, b)
# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
# LINK : https://judge.beecrowd.com/pt/problems/view/1022

from fractions import Fraction as frc

control = int(input())

for i in range(control):
    ope = input().split()
    
    n1 = int(ope[0])
    d1 = int(ope[2])
    n2 = int(ope[4])
    d2 = int(ope[6])

    # checando para ver o operador matemático
    if ope[3] == '+':
       numerador = (n1*d2 + n2*d1)
       denominador = (d1*d2)
       n = numerador / denominador
    elif ope[3] == '-':
        numerador = (n1*d2 - n2*d1)
        denominador = (d1*d2)
        n = numerador / denominador
    elif ope[3] == '*':
        numerador = (n1*n2)
        denominador = (d1*d2)
        n = numerador / denominador
    elif ope[3] == '/':
        numerador = (n1*d2)
        denominador = (n2*d1)
        n = numerador / denominador
    
    n2 = frc(n).limit_denominator()
    if n2 == int(n2):
        print(f'{numerador}/{denominador} = {frc(n).limit_denominator()}/1')
    else:
        print(f'{numerador}/{denominador} = {frc(n).limit_denominator()}')




# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
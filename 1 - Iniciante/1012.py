# LINK : https://judge.beecrowd.com/pt/problems/view/1012

n = list(map(float, input().split()))





print(f'TRIANGULO: {((n[0] * n[2])/2):.3f}\nCIRCULO: {3.14159 * n[2]**2:.3f}\nTRAPEZIO: {((n[0] + n[1]) * n[2])/2:.3f}\nQUADRADO: {n[1]**2:.3f}\nRETANGULO: {n[0] * n[1]:.3f}')

# Autor: Leonardo Amorim de Araujo || Github: https://github.com/Leow14
import os
os.system ('cls')
print ('soma de ímpares multiplos de 3 de [1 a 500]')
soma = 0
cont = 0
for c in range (1,501):
    if c % 2 ==1 and c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print (f'A soma dos {cont} valores solicitados é: {soma}')
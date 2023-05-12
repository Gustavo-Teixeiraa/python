import os
os.system('cls')

print('='*30)
print('BANCO DEV'.center(30))
print('='*30)

valor = int(input('Qual valor dejesa sacar?: '))
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        totalced +=1
        total -= ced
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de {ced} ')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
            totalced = 0 
        if total == 0:
            break
print('='*30)
print('Volte sempre!'.center(30))
print('='*30)


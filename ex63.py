import os
os.system('cls')
print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)
num= int(input('Quantos termos deseja mostrar: '))
cont = 3
t1 = 0
t2 = 1 
print('-'*30)
print(end=' ' f'{t1} {t2}')
while cont <=num:
    t3 = t1 + t2
    print(end=' ' f'{t3}')
    t1 = t2
    t2 = t3
    cont +=1
print('\nFim\n')
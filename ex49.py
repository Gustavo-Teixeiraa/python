import os
os.system ('cls')

num = int(input('Digite um número para ver sua tabuada: '))

for c in range (1,11):
    print(f'{num} x {c} =  {num*c}')
print('Fim')
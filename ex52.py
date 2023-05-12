import os
os.system('cls')

num = int(input('Digite um número inteiro: '))

div = 0

for c in range(1,num+1):
    if num % c ==0:
        div +=1

if div ==2:
    print(f'{num} É primo')
else:
    print(f'{num} Não é primo')
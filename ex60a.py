import os, math
os.system ('cls')

num = int(input('Digite um número para ver seu fatorial: '))
cont = num
f = math.factorial(num)

while cont > 0:
    print(cont,end=' * ')
    print(' * ' if cont > 1 else '= ',end='')
    cont -=1
print(f)
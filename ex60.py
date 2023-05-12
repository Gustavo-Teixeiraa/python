import os,math
os.system('cls')

num = int(input('Digite um número para ver seu fatorial: '))
f = math.factorial(num)

for c in range(num,0,-1):
    print(f'{num} * {c}')

print(f'Resultado...\n{f}')


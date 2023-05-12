import os
os.system('cls')

soma = 0
for c in range(1,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num
    else:
        print ('Não é um número par')
print(f'A soma do números pares é: {soma}')
print ('fim')

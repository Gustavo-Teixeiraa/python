import os
os.system ('cls')

print('-'*30)
print('SOMA DOS NÚMEROS')
print('-'*30)
soma = 0

while True:
    num = int(input('Digite um Número [ou 999 para sair]: '))
    if num == 999:
        break
    else:
        soma = soma + num

print(f'A soma dos números é: {soma}')
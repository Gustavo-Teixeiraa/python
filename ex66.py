import os
os.system ('cls')
soma = 0
digitados = 0
while True:
    num = int(input('Digite um número [ou 999 para sair]: '))
    if num == 999:
        break
    else:
        soma += num
        digitados +=1

print(f'A soma dos {digitados} valores digitados é {soma}')
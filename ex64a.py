import os
os.system ('cls')
num = 0
digitados = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [ou 999 para sair]: '))
    if num == 999:
        break
    else:
        digitados +=1
        soma = soma + num
        cont += 1
print(f'A quantidade de números digitaos é: {digitados}\nE a soma é: {soma}')
import os
os.system('cls')

numeros = []
cont = 0
while True:
    num = float(input('Digite um número para ser armazenado (ou 0 para sair): '))
    if num == 0:
        break
    numeros.append(num)
    soma = sum(numeros)
    media = soma / len(numeros)
for num in numeros:
    if num > 6:
        cont+=1

print('='*30)
print(f'A soma dos valores é: {soma}\nA média dos valores é: {media}\nE a quantidade de números acima da média (6) é: {cont}')
print('='*30)
import os
os.system ('cls')

resposta = 's'
cont = 0
digitados = 0
media = 0
maior = 0
menor = 0
soma = 0

while resposta in 'sS':
    num = int(input('Digite um número: '))
    soma += num
    digitados +=1
    cont +=1
    if num > maior:
        maior = num
    else:
        menor = num
    resposta = input('Deseja continuar?: ')
media = soma / digitados
if resposta in 'nN':
        print(f'Você digitou {digitados} números e a média deles foi {media}\nO maior valor foi {maior} e o menor foi {menor}')


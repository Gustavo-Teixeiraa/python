import os
os.system('cls')

valores = []
par = []
impar = []

while True:
    num = int(input('Digite um número(ou 0 para sair): '))
    if num == 0:
        break
    valores.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'Os valores foram: {valores}\nNúmeros Ímpares: {impar}\nNúmeros Pares: {par}')
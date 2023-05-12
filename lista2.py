import os
os.system('cls')

placa = []
multa = []
cont = 0
for c in range(15):
    print('='*30)
    placa2 = input(f'Digite a placa do {c+1}° carro: ')
    placa.append(placa2)
    multa2 = float(input(f'Digite o valor da multa do {c+1}° carro: '))
    print('='*30)
    multa.append(multa2)
    if multa2 >= 300:
        cont+=1

media = sum(multa) / 15

print(f'A média das multas é: {media:.2f}\nQuantidade de carros com multa maior ou igual a R$300: {cont}')
import os
os.system('cls')

maior = 0
menor = float('inf')

for c in range (1,6):
    peso = float(input('Digite o seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'O maior peso foi: {maior:.2f}KG\nE o menor peso foi {menor:.2f}')
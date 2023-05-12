import os
os.system ('cls')

km = float (input('Quantos km rodados com o carro?'))
dias = int (input('Por quantos dias andou com ele'))
precodia = dias * 60
kmrodado = km * 0.15
totalpagar = precodia + kmrodado

print (f'o total a pagar é de {totalpagar:.2f}')

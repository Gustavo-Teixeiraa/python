import os
os.system ('cls')
barato = float('inf')
total = 0
maior1000 = 0
nomeb = ''
while True:
    print('='*30)
    print('LOJA SUPER BARATÃO'.center(30))
    print('='*30)

    produto = input('Nome do produto: ')
    preco = float(input('Digite o preço R$: '))
    if preco > 1000:
        maior1000 +=1
    if preco < barato:
        barato = preco
        nomeb = produto
    total += preco

    resposta = input('Dejesa continuar?: ')
    while resposta not in 'sn':
        resposta =input('Dejesa continuar?: ')
    if resposta == 'n':
        break
print('='*30)
print('Fim do Programa'.center(30))
print(f'O total da compra foi {total}\nTemos {maior1000} produto custando mais de R$1000\nO produto mais barato foi {nomeb} e custa: {barato}')
print('='*30)
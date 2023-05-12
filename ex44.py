import os
os.system ('cls')

print ('============= LOJAS GUSTAVO ============= ')
preco = float(input('Qual é o preço do produto: '))
os.system('cls')
condicao = input('Qual a condição de pagamento\n[1] A vista dinheiro ou cheque [10% Desconto]\n[2] A vista no cartão [5% Desconto]\n[3] Até 2x no cartão [Preço normal]\n[4] 3 ou mais vezes no cartão [20% juros]\n\nDigite aqui: ')
os.system('cls')

if condicao == '1':
    desconto = preco * 0.10
    novopreco = preco - desconto
    print (f'O produto que custava {preco} com 10% de desconto fica {novopreco:.2f}')
elif condicao == '2':
    desconto = preco * 0.05
    novopreco = preco - desconto
    print (f'O produto que custava {preco} com 5% de desconto fica {novopreco}')
elif condicao == '3':
    print (f'2x no cartão o preço fica normal custando {preco}')
elif condicao == '4':
    juros = preco * 0.20
    novopreco = preco + juros
    print (f'O produto que custava {preco} com 20% de juros fica {novopreco}')
else:
    print ('Opção inválida')

print ('============= AGRADEÇEMOS A PREFERÊNCIA ============= ')

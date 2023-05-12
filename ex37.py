import os
os.system ('cls')

num = int(input('Digite um número inteiro: '))
os.system ('cls')

resposta = input('Escolha uma das bases para conversão:\n[ 1 ] BINÁRIO\n[ 2 ] OCTAL\n[ 3 ] HEXADECIMAL\n\nDigite aqui:')

if resposta == '1':
    binario = bin(num)
    print (f'O número {num} em Binário representa {binario[2:]}')
elif resposta =='2':
    octal = oct(num)
    print (f'O número {num} em Octal representa {octal[2:]}')
elif resposta == '3':
    hexa = hex(num)
    print (f'O número {num} em Hexadecimal representa {hexa[2:]}')
else:
    print ('Opção Inválida')
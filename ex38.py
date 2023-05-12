import os
os.system ('cls')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    maior = num1
    print (f'O maior número é o {maior}')
elif num2 > num1:
    maior = num2
    print (f'O maior número é o {maior}')
else:
    print ('Os números são iguais')
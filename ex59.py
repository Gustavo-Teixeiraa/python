import os
os.system('cls')

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

resposta =0

while True:
    menu = int(input('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS VALORES\n[5] SAIR\n\nDigite sua opção: '))

    if menu ==1:
        soma = num1 +num2
        print(f'{num1} + {num2} = {soma}')
    elif menu ==2:
        multi = num1 * num2
        print(f'{num1} * {num2} = {multi}')
    elif menu ==3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
            print(f'O maior número é {maior}')
    elif menu ==4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        print(menu)
    elif menu ==5:
        break
    else:
        print('Opção inválida')

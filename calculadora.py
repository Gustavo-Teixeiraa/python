import os , math
os.system ('cls')
while True:
    print('='*30)
    print('CALCULADORA'.center(30))
    print('='*30)

    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))

    escolha = int(input('Digite sua escolha\n\n[1] Adição\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Divisão Inteira\n[6] Raiz Quadrada\n[7] Sair\n\nDigite sua opção: '))

    match(escolha):

        case(1):
            print('Opção 1 selecionada!')
            soma = n1 + n2
            print('--------'*12)
            print(f'{n1} + {n2} = {soma}'.center(12))
            print('--------'*12)
            input('Aperte enter para voltar ao menu...')
            os.system('cls')
        case(2):
            print('Opção 2 selecionada')
            sub = n1 - n2
            print('--------'*12)
            print(f'{n1} - {n2} = {sub}')
            print('--------'*12)
            input('Aperte enter para voltar ao menu')
            os.system('cls')
        case(3):
            print('Opção 3 selecionada')
            multi = n1 * n2
            print('--------'*12)
            print(f'{n1} x {n2} = {multi}')
            print('--------'*12)
            input('Aperte enter para voltar ao menu')
            os.system ('cls')

        case(3):
            print('Opção 4 selecionada')
            div = n1 / n2
            print('--------'*12)
            print(f'{n1} / {n2} = {div}')
            print('--------'*12)
            input('Aperte enter para voltar ao menu')
            os.system ('cls')

        case(5):
            print('Opção 5 selecionada')
            div2 = n1 // n2
            print('--------'*12)
            print(f'{n1} // {n2} = {div2}')
            print('--------'*12)
            input('Aperte enter para voltar ao menu')
            os.system ('cls')
        
        case(6):
            print('Opção 6 selecionada')
            raiz1 = math.sqrt(n1)
            raiz2 = math.sqrt(n2)
            print('--------'*12)
            print(f'Raiz quadrada de {n1} = {raiz1:.2f}\nRaiz quadrada de {n2} = {raiz2:.2f}')
            print('--------'*12)
            input('Aperte enter para voltar ao menu')
            os.system ('cls')

        case(7):
            print('saindo do menu...')
            break
        case _:
            input('Opção inválida!, aperte enter para voltar ao menu')
            os.system('cls')
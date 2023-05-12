import os
os.system ('cls')
from random import randint
print('='*30)
print('PAR OU ÍMPAR, VAMOS JOGAR!')
print('='*30)
vence = 0

while True:
    jogador = int(input('Digite um valor: '))
    tipo = str(input('Par ou ímpar: '))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ''
    while tipo not in 'pPiI':
        tipo = str(input('Par ou ímpar: '))
    print(f'Você jogou {jogador} e a máquina {computador} com total: {total}')
    print(f'Deu par' if  total % 2 == 0 else 'Deu ímpar')
    if tipo in 'pP':
        if total % 2 ==0:
            print('Você venceu')
            vence += 1
        else:
            print('Você perdeu')
            break
    elif tipo in 'iI':
        if total % 2 ==1:
            print('VocÊ venceu')
            vence +=1
        else:
            print('VocÊ perdeu')
            break
print(f'VocÊ venceu {vence} vezes')  

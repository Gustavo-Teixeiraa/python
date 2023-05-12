import os
os.system('cls')
from random import randint

print ('Vou pensar em um número de 0 a 10 tente adivinhar...')
respostamaq = randint(0,10)
cont = 0

eu = int(input('Em que número eu pensei: '))

while eu != respostamaq:
    cont +=1
    if eu < respostamaq:
        print('O número que eu pensei é maior, está quase lá')
        eu = int(input('Em que número eu pensei: '))
    else:
        print('O número que eu pensei é menor, está quase lá')
        eu = int(input('Em que número eu pensei: '))

print(f'Parabéns, eu pensei no número {respostamaq} e Você no {eu} também\nE a quantidade de tentativas foi de: {cont}')

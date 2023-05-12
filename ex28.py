import os , random
os.system('cls')

print ('Vou pensar em um número de 0 a 5 tente adivinhar...')
lista = [0,1,2,3,4,5]
respostamaq = random.choice(lista)

eu = int (input('Em que número eu pensei: '))

if eu == respostamaq:
    print (f'Parabéns eu pensei no {respostamaq} e você no {eu} também ')
else:
    print (f'Você perdeu, eu pensei no {respostamaq} e você no {eu}')
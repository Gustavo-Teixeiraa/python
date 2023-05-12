import os 
os.system('cls')

distancia = float (input('Diigite aqui a distância de uma viagem em km: '))

if distancia <=200:
    cobranca = distancia * 0.50
    print(f'Sua viagem é de {distancia}km e vamos cobrar {cobranca:.2f}')
else:
    cobranca = distancia * 0.45
    print (f'Sua viagem de {distancia} km é mais longa e a cobrança será {cobranca:.2f}')
import os
os.system ('cls')

velocidade = float (input('Digite a velocidade atual do carro: '))

if velocidade > 80:
    multa = (velocidade-80) * 7.00
    print (f'Você foi multado excedeu a velocidade permitida que é 80km e sua multa foi de {multa:.2f}')
else:
    print ('Tenha um bom dia e dirija com segurança!')
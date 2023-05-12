import os
os.system ('cls')

altura = float(input('Digite aqui a sua altura: '))
peso = float(input('Digite aqui a seu peso: '))

imc = peso  / altura**2

if imc < 18.5:
    print ('Você está abaixo do peso')
elif imc <=25:
    print ('Você está no peso ideal')
elif imc <=30:
    print ('Você está em sobrepeso')
elif imc <=40:
    print ('Você está obeso')
else:
    print ('Você é obeso mórbido')
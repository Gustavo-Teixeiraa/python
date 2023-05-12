import os , math
os.system ('cls')

oposto = float (input('Digite o valor do cateto oposto: '))
ad = float (input('Digite o valor do cateto adjacesnte: '))

hipotenusa = math.hypot(oposto,ad)

print (f'A hipotenusa vai medir {hipotenusa:.2f}')
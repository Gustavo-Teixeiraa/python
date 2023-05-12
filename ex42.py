import os
os.system ('cls')

r1 = float(input('Digite o valor do primeiro segmento: '))
r2 = float(input('Digite o valor do segundo segmento: '))
r3 = float(input('Digite o valor do terceiro segmento: '))

if r1 < r2 + r3 and  r2 < r1 + r3 and r3 < r1 + r2:
    print ('Os segmentos acima podem formar um triângulo')
    if r1 == r2 and r3 and r2 == r1 and r3 and r3 == r1 and r2:
        print ('Este triângulo é Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r1 or r2 == r3 or r3 == r1 or r3 ==r2:
        print ('Este triângulo é Isóceles')
    else:
        print ('Este triângulo é Escaleno')
else:
    print('Os segmentos não podem formar um triângulo')
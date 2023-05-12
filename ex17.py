import os , math
os.system ('cls')

angulo = float (input('Digite aqui o valor de um ângulo: '))
angulorad = math.radians(angulo)

seno = math.sin(angulorad)
cos = math.cos(angulorad)
tang = math.tan(angulorad)

print (f'O Seno do ângulo é {seno:.2f}')
print (f'O Cosseno do ângulo é {cos:.2f}')
print (f'A Tangente do ângulo é {tang:.2f}')
import os
os.system ('cls')

sexo = input('Digite seu sexo [Masculino ou Feminino]: ')

while sexo != 'masculino' and sexo != 'feminino':
    print('Digite um sexo válido')
    sexo = input('Digite seu sexo [M ou F]: ')
print(f'O sexo digitado foi: {sexo}')
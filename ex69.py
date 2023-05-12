import os
os.system ('cls')
maiori = 0
m = 0
f = 0
while True:
    print('='*30)
    print('CADASTRE UMA PESSOA')
    print('='*30)

    print('='*30)
    idade = int(input('Digite a sua idade: '))
    sexo = input('Digite seu sexo [m ou f]: ')
    while sexo not in 'mf':
        sexo = input('Digite seu sexo [m ou f]: ').strip().upper()[0]
    if idade >18:
        maiori +=1
    if sexo == 'm':
            m += 1
    if sexo == 'f' and idade <20:
            f +=1
    resposta = str(input('Deseja continuar [s ou n]: '))
    while resposta not in 'sn':  
        resposta = str(input('Deseja continuar [s ou n]: ')).strip().upper()[0]
    if resposta == 'n':
            break
print('='*30)

print(f'total de pessoas com mais de 18 anos: {maiori}\nAo todo temos: {m} homens cadastrados\ne temos: {f} mulher com menos de 20 anos')

print('='*30)
import os
os.system ('cls')

ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = ptermo
cont = 1

while cont <= 10:
    print(termo,end=' - ')
    termo += razao
    cont+=1

escolha = int(input('Quantos termos a mais quer mostrar?'))
while escolha == escolha:
    print(termo,end=' - ')
    termo += razao
    cont+=1
   

import random , os
os.system ('cls')

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista = [a1 ,a2 ,a3 , a4]

         
escolha = random.choice(lista) #choice = aleatório

print (f'O aluno escolhido foi {escolha}')


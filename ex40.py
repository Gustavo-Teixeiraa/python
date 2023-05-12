import os
os.system ('cls')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a Segunda nota: '))
media = (nota1 + nota2) / 2

if media <5:
    print (f'Tirando a nota {nota1} e {nota2} a média do aluno é {media}\nE o aluno está reprovado')
elif media >= 5 or media < 7:
    print (f'tirando a nota {nota1} e {nota2} a média do aluno é {media}\nE o aluno está de recuperação')
else:
    print (f'Tirando a nota {nota1} e {nota2}, a média do aluno é {media}\nO aluno está aprovado')
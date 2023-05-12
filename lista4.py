import os
os.system('cls')

nomealun = []
notaalun = []
cursoalun = []
cont = 0
aprovado = 0
while True:
    print('='*30)
    aluno = input('Digite seu nome: ')
    curso = input('Digite seu curso (ccp ou tads): ')
    notas = float(input('Digite a sua nota: '))
    print('='*30)
    nomealun.append(aluno)
    cursoalun.append(curso)
    notaalun.append(notas)
    resposta = input('Dejesa continuar? (s ou n): ')
    while resposta not in 'sn':
        resposta = input('Dejesa continuar? (s ou n): ')
    if resposta == 'n':
        break     
    for curso in cursoalun:
        if curso == 'tads':
            cont +=1
media = sum(notaalun) / len(nomealun)
for nota in notaalun:
    if nota > 6:
        aprovado +=1
print('='*30)
print(f'A quantidade de alunos de tads é: {cont}\nA média das notas dos alunos é: {media:.2f}\nA quantidade de alunos acima da média: {aprovado}')
print('='*30)
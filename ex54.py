import os
os.system ('cls')
from datetime import date

atual = date.today().year
idade = 0
maioridade = 0
menoridade = 0

for c in range(1,8):
    ano = int(input('Digite o ano de seu nascimento: '))
    idade = atual - ano
    if idade >=18:
        maioridade +=1
    else:
        menoridade +=1

print(f'{maioridade} Pessoas já tem maior idade\n{menoridade} Pessoas ainda não tem maior idade')

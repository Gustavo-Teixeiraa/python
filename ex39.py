import os
os.system ('cls')
from datetime import date


atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print (f'Quem nasceu em {ano} tem {idade} anos em {atual}')

if idade == 18:
    print ('Você tem idade para se alistar imediatamente')
elif idade < 18:
    saldo = idade - 18
    print (f'Ainda faltam {saldo} anos para o alistamento')
else:
    saldo = idade - 18
    print (f'Você deveria ter se alistado a {saldo} anos')
    ano = atual - saldo
    print (f'Seu alistamento foi em {ano}')


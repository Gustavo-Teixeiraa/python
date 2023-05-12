import os
os.system ('cls')
from datetime import date

atual = date.today().year
ano = int(input('Digite o ano de seu nascimento: '))
idade = atual - ano 

if idade <=9:
    print (f'Você tem {idade} anos e é classificado como MIRIM')
elif idade <=14:
    print (f'Você tem {idade} anos e é classificado como INFANTIL')
elif idade <=19:
    print (f'Você tem {idade} anos e é classificado como JUNIOR')
elif idade <=20:
    print (f'Você tem {idade} anos e é classificado como SENIOR')
else:
    print (f'Você  tem {idade} anos e é classificado como MASTER')
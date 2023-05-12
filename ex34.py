import os
os.system ('cls')

sal = float(input('Digite o valor do seu salário: '))

if sal <= 1250:
    aumento = sal + (sal * 0.15)
    print(f'Quem ganhava {sal} passa a ganahr {aumento}')
else:
    aumento = sal  + (sal * 0.10)
    print (f'Quem passava a ganhar {sal} passa a ganhar {aumento}')
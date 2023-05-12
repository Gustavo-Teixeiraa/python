import os
os.system ('cls')

ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for c in range(11):
    termo = ptermo + c * razao
    print(termo)
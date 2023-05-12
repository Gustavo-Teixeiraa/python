import os
os.system ('cls')

while True:
    print('='*30)
    num = int(input('Quer ver a tabuada de qual valor? [digite um num negativo para sair]: '))
    print('='*30)
    if num <0:
        break

    else:
        for c in range(1,11):
            print(f'{num} x {c} = {num*c}')

print('Tabuada encerrada, volte sempre')

import os
os.system('cls')

diasemana = []
volume = []

for c in range(5):
    semana = input(f'Digite o {c+1}° dia da semana: ')
    volume2 = float(input(f'Digite o {c+1}° volume de chuva: '))
    diasemana.append(semana)
    volume.append(volume2)
    if semana in 'quartaQuarta':
        media = sum(volume) / 5
somatotal = sum(volume)

print(f'A soma total de volume é: {somatotal}\nE a média de volume nas quartas feiras é de: {media:.2f} ')
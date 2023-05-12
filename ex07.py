import os 
os.system ('cls')

distancia = float(input('Digite aqui o valor da distância:'))
cm = distancia * 100
mm = distancia * 1000
dam = distancia / 10
km = distancia / 1000
hm = distancia / 100
dm = distancia * 10 

print(f'A distância {distancia} em cm é de {cm:.0f} cm em milimetros é {mm:.0f} mm')
print (f'Em decametro {dam:.1f} dm')
print (f'Em km {km:.3f} km')
print (f'Em hm {hm:.2f} hm')
print (f'Em dm {dm:.0f} dm')
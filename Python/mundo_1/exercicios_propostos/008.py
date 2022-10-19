metros = float(input('Digite uma distância em metros: '))

print(f'A medida de {metros}m corresponde a: ')
print(f' {metros / 1000}km \n {metros / 100}hm \n {metros / 10}dam \n {metros * 10:.0f}dm \n {metros * 100:.0f}cm \n {metros * 1000:.0f}mm')

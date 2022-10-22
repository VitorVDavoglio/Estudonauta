dist = float(input('Digite a distância da viagem: '))

if (dist <= 200):
    passag = dist * 0.50
else:
    passag = dist * 0.45

# passag = dist * 0.50 if dist <=200 else dist * 0.45

print(f'O valor da passagem é: {passag}')

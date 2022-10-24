peso = float(input('Qual é a seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}.')

if imc < 18.5:
    print('Com esse IMC o usuário está Abaixo do Peso.')
elif imc < 25:
    print('Com esse IMC o usuário está com o Peso Ideal.')
elif imc < 30:
    print('Com esse IMC o usuário está com Sobrepeso.')
elif imc < 40:
    print('Com esse IMC o usuário está com Obesidade.')
else: 
    print('Com esse peso o usuário está com Obesidade Mórbida')

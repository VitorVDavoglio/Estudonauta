resp = 0
while resp == 0:
    sexo = str(input('Digite o seu sexo [F/M]: '))
    if sexo == 'F' or sexo == 'M':
        print('Parabéns, você digitou corretamente.')
        resp = 1
    else:
        print('Tente novamente....')

if sexo == 'M':
    print('Sexo Masculino registrado com sucesso!')
else:
    print('Sexo Feminino registrado com sucesso!')

#sexo = str(input('Informe seu sexo: [M/F] )).strip().upper()[0]
#while sexo not in 'MF':
#    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
#print(f'Sexo {sexo} registrado com sucesso)

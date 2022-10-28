resp = 0
while resp == 0:
    sexo = str(input('Digite o seu sexo [F/M]: '))
    if sexo == 'F' or sexo == 'M':
        print('Parabéns, você digitou corretamente.')
        resp = 1
    else:
        print('Tente novamente....')

print('Programa encerrando....')

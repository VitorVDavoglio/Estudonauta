vel = float(input('Qual a velocidade: '))

if (vel > 80):
    valor_multa = (vel_extra - 80) * 7
    print('Você excedeu a velocidade permitida.')
    print(f'O valor da multa é: R${valor_multa:.2f}')
else:
    print('Velocidade dentro do permitido, dirija com segurança!')

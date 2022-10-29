from random import randint

n_maquina = randint(0, 10)
n_usuario = 20
tentat = 0

while n_usuario != n_maquina:
    n_usuario = int(input('Digite um número de 0 a 10 e tente adivinhar qual é: '))
    tentat += 1
    if n_usuario < n_maquina:
        print('Mais... tente novamente.')
    else:
        print('Menos... tente novamente.')
    print('-------------------------------')

print(f'Parabéns é o número {n_usuario} mesmo. Jogue novamente!')
print(f'--> Números de tentativas: {tentat}')

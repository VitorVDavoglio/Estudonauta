from email import message


print('Olá, Mundo!')

nome = input('Qual é o seu nome? ')

print(f'Olá {nome}, seja bem vindo.')

dia = input('Dia = ')
mes = input('Mês = ')
ano = input('Ano = ')

print(f'{nome} você nasceu no dia {dia} de {mes} de {ano}. Correto? ')

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

print(f'A soma dos números digitados é: {num1 + num2}')

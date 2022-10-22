nome = str(input('Digite o seu nome completo: '))

nome1 = nome.split()
quant = len(nome1) - 1
print(f'Primeiro nome: {nome1[0]}')
print(f'Último nome: {nome1[quant]}')

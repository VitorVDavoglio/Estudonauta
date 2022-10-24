valor = int(input('Digite um número inteiro: '))
print('Qual será a base de conversão do número digitado? ')
escolha = int(input('[1] Binário\n[2] Octal\n[3] Hexadecimal\n-->'))

if escolha == 1:
    print(f'Número convertido para binário: \033[7m{bin(valor)[2:]}\033[m') 
elif escolha == 2:
    print(f'Número convertido para Octal: \033[7m{oct(valor)[2:]}\033[m')
elif escolha == 3: 
    print(f'Número convertido para Hexadecimal: \033[7m{hex(valor)[2:]}\033[m')
else:
    print('Valor inválido, tente novamente.')

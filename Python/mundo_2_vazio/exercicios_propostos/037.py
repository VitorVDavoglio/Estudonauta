valor = int(input('Digite um número inteiro: '))
print('Qual será a base de conversão do número digitado? ')
escolha = int(input('[1] Binário\n[2] Octal\n[3] Hexadecimal\n-->'))

if escolha == 1:
    binario = '{0:b}'.format(valor)
    print(f'Número convertido para binário: \033[7m{binario}\033[m') 
elif escolha == 2:
    octal = '{0:o}'.format(valor)
    print(f'Número convertido para Octal: \033[7m{octal}\033[m')
else: 
    hexa = '{0:x}'.format(valor)
    print(f'Número convertido para Hexadecimal: \033[7m{hexa}\033[m')

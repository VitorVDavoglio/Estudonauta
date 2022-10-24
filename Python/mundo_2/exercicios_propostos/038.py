n1 = int(input('Digite um valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print(f'O valor \033[32m{n1}\033[m é \033[34mmaior\033[m que o \033[31m{n2}\033[m')
elif n2 > n1:
    print(f'O valor \033[32m{n2}\033[m é \033[34mmaior\033[m que o \033[31m{n1}\033[m')
else:
    print(f'Não existe valor maior, os dois são \033[34miguais\033[m.')

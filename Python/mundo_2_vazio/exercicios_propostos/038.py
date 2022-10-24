n1 = int(input('Digite um valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print(f'O valor {n1} é \033[34mmaior\033[m que o {n2}')
elif n2 > n1:
    print(f'O valor {n2} é \033[34mmaior\033[m que o {n1}')
else:
    print(f'Não existe valot maior, os dois são \033[34miguais\033[m.')

for i in range(1, 6):
    n1 = int(input('Digite um número: '))
    print(f'-> Tentativa: {i}')
    if (n1 % 2 != 0) and (n1 % n1 == 0): 
        print('\033[31mNão é um numero primo.\033[m')
    else:
        print('\033[32mÉ um número primo.\033[m')
print('Fim do programa.')
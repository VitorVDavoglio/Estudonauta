n1 = int(input('Digite um número: '))

verif = True
for c in range(2, n1):
    if n1 % c == 0:
        verif = False

if verif:
    print('\033[32mÉ um número primo.\033[m')
else: 
    print('\033[31mNão é um numero primo.\033[m')

print('Fim do programa.')


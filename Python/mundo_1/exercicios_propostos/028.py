import random

n1 = int(input('Digite um número entre 0 e 5: '))
n2 = int(random.randint(0,5))

print(f'Números selecionados na ordem: {n1} e {n2}')

if (n1 == n2):
    print('Você ganhou.') 
else:
    print('Você perdeu.') 

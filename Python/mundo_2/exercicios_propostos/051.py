n1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da P.A.: '))

for i in range(1, 11):
    if i == 10:
        print(n1, end='.')
    else: 
        print(n1, end=', ')
    n1 += razao
print('')
print('Fim da P.A.')
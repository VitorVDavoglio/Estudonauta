n1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da P.A.: '))

valor_final = n1 + (10 - 1) * razao
while n1 <= valor_final:
    if n1 == valor_final:
        print(f'{n1}.')
    else:
        print(n1, end=', ')
    n1 += razao
print('Programa finalizando')

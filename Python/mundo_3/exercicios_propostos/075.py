a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))
d = int(input('Digite um valor: '))

valores = (a, b, c, d)

print(f'O número 9 aparece {valores.count(9)} vezes na lista.')

if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3) + 1} posição.')
else:
    print(f'Não ha o valor 3 na tupla.')

print(f'Os números pares digitados foram: ', end='')

for i in range(0, len(valores)):
    if valores[i] % 2 == 0:
        print(valores[i], end=', ')

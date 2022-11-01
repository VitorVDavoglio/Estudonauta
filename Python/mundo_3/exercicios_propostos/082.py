lista = []
lista_par = []
lista_impar = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    resp = str(input('Quer continuar? [S/N] -> ')).strip().upper() [0]
    if resp in 'N':
        break

print('-=' * 20)
print(f'A lista completa é {lista}.')
print(f'A lista de pares é {lista_par}.')
print(f'A lista de ímpares é {lista_impar}.')

soma = 0
cont = 0
for i in range(1, 501, 2):
    if (i % 3 == 0):
        print(i,end=' ')
        soma += i
        cont += 1
print('')
print(f'A soma desses {cont} valores é igual a: {soma}')

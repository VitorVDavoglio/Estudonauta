grupo = list()
ind = list()
maior_peso = menor_peso = 0

while True:
    ind.append(str(input('Nome: ')))
    ind.append(float(input('Peso: ')))
    if len(grupo) == 0:
        maior_peso = menor_peso = ind[1]
    else:
        if ind[1] > maior_peso:
            maior_peso = ind[1]
        elif ind[1] < menor_peso:
            menor_peso = ind[1]
    grupo.append(ind[:])
    ind.clear()

    resp = str(input('Quer continuar? [S/N] -> ')).strip().upper()[0]
    if resp != 'S':
        break

print(f'Ao todo, você cadastrou {len(grupo)} pessoas.')
print(f'O maior peso foi de {maior_peso}Kg. Peso de ', end='')
for i in grupo:
    if i[1] == maior_peso:
        print(i[0],end='.. ')
print('')

print(f'O menor peso foi de {menor_peso}Kg. Peso de ',end='')
for i in grupo:
    if i[1] == menor_peso:
        print(i[0],end='.. ')

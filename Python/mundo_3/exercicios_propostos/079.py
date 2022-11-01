lista = []
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('\033[31mValor duplicado, não posso adicionar...\033[m')
    else:
        lista.append(num)
        print('\033[32mValor adicionado com sucesso...\033[m')

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('=-=' * 20)
print(f'Você digitou os valores {lista}')

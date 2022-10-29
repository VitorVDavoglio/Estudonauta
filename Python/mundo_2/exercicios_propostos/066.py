soma = num1 = cont = 0
while True:
    num1 = int(input('Digite um valor: '))
    if num1 == 999:
        print('Programa encerrando...')
        break
    soma += num1
    cont += 1
print(f'A quantidade de números digitados foi: {cont}')
print(f'A soma dos valores digitados é {soma}.')

while True:
    num1 = int(input('Digite um valor para ver a tabuada: [Valor negativo encerrará o programa] -> '))
    if num1 < 0:
        break
    for i in range (1, 11):
        print(f'{num1} x {i:2} = {num1 * i}')
    print('-' * 15)

print('Programa encerrado!')

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

resp = 0
while resp != 5:
    resp = int(input(' [1] Somar\n [2] Multiplicar\n [3] Maior\n [4] Novos números\n [5] Sair do programa\n -->'))
    if resp == 1:
        print(f'A soma dos valores : {n1 + n2}')
    elif resp == 2:
        print(f'A multiplicação dos valores é: {n1 * n2}')
    elif resp == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior valor digitado é {maior}')
    elif resp == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
    elif resp == 5:
        print('Programa sendo encerrado...')
    else:
        print('Valor errado, tente novamente.')
    print('-=-' * 10)
print('Obrigado por utilizar o programa!')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if (n1 > n2) and (n1 > n3):
    print(f'O maior valor é: {n1}')
elif (n2 > n1) and (n2 > n3):
    print(f'O maior valor é: {n2}')
else:
    print(f'O maior valor é: {n3}')

if(n1 < n2)  and (n1 < n3):
    print(f'O menor valor é: {n1}')
elif(n2 < n1) and (n2 < n3):
    print(f'O menor valor é: {n2}')
else:
    print(f'O menor valor é: {n3}')

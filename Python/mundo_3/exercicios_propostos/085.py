numeros = [[], []]
cont_par = cont_impar = 0

for cont in range(1, 8):
    num = int(input(f'Digite o {cont}º valor: '))
    if num % 2 == 0:    
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()

print('-=' * 30)
print(f'Os números pares são: {numeros[0]}')
print(f'Os números ímpares são: {numeros[1]}')

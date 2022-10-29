num1 = soma = quant = media = maior = menor = 0 

resp = 'S'
while resp == 'S':
    num1 = int(input('Digite valor para análise: '))
    soma += num1
    quant += 1
    if quant == 1:
        maior = menor = num1
    if num1 > maior:
        maior = num1
    if num1 < menor:
        menor = num1
    resp = input('Deja continuar digitando? [S/N]: ').upper()

print(f'A média dos números digitados é: {soma / quant}')
print(f'O maior e o menor valor respectivamente são: {maior} e {menor}')

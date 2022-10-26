soma = 0
for i in range(1, 7):
    n1 = int(input('Digite um valor: '))
    if n1 % 2 == 0:
        soma += n1

print(F'A soma dos números pares é {soma}.')

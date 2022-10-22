n1 = int(input('Digite um número entre 0 e 9999: '))

unidade = n1 // 1 % 10
dezena = n1 // 10 % 10
centena = n1 // 100 % 10
milhar = n1 // 1000 % 10

print(f'Milhar: {milhar}')
print(f'Centena: {centena}')
print(f'Dezena: {dezena}')
print(f'Unidade: {unidade}')

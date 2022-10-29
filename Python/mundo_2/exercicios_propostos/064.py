quant_num = soma_num = 0
num1 = int(input('Digite um valor [999 fará o programa encerrar] -> '))
while num1 != 999:
    quant_num += 1
    soma_num += num1
    num1 = int(input('Digite um valor [999 fará o programa encerrar] -> '))

print('Somando resultado...')
print('-=-' * 10)
print(f'A quantidade de números digitados foi: {quant_num}.')
print(f'E a soma deles é: {soma_num}.')

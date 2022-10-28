num1 = 1
quant_num = 0
soma_num = 0
while num1 != 999:
    num1 = int(input('Digite um valor [999 fará o programa encerrar] -> '))
    if num1 == 999:
        print('Somando resultado...')
    else:
        quant_num += 1
        soma_num += num1
print('-=-' * 10)
print(f'A quantidade de números digitados foi: {quant_num}.')
print(f'E a soma deles é: {soma_num}.')

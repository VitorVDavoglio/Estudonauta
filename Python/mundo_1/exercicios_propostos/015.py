kms = float(input('Quantos kilometros foram percorridos? '))
dias = int(input('Quantidade de dias com o cliente: ')) 

valor_dias = dias * 60
valor_kms = kms * 0.15

print(f'O valor total a ser pago é: {valor_dias + valor_kms:.2f}')

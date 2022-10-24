valor = float(input('Digite o valor do produto: R$'))
escolha = int(input('''Como será feito o pagamento: 
[1] À vista \033[34mdinheiro/cheque\033[m -> Com 10% de desconto.
[2] À vista no \033[34mcartão\033[m -> Com 5% de desconto.
[3] Em até \033[34m2x no cartão\033[m -> Com preço normal.
[4] \033[34m3x ou mais no cartão\033[m -> Com 20% de juros
-->'''))

if escolha == 1:
    print(f'Valor a ser pago: R${valor * 0.9:.2f} reais.')
elif escolha == 2:
    print(f'Valor a ser pago: R${valor * 0.95:.2f} reais.')
elif escolha == 3:
    print(f'Valor a ser pago: R${valor} reais.')
    print(f'Cada parcela ficará em R${valor / 2:.2f} reais.')
elif escolha == 4:
    valor_acre = valor * 1.20
    print(f'Valor a ser pago: R${valor_acre} reais.')
    parcela = int(input('Quantas parcelas? '))
    print(f'Cada parcela será de R${valor_acre / parcela:.2f} reais.')
else: 
    print('Opção inválida de pagamento. \033[31mERRO...\033[m')

nome_barato = ''
total_gasto = quant_1000 = mais_barato = cont = 0

print('-' * 15)
print(' LOJA BARATÃO ')
print('-' * 15)

while True:
    print('--> NOVO PRODUTO')
    nome = str(input('Digite o nome do produto: '))
    preco = float(input(f'Digite o valor de {nome}: R$'))
    total_gasto += preco
    cont += 1
    if cont == 1 or preco < mais_barato:
        mais_barato = preco
        nome_barato = nome
    if preco > 1000:
        quant_1000 +=1
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar as compras? [S/N] -> ')).upper()
    if resp == 'N':
        break

print(f'O total gasto foi de: {total_gasto}.')
print(f'A quantidade de produtos acima de R$ 1000 reais é: {quant_1000}')
print(f'O produto mais barato é de R${mais_barato} e é {nome_barato}.')

n1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da P.A.: '))
quant = int(input('Quantos números dessa P.A. você quer ver? '))

print(f'Os {quant} primeiros números dessa P.A. são: ')

for i in range(1, quant + 1):
    if i == quant:
        print(n1, end='.')
    else: 
        print(n1, end=', ')
    n1 += razao
print('')
print('Fim da P.A.')

from datetime import date

quant_menor = 0
for i in range(1, 8):
    ano = int(input('Digite o ano de nascimento: '))
    idade = (date.today().year) - ano 
    if idade < 21:
        quant_menor += 1

print(f'A quantidade que não atingiram a maioridade(21 anos) é: {quant_menor}.')
print('Fim do programa...')

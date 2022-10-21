frase = str(input('Digite uma frase a sua escolha: '))
quant_a = frase.count('a')
pri_a = frase.find('a',0) + 1
ult_a = frase.find('a',quant_a)

print(f'Quantas vezes repete a letra A? {quant_a}')
print(f'A posição que se encontra o primeiro A é: {pri_a}')
print(f'A posição que se encontra o último A é: {ult_a}')
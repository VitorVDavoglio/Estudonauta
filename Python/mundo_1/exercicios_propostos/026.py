frase = str(input('Digite uma frase a sua escolha: ')).upper()
quant_a = frase.count('A')
pri_a = frase.find('A') + 1
ult_a = frase.rfind('A') + 1

print(f'Quantas vezes repete a letra A? {quant_a}')
print(f'A posição que se encontra o primeiro A é: {pri_a}')
print(f'A posição que se encontra o último A é: {ult_a}')

maior = 0
menor = 999
for i in range(1, 6):
    peso = float(input('Digite o peso do usuário: '))
    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso

print(f'O maior peso digitado foi: {maior}Kgs.')
print(f'O menor peso digitado foi: {menor}Kgs.')

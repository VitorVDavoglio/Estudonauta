from random import randint

numeros = (randint(0,50), randint(0,50), randint(0,50), randint(0,50) ,randint(0,50))

print(f'Os números selecionados foram: {numeros}')
print(f'O maior número da lista é: {max(numeros)}')
print(f'O menor número da lista é: {min(numeros)}')

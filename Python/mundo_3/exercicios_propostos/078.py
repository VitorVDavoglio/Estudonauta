num = []
for i in range(0,5):
    num.append(int(input(f'Digite um valor para a posição {i}: ')))

print('=-=' * 20)
print(f'Os valores digitados foram {num}')
print(f'O maior número digitado foi {max(num)} e está na posição ',end = '')
for i, ma in enumerate(num):
    if ma == max(num):
        print(f'{i}.. ', end = '')
print('')
print(f'O menor número digitaado foi {min(num)} e está na posição ',end = '')
for i, mi in enumerate(num):
    if mi == min(num):
        print(f'{i}.. ', end = '')

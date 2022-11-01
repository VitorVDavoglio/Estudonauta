num = []
for i in range(0,5):
    num.append(int(input(f'Digite um valor para a posição {i}: ')))

print('=-=' * 20)
print(f'Os valores digitados foram {num}')
print(f'O maior número digitado foi\033[7m {max(num)} \033[me está na posição ',end = '')
for i, ma in enumerate(num):
    if ma == max(num):
        print(f'{i}.. ', end = '')
print('')
print(f'O menor número digitado foi\033[7m {min(num)} \033[me está na posição ',end = '')
for i, mi in enumerate(num):
    if mi == min(num):
        print(f'{i}.. ', end = '')

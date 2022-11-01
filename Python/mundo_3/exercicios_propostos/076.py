listagem = ('Canetas', 22.30, 'Caderno', 15.90, 'Lápis', 1.75, 
            'Transferidor', 4.2, 'Mochila', 120.32, 'Borracha', 2, 
            'Estojo', 25, 'Compasso', 9.99, 'Livros', 34.9)

print('-' * 40)
print(f'{"LISTAGEM PREÇOS":^40}')
print('-' * 40)

for i in range(0, len(listagem), 2):
    print(f'{listagem[i]:.<30}R$ {listagem[i + 1]:6.2f}')



# for i in range(0, len(listagem), 2):
#     print(f'{listagem[i]}',end='')
#     for j in range(len(listagem[i]), 25):
#         print('.',end='')
#     print(f'R$ {listagem[i + 1]:6.2f}')

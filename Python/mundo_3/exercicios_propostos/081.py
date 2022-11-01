from operator import invert


lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    print(f'\033[32m-> Adicionado com sucesso!!!\033[m')

    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'A quantidade de números digitados foi de: {len(lista)}.')
lista.sort(reverse = True)
print(f'A lista em ordem decrescente é: {lista}')    
if 5 in lista:
    print('O valor 5 está presente na lista.')
else:
    print('O valor 5 não está presente na lista')
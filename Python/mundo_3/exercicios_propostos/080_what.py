# ordem = []
# ordem.append(int(input('Digite um valor: ')))
# for i in range(0,4):
#     num = int(input('Digite um valor: '))
#     if num > max(ordem):
#         ordem.insert(num)
#         print('Número adicionado no final da lista.')
#     elif num < min(ordem):
#         ordem.insert(0,num)
#         print('Número adicionado no início da lista.')
#     elif num in ordem:
#         ordem.insert(ordem.index(num),num)
#     else:
#         for i in range(1,len(ordem)):
#             if num < ordem[i]:
#                 ordem.insert(i, num)
#                 print(f'Número adicionado na posição {i}')
#                 break

# print('=-=' * 20)
# print(f'Os valores digitados em ordem foram {ordem}.')


#---SOLUÇÃO GUANABARA---
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print('~~~' * 30)
print(f'Os valores digitados em ordem foram {lista}')
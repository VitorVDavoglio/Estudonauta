# lanche = ['Hamburger','Suco','Pizza','Pudim']

# lanche.append('Cookie') #Add a lista mais um elemento.
# print(lanche[4])
# lanche.insert(0,'Cachorro-Quente') #Add a lista na posição específica o item
# print(lanche[0])

# del lanche[3] #Eliminou a PIZZA
# lanche.pop(3) #Eliminou o Pudim
# if 'Cachorro-Quente' in lanche:
#     lanche.remove('Cachorro-Quente')
# print(lanche)

# valores = list(range(4,11)) #Cria uma lista com valores do 4 até 10
# print(valores)

# valor = [8,2,5,4,9,3,0]
# valor.sort() #Deixa em ordem crescente
# print(valor)
# valor.sort(reverse=True) #Deixa em ordem decrescente
# print(valor)

# val = []
# for cont in range(0,5):
#     val.append(int(input('Digite um valor: ')))

# for c, v in enumerate(val):
#     print(f'Na posição {c} encontrei o valor {v}!!!')
# print('Cheguei ao final da lista.')

# for i in range(0, len(val)):
#     print(f'Na posição {i} encontrei o valor {val[i]}!!!')
# print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a[:] #Desse jeito a lista B recebe só os valores da lista A, não tendo atualização na lista A.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

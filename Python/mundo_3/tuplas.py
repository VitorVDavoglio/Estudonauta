#TUPLAS -> são imutáveis, só será possível mudar quando o programa estiver parado.

lanche = ('Hambúrguer','Suco','Pizza','Pudim')
#print(lanche[1]) -> Suco
#print(lanche[-2]) -> Pizza
#print(lanche[2:]) -> ('Pizza', 'Pudim')

#lanche[1] = 'Refrigerante' -> Não pode substituir durante a execução, só na matriz.

#for cont in range(0, len(lanche)):
#    print(f'Eu vou comer {lanche[cont]}')

#print('-' * 15) 

#for comida in lanche:
#    print(f'Hoje vou comer {comida}')
#print('Comi muito!!')
#print(f'Foram {len(lanche)} vezes.')

#print('-' * 15)

#for pos, comida in enumerate(lanche):
#    print(f'Eu vou comer {comida} na posição {pos}.')

#print(sorted(lanche))
#print(lanche)

a = (2, 5, 4)
print(f'a = {a}')
b = (5, 8, 1, 2)
print(f'b = {b}')
c = a + b
print(f'c = {c}')
print(f'O número 5 aparece: {c.count(5)} vezes.')
print(f'a posição do número 8 é: {c.index(8) + 1}.')
d = b + a 
print(f'd = {d}')

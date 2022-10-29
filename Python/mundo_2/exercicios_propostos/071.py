nota_50 = nota_20 = nota_10 = nota_1 = 0

print('=' * 15)
print(' BANCO ESTUDONAUTA ')
print('=' * 15)

valor = int(input('Qual o valor deseja sacar? R$')) 
while valor > 0:
    if valor % 50 == 0:
        valor -= 50
        nota_50 += 1
    elif valor % 20 == 0:
        valor -= 20
        nota_20 += 1
    elif valor % 10 == 0:
        valor -= 10
        nota_10 += 1
    elif valor % 1 == 0:
        valor -= 1
        nota_1 += 1
    else:
        break
 
print('=' * 30)
print(f'Notas de R$50 reais saindo: {nota_50}.')
print(f'Notas de R$20 reais saindo: {nota_20}.')
print(f'Notas de R$10 reais saindo: {nota_10}.')
print(f'Notas de R$1 reais saindo: {nota_1}.')

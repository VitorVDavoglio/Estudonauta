idade = mais_18 = homens = mulher_menor = 0

while True:
    print('-' * 23)
    print(' CADASTRO DE CLIENTES ')
    print('-' * 23) 

    idade = int(input('Digite a idade do usuário: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo: [F/M] -> ')).strip().upper()[0]

    if idade > 18:
        mais_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menor += 1
    fim = str(input('Deseja continuar? [S/N] -> ')).upper()
    if fim == 'N':
        break
    print('-=-' * 10)

print('~' * 20)
print(f'A quantidade de pessoas mairos de 18 anos é: {mais_18}.')
print(f'A quantidade de homens cadastrados é: {homens}.')
print(f'A quantidade de mulheres com menos de 20 anos é: {mulher_menor}.')

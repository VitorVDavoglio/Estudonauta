soma_idade = 0 
maior_idade_homem = 0
nome_mais_velho = ''
cont_menor = 0
for i in range(1, 5):
    print(f'----- {i}º PESSOA  -----')
    nome = input('Nome do cliente: ').strip()
    idade = int(input('Idade do cliente: '))
    sexo = input('Sexo do cliente: [F/M] ').strip().upper()

    soma_idade += idade

    if sexo in 'MMASCULINO':
        if idade > maior_idade_homem:
            nome_mais_velho = nome
            maior_idade_homem = idade

    if (sexo in'FFEMININO') and idade < 20:
        cont_menor += 1

print('-=-' * 15)
print(f'A média das idades dos clientes é de: {soma_idade / 4} anos.')
print(f'O {nome_mais_velho} é o homem mais velho com {maior_idade_homem} anos. ')
print(f'A quantidade de mulhers com menos de 20 anos é {cont_menor}.')

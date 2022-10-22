nome = str(input('Digite o seu nome completo: '))

print(nome.upper())
print(nome.lower())
print("A quantidade " , len(nome) - nome.count(' '))

nome_curto = nome.split()
print("O tamanho do primeiro nome é:" , len(nome_curto[0]))

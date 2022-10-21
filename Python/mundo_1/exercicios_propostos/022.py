nome = str(input('Digite o seu nome completo: '))

print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))

nome_curto = nome.split()
print(len(nome_curto[0]))

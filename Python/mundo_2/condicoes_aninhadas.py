nome = str(input('Qual é seu nome: '))

if (nome == 'Vitor'):
    print('Que nome bonito!')
elif (nome == 'João') or (nome == 'Maria'):
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica':
    print('Belo nome feminino.')
else: 
    print(f'Tenha um bom dia {nome}.')

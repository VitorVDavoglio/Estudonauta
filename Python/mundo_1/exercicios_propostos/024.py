cidade = str(input('Digite o nome da sua cidade: ')).strip()
cidade = cidade.upper()
cidade_corte = cidade[:6]
verif = 'SANTO' in cidade_corte

print(f'A sua cidade começa com a palavra santo? {verif}') 
print('')

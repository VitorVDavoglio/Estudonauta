pos_times = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 'Athletico-PR', 'Atlético-MG', 'São Paulo', 'Fortaleza', 'Botafogo', 'América-MG', 'Santos', 'Goiás', 'Bragantino', 'Chapecoense', 'Cuiába', 'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude')

print('-=-' * 35)
print(f'Os 5 primeiros colocados são os times: {pos_times[0:5]}')
print('-=-' * 35)
print(f'Os últimos 4 colocados na tabela são: {pos_times[-4:]}')
print('-=-' * 35)
print(f'Em ordem alfabética: {sorted(pos_times)}')
print('-=-' * 35)
print(f'O time da chapecoense está na {pos_times.index("Chapecoense") + 1} colocação.')
print('-=-' * 15)

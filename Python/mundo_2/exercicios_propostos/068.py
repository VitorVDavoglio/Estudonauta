from random import randint
pontos_jogador = 0
while True:
    print('=-=' * 10)
    print(' VAMOS JOGAR PAR OU ÍMPAR ')
    print('=-=' * 10)

    escolha_jogador = str(input('Escolha: Par ou Ímpar [P/I]--> ')).strip().upper()[0]
    while escolha_jogador not in 'PI':
        escolha_jogador = str(input('Escolha: Par ou Ímpar [P/I]--> ')).strip().upper()[0]
    num_jogador = int(input(f'Digite o seu valor: '))

    num_pc = randint(0,21)
    soma = num_jogador + num_pc
    print(f'Você jogou {num_jogador} e o computador jogou {num_pc} . Total de {soma}.')
    if escolha_jogador == 'P' and soma % 2 == 0:
        pontos_jogador += 1
        print('\033[32mVocê ganhou essa!\033[m')
    elif escolha_jogador == 'I' and soma % 2 != 0:
        pontos_jogador += 1
        print('\033[32mVocê ganhou essa!\033[m')
    else: 
        print('\033[31mVocê perdeu esssa!\033[m')
        break
    print('Vamos jogar novamente')
print(f'\033[31mGAME OVER!\033[m O jogador ganhou {pontos_jogador} vezes.')   
    
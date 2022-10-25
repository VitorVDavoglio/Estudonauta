from random import randint
escolha_comp = randint(1,3)

print('Bem vindo ao jogo: Pedra, Papel e Tesoura.\n Qual deseja escolher?')
escolha_player = int(input('[1]Pedra  [2]Papel  [3]Tesoura \n -->'))

if escolha_comp == escolha_player:
    print('Jogo empatado, ambos escolheram a mesma ferramenta, tente novamente.')

#COMPUTADOR GANHANDO
if escolha_comp == 1 and escolha_player == 3:
    print('\033[31mNão foi dessa vez\033[m, a Pedra ganhou da tesoura.')
elif escolha_comp == 2 and escolha_player == 1:
    print('\033[31mNão foi dessa vez\033[m, o Papel ganhou da Pedra.')
elif escolha_comp == 3 and escolha_player == 2:
    print('\033[31mNão foi dessa vez\033[m, a Tesoura ganhou do Papel.')
else:
    if escolha_player == 1 and escolha_comp == 3:
        print('\033[32mVocê ganhou\033[m, a Pedra ganhou da tesoura.')
    elif escolha_player == 2 and escolha_comp == 1:
        print('\033[32mVocê ganhou\033[m, o Papel ganhou da Pedra.')
    elif escolha_player == 3 and escolha_comp == 2:
        print('\033[32mVocê ganhou\033[m, a Tesoura ganhou do Papel.')

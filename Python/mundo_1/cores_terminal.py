# \033[ m
# style/text/back
# 0;33;44 ()

# none(0) bold(1) Underline(4) negativo(7) 
# branco(30) vermelho(31) verde(32) amarelo(33) azul(34) roxo(35) azul-claro(36) cinza(37) 
# branco(40) vermelho(41) verde(42) amarelo(43) azul(44) roxo(45) azul-claro(46) cinza(47) 

print('\033[0;30;41mteste\033[m')
print('\033[4;33;44mteste\033[m')

a = 5
b = 7
print(f'Os valores são \033[0;32m{a}\033[m e \033[0;31m{b}\033[m!!!')

#OUTRA OPÇÃO
nome = 'Vítor'
print(f'Olá! Muito prazer em te conhecer, \033[0;32;47m{nome}\033[m')

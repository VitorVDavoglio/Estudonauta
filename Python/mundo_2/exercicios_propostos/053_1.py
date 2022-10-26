frase = input('Digite uma frase e descubra se é um \033[34,4mPalíndromo\033[m: ').strip().lower().split() #tira os espaços da frente, deixa tudo em minúscula e separa a frase em palavras.
frase = ''.join(frase)  #Junta as palavras em uma frase sem os espaços.

final = len(frase) - 1
cont = int(len(frase) / 2) 
if cont % 2 != 0:
    cont -= 1

verf = 0
for i in range(0, cont):
    if frase[i] == frase[final]:
        verf += 1
    final -= 1

if verf == cont:
    print('\033[32mA frase é um Palíndromo\033[m')
else:
    print('\033[31mA frase não é um pálindromo\033[m')

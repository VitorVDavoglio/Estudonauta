#import bebida (pacote completo)
#from doce import ... (uma que vai ser escrita nos tres pontos)

import math
import random 
import emoji #No prompt escreve 'pip install emoji'
 
#ceil -> arredondamento para cima
#floor -> arredondamento para baixo
#trunc -> vai eliminar da virgula para frente e não vai arredondar
#pow -> potencia
#sqrt-> raiz quadrada
#factorial -> fatorial

#from math import sqrt

num1 = int(input('Digite um número: '))
raiz = math.sqrt(num1)

print(f'A raiz do número {num1} é {raiz} e arredondando para baixo fica: {math.floor(raiz)}')

alea = random.randint(1, 10)
print(alea) 
print(emoji.emojize('Python is :thumbs_up:'))
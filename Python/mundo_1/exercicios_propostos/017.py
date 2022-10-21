from cmath import sqrt

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hip = hypot(co, ca)
#hip = sqrt((co ** 2) + (ca ** 2))
#hip = (co ** 2 + ca ** 2) ** (1/2)

print(f'A hipotenusa vai demir: {hip:.2f}') 

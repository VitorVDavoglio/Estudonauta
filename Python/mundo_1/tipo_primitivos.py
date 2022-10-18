# int -- 7 -4 0 9875 
# float -- 4.5 0.076 -15.223
# bool -- True False
# str -- 'Olá' '7.5' ''

n1 = input('Digite um valor: ')
n2 = int(input('Digite outro valor: '))
tipo_n1 = type(n1)

print(f'O tipo do valor digitado {n1} é {tipo_n1} ')

n1 = int(n1)
s = n1 + n2 
print(f'A soma do valor {n1} + {n2} é {s}')

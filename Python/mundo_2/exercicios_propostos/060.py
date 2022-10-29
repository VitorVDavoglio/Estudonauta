num1 = int(input('Digite um número para o fatorial: '))
valor = num1
mult = 1
print(f'Calculando {num1}! = ', end='')
while valor > 0:
    print(f'{valor}', end='')
    if valor > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    mult *= valor 
    valor -= 1

print(f'{mult}')

#from math inport factorial
#n = int(input('Digite um número para calcular seu Fatorial: '))
#f = factorial(n)
#print('O fatorial de {n} é {f})

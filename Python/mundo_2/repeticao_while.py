#while not X:
#   passo
#pega

#c = 1                   for c in range(1,10):
#while c < 10:               print(c)
#    print(c)
#    c+= 1

resp = 'S'
par = impar = 0
while resp == 'S':
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
    resp = str(input('Quer continuar? [S/N] ')).upper()
print(f'Você digitou {par} números pares e {impar} números ímpares.')
print('Fim')

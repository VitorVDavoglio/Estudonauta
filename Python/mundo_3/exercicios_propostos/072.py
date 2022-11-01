numeros = ('zero', 'um', 'dois','três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
        
    num = int(input('Digite um número entre 0 e 20: '))
    while num < 0 or num > 20:
        num = int(input('Tente novamente. Digite um número de 0 a 20: '))

    print(f'Você digitou o número \033[31m{numeros[num]}\033[m.')

    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
    print('-' * 20)
    
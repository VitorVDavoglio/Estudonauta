print('\033[33m-=-\033[m' * 13)
print('Analisador de Triângulos.')
print('\033[33m-=-\033[m' * 13)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
print('\033[33m-=-\033[m' * 13)

if (a + b > c) and (a + c > b) and (b + c > a):
    print('\033[32mOs segmentos acima PODEM FORMAR triângulo!\033[m')
    if (a == b == c):
        print('Como todos os lados são iguais então é formado um triângulo \033[7mEQUILÁTERO\033[m') 
    elif (a != b != c != a):
        print('Como todos os lado são diferentes é formado um triângulo \033[7mESCALENO\033[m')
    else: 
        print('Como só ha dois lados iguais é formado um triângulo \033[7mISÓSCELES\033[m')
else:
    print('\033[31mOs segmentos acima NÃO PODEM FORMAR triângulo!\033[m')

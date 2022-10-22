cores = {'limpa':'\033[m', 
         'azul': '\033[34m', 
         'amarelo':'\033[33m', 
         'vermelho':'\033[31m'}

print('\033[33m-=-\033[m' * 13)
print('Analisador de Triângulos.')
print('\033[33m-=-\033[m' * 13)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    print('\033[32mOs segmentos acima PODEM FORMAR triângulo!\033[m')
else:
    print('\033[31mOs segmentos acima NÃO PODEM FORMAR triângulo!\033[m')

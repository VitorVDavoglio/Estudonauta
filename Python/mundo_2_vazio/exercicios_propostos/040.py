nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'\033[31mREPROVADO\033[m, média final de: {media} pontos.')
elif media >= 5 and media < 7:
    print(f'\033[33mRECUPERAÇÃO\033[m, média final de: {media} pontos.')
else: 
    print(f'\033[32mAPROVADO\033[m, média final de: {media} pontos.')
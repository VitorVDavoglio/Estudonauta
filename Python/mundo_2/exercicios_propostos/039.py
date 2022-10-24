from datetime import date

ano = int(input('Digite o ano de nascimento do jovem: '))

idade = (date.today().year) - ano

if idade < 18:
    print('\033[32mAinda não chegou a idade para se alistar.\033[m')
    print(f'Faltam {18 - idade} anos.')
elif idade == 18:
    print('Está na idade para o alistamento obrigatório.')
else:
    print('\033[31mJá passou a hora de se alistar.\033[m')
    print(f'Passaram {idade - 18} anos do alistamento orbigatório.')

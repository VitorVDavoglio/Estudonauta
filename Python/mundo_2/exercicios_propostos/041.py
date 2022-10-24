from datetime import date

ano = int(input('Digite o ano de nascimento do atleta: '))
idade = (date.today().year) - ano

if idade <= 9:
    print('\033[34mMIRIM\033[m')
elif idade <= 14:
    print('\033[34mINFANTIL\033[m')
elif idade <= 19:
    print('\033[34mJUNIOR\033[m')
elif idade <= 25:
    print('\033[34mSÊNIOR\033[m')
else:
    print('\033[34mMASTER\033[m')
    
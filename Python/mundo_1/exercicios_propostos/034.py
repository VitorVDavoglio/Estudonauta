salario = float(input('Digite seu salário: R$'))

if (salario > 1250):
    novo_salario = salario + (salario * 0.10)
else:
    novo_salario = salario + (salario * 0.15)

print(f'O valor do novo sálario é: R${novo_salario:.2f}.')

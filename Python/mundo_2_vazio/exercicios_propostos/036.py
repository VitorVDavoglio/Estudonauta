valor_casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o valor do salário do comprador? '))
anos = int(input('Em quantos anos deseja pagar a casa? '))

prestacao = valor_casa / (anos * 12)
parte_salario = salario * 0.3

if (prestacao <= (parte_salario)):
    print(f'O valor da prestação será de R${prestacao} e não excede o valor de 30% do salário que fica em R${parte_salario}')
    print('\033[32mEmpréstimo aprovado.\033[m')
else: 
    print(f'A prestação excede 30% do salário em R${prestacao - parte_salario}')
    print('\033[31mEmpréstimo negado.\033[m')
expr = str(input('Digite a sua expressão: '))

pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop() #Remove o último elemento da lista
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('\033[32mSua expressão está válida!\033[m')
else:
    print('\033[31mSua expressão está errada!\033[m')
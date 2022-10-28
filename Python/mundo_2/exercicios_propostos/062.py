n1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da P.A.: '))
quant_termos = 10
quant_termos_aux = 1
aux = n1
while quant_termos_aux != 0:
    valor_final = n1 + (quant_termos - 1) * razao
    while aux <= valor_final:
        if aux == valor_final:
            print(f'{aux}.')
        else:
            print(aux, end=', ')
        aux += razao
    quant_termos_aux = int(input('Quantos termos a mais deseja ver? [0 para encerrar.]\n-->'))
    quant_termos += quant_termos_aux
    aux = n1 
print('Programa encerrado.')

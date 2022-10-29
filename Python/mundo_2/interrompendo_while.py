#while True:
    #if bloco:
        #passo
    #if espaço:
        #pula
    #if  moeda:
        #pega
    #if trofeu:
        #pula
        #break
#pega

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.')

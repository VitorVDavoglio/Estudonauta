ordem = []
ordem.append(int(input('Digite um valor: ')))
for i in range(0,4):
    num = int(input('Digite um valor: '))
    for j in range(0,len(ordem)):
        if num > ordem[j]:
            continue
        else: # num == ordem[j]:
            ordem.insert(i,num)
            continue
    print(ordem)

    
frase = 'Curso em Video Python' 
#        012345678901234567890

# print(frase[9])
# print(frase[9:14])
# print(frase[:5])
# print(frase[9::3])

# print(len(frase))                #Tamanho da string
# print(frase.count('o'))          #Contar quantas vezes repete a letra 'o'
# print(frase.count('o',0,13))     #Contando a letra 'o' até o espaço 12
# print(frase.find('deo')) 
# print(frase.find('Android'))     #Mostra se ha essa frase na string 
# print('Curso' in frase)

# -> TRANSFORMAÇÃO
# print(frase.replace('Python','Android'))
# print(frase)

#print(frase.upper())           #Deixa toda a frase em maiúscula
#print(frase.lower())           #Deixa toda a frase em minúsculo
#print(frase.capitalize())      #Deixa só a primeira letra da primeira palavra em maiúsluca
#print(frase.title())           #Deixa todas as primeiras letras de cada palavra em maiúscula 
# frase.trip()                  #Retira todos os espaços desnecessários na frente e no final da string

# -> DIVISÃO
print(frase)
frase1 =frase.split()        #Vai dividir uma string em uma lista que cada palavra na sequencia é a numeração na lista
print(frase1)
frase2 = '-'.join(frase1)    #Vai juntar as palavras separadas e adicionar 
print(frase2)
print(frase1[1])

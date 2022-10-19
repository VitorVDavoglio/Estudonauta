largura = float(input('Largura da pareds: '))
altura = float(input('Altura da parede: '))

tamanho = largura * altura

print(f'Sua parade tem a dimensão de {largura:.2f} X {altura:.2f} e sua área é de {tamanho:.2f}m².')
print(f'Para pintar essa parede, você precisará de {tamanho/2:.2f}l de tinta.')

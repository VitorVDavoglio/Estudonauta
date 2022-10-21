import math

angulo = int(input('Digite o ângulo que você deseja: '))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print(f'O ângulo de {angulo} tem o SENO de {sen:.2f}')
print(f'O ângulo de {angulo} tem o COS de {cos:.2f}')
print(f'O ângulo de {angulo} tem o TAN de {tang:.2f}')

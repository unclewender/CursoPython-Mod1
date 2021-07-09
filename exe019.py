import random
n1 = str(input('Digite um nome:'))
n2 = str(input('Digite um nome:'))
n3 = str(input('Digite um nome:'))
lista = [n1, n2, n3]
nome = random.choice(lista)
print('O escolhido foi {}.'.format(nome))

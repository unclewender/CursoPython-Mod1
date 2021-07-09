from random import randint
from time import sleep

print('-=' * 20)

print('Vou pensar em um número de 0 a 5.')
res = randint(0, 5)
num = int(input('Que número eu pensei?'))

print('-=' * 20)
print('PROCESSANDO...')
sleep(2)
print('-=' * 20)

print('O número que eu pensei foi {} e sua resposta foi {}'.format(res, num))
if num == res:
    print('Carai viado lançou o bagulho certo memo.')
else:
    print('Viiiish se fudeu, tenta de novo manézao.')

print('-=' * 20)

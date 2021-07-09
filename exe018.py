import math
num = float(input('Digite o ângulo:'))
sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print('O ângulo {} tem o seno de {:.2f}.'.format(num, sen))
print('O ângulo {} tem o coseno de {:.2f}.'.format(num, cos))
print('O ângulo {} tem a tangente de {:.2f}.'.format(num, tan))
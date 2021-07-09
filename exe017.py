from math import hypot
ca = float(input('qual o valor do cateto adjacente?'))
co = float(input('qual o valor do cateto oposto?'))
h = hypot(ca, co)
print('o valor da hipotenusa é {:.2f}'.format(h))

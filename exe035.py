print('-=' * 25)
print('ANALISADOR DE TRIÂNGULOS')
print('-=' * 25)
a = float(input('Digite um segmento:'))
b = float(input('Digite um segmento:'))
c = float(input('Digite um segmento:'))
if a + b > c and a + c > b and b + c > a:
    print('Os valores {}, {} e {}, podem formar um triangulo.'.format(a, b , c))
else:
    print('Os valores {}, {} e {}, não podem formar um triangulo.'.format(a, b, c))

km = int(input('Quantos km tem sua viagem?'))
if km <= 200:
    valor = 0.50 * km
else:
    valor = 0.45 * km
print('Sua passagem custará: R${:.2f}'.format(valor))
print('Boa viagem!')
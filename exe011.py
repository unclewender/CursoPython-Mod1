print('Digite as dimensões da sua parede.')
altura = float(input('Qual a altura da parede?'))
largura = float(input('Qual a largura da sua parede?'))
area = altura * largura
print('Sua parede de {:.2f}x{:.2f} tem uma área de {}m².'.format(altura, largura, area))
tinta = area / 2
print('São necessários {}l de tinta para pinta-la'.format(tinta))
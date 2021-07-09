preço = float(input('Digite o valor do produto: R$'))
desconto = int(input('Digite o valor do desconto em %:'))
porc = preço - (preço * desconto / 100)
print('Com {}% de desconto o valor do seu produto vai para R${:.2f}.'.format(desconto, porc))

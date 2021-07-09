si = float(input('Qual valor do seu salário? R$'))
if si <= 1250.00:
    por = (si * 15) / 100 + si
else:
    por = (si * 10) / 100 + si
print('Seu salário atual: R${:.2f}\nSeu salário com o aumento: R${:.2f}'.format(si, por))
print('Parabens pelo seu aumento, você mereceu! S2')


vel = int(input('Velocidade do carro:'))
print('_=' * 30)
if vel <= 80:
    print('Continue dirigindo com segurança.')
else:
    print('VOCê ULTRAPASSOU O LIMITE PERMITIDO!')
    multa = float((vel - 80) * 7)
    print('O valor da multa é de R${:.2f}'.format(multa))

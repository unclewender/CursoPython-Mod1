salario = float(input('Digite o salário do funcionário: R$'))
aumento = int(input('Digite o valor em % do aumento salarial:'))
novo = salario + (salario * aumento / 100)
print('Com o aumento de {}% do salário, o funcionário irá receber R${:.2f} a partir de agora.'.format(aumento, novo))

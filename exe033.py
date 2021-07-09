n1 = int(input('digite numeros:'))
n2 = int(input('digite numeros:'))
n3 = int(input('digite numeros:'))
num = [n1, n2, n3]
menor = num[0]
maior = num[0]
for numero in num:
    if menor > numero:
        menor = numero
    if maior < numero:
        maior = numero
print('{} e o maior numero, e o menor é {}'.format(maior, menor))
frase = str(input('Digite uma frase:')).lower().strip()
print('sua frase tem {} letras "A"'.format(frase.count('a')))
print('a primeira letra "A" aparece na posição {}'.format(frase.find('a')+1))
print('a ultima letra "A" aparece na posição {}'.format(frase.rfind('a')+1))


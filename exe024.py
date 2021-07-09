# city = str(input('Digite onde você nasceu:'))
# minicity = city.lower()
# minicity.split()
# if 'santo' in minicity:
#     print('ok')
# else:
#     print('no')
city = str(input('Digite onde você nasceu:')).strip()
print(city[:5].lower() == 'santo')

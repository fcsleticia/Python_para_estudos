num=input('Digite um número de 4 digitos: ')
print('Unidade: {} \nDezenas: {}\nCentena: {}\nMilhar: {}'.format(num[3],num[2],num[1],num[0]))
print('Ou seja: ')
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))

#desafio24=str(input('Qual o nome da sua cidade? '))
#santo=(desafio24.split())
#print('O primeiro nome da sua cidade é {}'.format(santo[0]))

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() =='SANTO')

desafio25= str(input('Qual o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in desafio25.lower()))








nome=str(input('Coloque o seu nome completo: ')).strip()
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
name= nome.replace(' ',"")
print('O nome possui {} letras.'.format(len(name)))
nombre=nome.split()
print('Sendo que o primeiro nome é {} e possui {} letras.'.format(nombre[0],len(nombre[0])))

num=int(input('Digite um número de 4 digitos: '))
num2=str(num)
print('Unidade: {} \nDezenas: {}\nCentena: {}\nMilhar: {}'.format(num2[3],num2[2],num2[1],num2[0]))
print('Ou seja: ')
print('Unidade: {}'.format(num2[3]))
print('Dezena: {}'.format(num2[2]))
print('Centena: {}'.format(num2[1]))
print('Milhar: {}'.format(num2[0]))

num=int(input('Digite um número de 4 digitos: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))









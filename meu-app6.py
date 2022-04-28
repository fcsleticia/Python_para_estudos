a = int(input('Nota Primeiro Trimestre: '))
b = int(input('Nota Segundo Trimestre: '))
c = int(input('Nota Terceiro Trimestre: '))
d = int(input('Nota Quarto Trimestre: '))
media = (a + b + c + d) / 4
if a <= 25 and b <= 25 and c <= 25 and d <= 25:
    print('Média: {}' .format(media))
else:
    print('Foi informada alguma nota errada')


a = int(input('Nota Primeiro Trimestre: '))
if a > 25:
    a = int(input('Você digitou o valor errado. Primeiro Trimestre: '))
b = int(input('Nota Segundo Trimestre: '))
if b > 25:
    b = int(input('Você digitou o valor errado. Segundo Trimestre: '))
c = int(input('Nota Terceiro Trimestre: '))
if c > 25:
    c = int(input('Você digitou o valor errado. Terceiro Trimestre: '))
d = int(input('Nota Quarto Trimestre: '))
if d > 25:
    d = int(input('Você digitou o valor errado. Quarto Trimestre: '))

media = (a + b + c + d) / 4
print('Média: {}' .format(media))

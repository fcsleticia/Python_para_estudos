desafio26= str(input('Diga uma frase: ')).strip()
frase=desafio26.upper()
print ('Sua frase possui {} letras A.'.format(frase.count('A')))
print ('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print ('A última letra A aparece na posição {}'.format(frase.rfind('A')+1))

desafio27= str(input('Digite seu nome completo: ')).strip().title()
nome=desafio27.split()
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[len(nome)-1]))

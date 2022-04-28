n1=int(input('Exercicio 5: Digite um número e te darei o seu sucessor e o seu antecessor: '))
s = n1 + 1
a = n1 - 1
print('Se você utilizar o número {}, o seu antecessor será {} e o seu sucessor será {}.'. format(n1,a,s))
print('Muito obrigada')

n2=int(input('Exercicio 6: Digite um número e te darei o seu dobro, o seu triplo, a sua potenciação e a sua raiz quadrada: '))
d = n2 * 2
t = n2 * 3
p = n2 ** 2
r = n2 ** (1/2)
print('Se você utilizar o número {}, o seu dobro será {}, o seu triplo será {}, sua potência será {} e a sua raiz quadrada será {:.3f}'. format(n2,d,t,p,r))
print('Muito obrigada')

n3=int(input('Exercício 7: Lance a nota da primeira prova: '))
n4=int(input('Lance a nota da segunda prova: '))
m=(n3+n4)/2
print('Sendo a nota da primeira prova {} e a nota da segunda prova {}, a média do aluno foi {}'. format (n3,n4,m))

n5=int(input('Exercício 8: Dê a medida em metros e o sistema converterá em centimetros e milimetros: '))
cent=n5*100
mili=n5*1000
print('Se você possui {} metros, você possui {} centimetros e {} milimetros.'.format (n5,cent,mili))

n6=int(input('Exercício 9: Escolha um número e o sistema te dirá a tabuada deste valor: '))
m1=n6*1
m2=n6*2
m3=n6*3
m4=n6*4
m5=n6*5
m6=n6*6
m7=n6*7
m8=n6*8
m9=n6*9
m10=n6*10
print('Tabuada do {a}:\n'
      '{a} x 1 = {b}\n'
      '{a} x 2 = {c}\n'
      '{a} x 3 = {d}\n'
      '{a} x 4 = {e}\n'
      '{a} x 5 = {f}\n'
      '{a} x 6 = {g}\n'
      '{a} x 7 = {h}\n'
      '{a} x 8 = {i}\n'
      '{a} x 9 = {j}\n'
      '{a} x 10 = {k}\n'.format(a=n6,b=m1,c=m2,d=m3,e=m4,f=m5,g=m6,h=m7,i=m8,j=m9,k=m10))

din=float(input('Exercício 10: Fale quantos reais você possui e o sistema te dirá quantos dólares você conseguiria comprar com a cotação em $3,27: '))
dol=din/3.27
print('Com {} reais você conseguiria comprar {:.2f} dólares.'.format(din,dol))

alt=float(input('Exercicio 11: Você precisa pintar uma parede. Diga a sua altura: '))
larg=float(input('Agora diga a sua largura: '))
area=(alt*larg)
quant=area/2
print('Sabendo que cada litro de tinta tem a cobertura de 2 metros quadrados, para pintar uma parede com altura de {} e largura de {}'.format (alt,larg),
      'sendo sua área de {}, \n você precisará de {} litros de tinta.'.format(area,quant))

preco=float(input('Exercicio 12: Qual o preço do produto que irá ter 5% de desconto? '))
npreco= preco-(preco*0.05)
print('Sendo o preço antigo {}, com desconto de 5% o novo preço será {:.2f}.'.format(preco,npreco))

sal=float(input('Exercicio 13: Qual o salário atual do seu funcionário que terá 15% de aumento? '))
novo= (sal*0.15)+sal
print('Sendo o salário atual {}, com aumento de 15% o novo salário será {:.2f}.'.format(sal,novo))


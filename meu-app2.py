a = 11
b = 5
sum = a + b
subtraction = a - b
multiplication = a * b
division = a / b
rest = a % b

print(sum)
print(subtraction)
print(multiplication)
print(int (division))
print(rest)

print('sum: ' + str(sum))
print('subtraction: ' + str(subtraction))
print('multiplication:' +str(multiplication))
print('division:' + str(int (division)))
print('rest:' + str(rest))

print(sum)
print(subtraction)
print(multiplication)
print(int (division))
print(rest)

print('sum: {}'.format(sum))
print('subtraction: {}'.format(subtraction))
print('multiplication: {}'.format(multiplication))
print('division: {}'.format(int (division)))
print('rest: {}'.format(rest))

print('Sum: {}. Subtraction: {}. Multiplication: {}. Division: {}. Rest: {}'.format(sum, subtraction, multiplication, int(division), rest))

print('Sum: {}.'
      '\nSubtraction: {}.'
      '\nMultiplication: {}.'
      '\nDivision: {}.'
      '\nRest: {}'.format(sum,
                          subtraction,
                          multiplication,
                          int(division),
                          rest))

print('Sum: {result1}.'
      '\nSubtraction: {result2}.'
      '\nMultiplication: {result3}.'
      '\nDivision: {result4}.'
      '\nRest: {result5}'.format(result1=sum,
                          result2=subtraction,
                          result3=multiplication,
                          result4=int(division),
                          result5=rest))

print('Sum: {result1}.'
      '\nSubtraction: {result2}.'
      '\nMultiplication: {result3}.'
      '\nDivision: {result4}.'
      '\nRest: {result5}'.format(result5=rest,
                                 result1=sum,
                                 result4=int(division),
                                 result2=subtraction,
                                 result3=multiplication))

# x = 1
# sum2 = int(x) + 1
# print(sum2)

c = int( input('Entre com o primeiro valor: '))
d = int( input('Entre com o segundo valor: '))
sum2 = c + d
subtraction2 = c - d
multiplication2 = c * d
division2 = c / d
rest2 = c % d

print('Sum: {result1}.'
      '\nSubtraction: {result2}.'
      '\nMultiplication: {result3}.'
      '\nDivision: {result4}.'
      '\nRest: {result5}'.format(result5=rest2,
                                 result1=sum2,
                                 result4=int(division2),
                                 result2=subtraction2,
                                 result3=multiplication2))

Resultado = ('Sum: {result1}.'
      '\nSubtraction: {result2}.'
      '\nMultiplication: {result3}.'
      '\nDivision: {result4}.'
      '\nRest: {result5}'.format(result5=rest2,
                                 result1=sum2,
                                 result4=int(division2),
                                 result2=subtraction2,
                                 result3=multiplication2))
print(Resultado)


l1 = float(input('Digite o 1º lado do Triângulo: '))
l2 = float(input('Digite o 2º lado do Triângulo: '))
l3 = float(input('Digite o 3º lado do Triângulo: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Legal, podemos formar um Triângulo!')
else:
    print('Com esses valores não conseguimos formar uma Triângulo!')

'''
if l1 == l2 and l1 == l3 and l2 == l3:
    print('EQUILÁTERO: todos os lados iguais.')

if l1 != l2 and l1 != l3 and l2 != l3:
    print('ESCALENO: todos os lados são diferentes.')

if l1 == l2 and l1 != l3 or l1 == l3 and l1 != l2 or l2 == l3 and l2 != l1:
    print('ISÓCELES: dois lados iguais.')
'''

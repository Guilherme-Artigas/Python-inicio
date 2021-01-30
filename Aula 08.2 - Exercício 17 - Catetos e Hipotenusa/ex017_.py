from math import hypot

o = float(input('Digite o valor do cateto oposto: '))
a = float(input('Digite o valor do cateto adjacente: '))

hip = hypot(o, a)
# (o ** 2 + a ** 2) ** (1/2) ... outra opção para fazer esse calculo...

print('cateto oposto {} / cateto adjacente {} / valor da hipotenusa {:.2f}'.format(o, a, hip))

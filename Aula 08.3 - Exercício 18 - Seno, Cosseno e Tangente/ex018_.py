from math import cos, sin, tan, radians

n = float(input('Digite o valor de um ângulo: '))

c = cos(radians(n))
s = sin(radians(n))
t = tan(radians(n))

print('Valor do cosseno {:.1f}, valor do seno {:.1f}, valor da tangente {:.1f}'.format(c, s, t))

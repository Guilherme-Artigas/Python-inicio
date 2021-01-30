from math import sqrt, ceil  # Forma de importação de itens especificos de dentro da biblioteca.
import math  # Forma de importar a biblioteca toda.

n = int(input('Digite o número: '))
print('Raiz de {} = {:.2f}'.format(n, ceil(sqrt(n))))

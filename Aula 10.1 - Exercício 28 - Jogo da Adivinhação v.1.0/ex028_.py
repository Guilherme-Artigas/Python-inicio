from random import randint
from time import sleep

n = int(input('Digite um valor entre [1 e 5]: '))
s = randint(1, 5)


print('Processando!')
sleep(3)
if n >= 1 and n <= 5:
    if n == s:
        print('Parabens! Nº Sorteado {} / Nº Escolhido {}'.format(s, n))
    else:
        print('Infelizmente não deu! Nº Sorteado {} / Nº Escolhido {}'.format(s, n))
else:
    print('Você escolheu um valor invalido! {}... por favor digite entre 1 e 5.'.format(n))

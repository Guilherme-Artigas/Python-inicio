valor1 = int(input('Digite o 1º valor: '))
valor2 = int(input('Digite o 2º valor: '))
s = valor1 + valor2
m = valor1 * valor2
d = valor1 / valor2
di = valor1 // valor2
e = valor1 ** valor2
print('Soma: {}'.format(s))
print('Multiplicação: {}'.format(m))
print('Divisão: {:.2f}'.format(d)) # formatação de casas decimais, para numeros muito grandes.
print('Divisão Inteira: {}'.format(di))
print('Exponenciação: {}'.format(e))

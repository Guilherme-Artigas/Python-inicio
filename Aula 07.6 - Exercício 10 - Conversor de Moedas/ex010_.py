dolar = float(input('Digite a cotação do dólar atual US$ '))
reais = float(input('Quantos R$(reais), serão convertidos em dólar R$ '))

print()

print('Resultado da Converção: R${:.2f} / US${:.2f}'.format(reais, reais / dolar))

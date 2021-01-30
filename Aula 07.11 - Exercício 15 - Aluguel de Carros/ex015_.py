d = int(input('Quantidade de dias: '))
km = float(input('Quantidade de KM rodados: '))
vf = (60 * d) + (0.15 * km)
print('Valor total a pagar R${:.2f}'.format(vf))

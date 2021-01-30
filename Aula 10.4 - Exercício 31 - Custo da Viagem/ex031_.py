km = float(input('Digite a distancia percorrida em KM: '))

# Operador Ternario em Python
# valor = km * 0.50 if km <= 200 else km 0.45

if km <= 200:
    valor = 0.50 * km
    print('Valor a pagar R${:.2f}'.format(valor))
else:
    valor = 0.45 * km
    print('Valor a pagar R${:.2f}'.format(valor))

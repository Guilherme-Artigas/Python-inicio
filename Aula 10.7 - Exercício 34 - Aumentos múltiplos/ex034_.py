salario = float(input('Digite o valor do seu salario: '))

if salario >= 1251:
    salario += (salario * 10 / 100)
else:
    salario += (salario * 15 / 100)

print()
print('Parabens você ganhou um aumento! seu novo salario é {}'.format(salario))

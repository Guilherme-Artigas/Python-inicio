km = float(input('Digite um valor em KM e vamos converter: '))

print()

print('{}km = {} Metros'.format(km, km * 1000))
print('{}km = {:.4f} Milhas Náuticas'.format(km, km / 1.852))
print('{}km = {:.4f} Milhas'.format(km, km / 1.609))

print()

metros = float(input('Digite um valor em Metros e vamos converte-lo: '))

print()

print('{}Metros = {} km'.format(metros, metros / 1000))
print('{}Metros = {:.4f} Polegada'.format(metros, metros * 39.37))
print('{}Metros = {:.4f} Milha Náutica'.format(metros, metros / 1852))
print('{}Metros = {:.4f} Pés'.format(metros, metros * 3.281))

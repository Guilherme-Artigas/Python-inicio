from datetime import date

ano = int(input('Digite o ano: '))

if ano == 0:
    ano = date.today().year

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print('Legal {} é Bissexto!'.format(ano))
else:
    print('{} não é bissexto!'.format(ano))
